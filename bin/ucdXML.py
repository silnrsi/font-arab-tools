#!/usr/bin/env python
'''Access Unicode character properties.

NAME
  ucdXML

DESCRIPTION
  This module provides access to the Unicode Character Database (UCD) that
  defines character properties for all Unicode characters. The methods
  provided here are similar to those provided by python's built-in 
  unicodedata module.
  
  Rather than using a pre-computed fixed version of Unicode, however, this 
  module requires the user to supply the Unicode Data file as a parameter.
  
  Zipped versions of the needed file can be downloaded from 
  http://www.unicode.org/Public/UCD/latest/ucdxml or, by ftp, from
  ftp://ftp.unicode.org/Public/UCD/latest/ucdxml/. (Versions of these files
  from previous editions of the Unicode Standard are also available from
  http://www.unicode.org/Public/ and ftp://ftp.unicode.org/Public/.)
  
  Any of the files unpacked from the zip files downloaded from the ucdxml 
  folder can be used, but generally speaking the "grouped" files are more 
  efficient than the "flat" ones. For more information about these files, 
  see http://www.unicode.org/Public/UCD/latest/ucdxml/ucdxml.readme.txt 
  and http://www.unicode.org/reports/tr42/.
  
  This module assumes that for any given use you probably aren't concerned 
  with all characters of the Unicode standard. Therefore you indicate which
  Unicode blocks you are interested in by providing a compiled regular
  expression that is matched against the "blk" property of the characters.
  The list of possible "blk" property values is documented at
  http://www.unicode.org/reports/tr42/#d1e2159.
  
  If, for example, you were interested in all Latin, Arabic, and punctuation
  characters, you might pass the following in as the blkRegex parameter:
       re.compile(r'ascii|latin|arabic|punctuation', re.IGNORECASE)
  
  For the methods that lookup specific character properties, the char 
  parameter identifies the character of interest. With the unicodedata
  module, the parameter must be a single-character string (unicode string
  in Python 2). In contrast, this module provides multiple ways to identify 
  the character:
      - integer representing the USV
      - string of 4 to 6 hex digits, identifying the USV code point
      - any other string or unicode string, of which the first 
          character is taken as the desired character
  If the indicated character is not present in the retrieved UCD info (perhaps
  because it is in a block not matched by blkRegex), KeyError is raised.

EXAMPLES
  import re
  from ucdXML import ucdXML
  ucd = ucdXML('ucd.nounihan.grouped.xml', re.compile(r'ascii|arabic', re.IGNORECASE))

  for c in (32, '(', u'\u0623', '0650'):
    print ucd.getprop('cp', c), ': ', ucd.name(c)
    print '           mirrored: ', ucd.mirrored(c)
    print '      decomposition: ', ucd.decomposition(c)
    print '   general category: ', ucd.category(c)
    print '         bidi class: ', ucd.bidirectional(c)
    print '    combining class: ', ucd.combining(c)
    print '     arabic joining: ', ucd.getprop('jt', c)
    print '                age: ', ucd.getprop('age', c)
    
  print "UnicodeData version: ", ucd.unidata_version()

''' 
__url__ = 'http://github.com/silnrsi/font-arab-tools'
__copyright__ = 'Copyright (char) 2017 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Bob Hallissy'

import xml.sax
import re
import os.path

_usvRegex = re.compile(r'^[a-f-0-9]{4,6}$', re.IGNORECASE)

class ucdXML(object):
  'Provides methods to access Unicode character properties'

  def __init__(self, UCDxmlFile, blkRegex):
    '''Create object to be used to retrive Unicode character properties.
    
    Arguments:
    UCDxmlFile - path name of UCD xml file to be read (required).
    blkRegex - a compiled regular expression used to select the 
      portions of the UCD xml file to be retrieved. 
    '''
    
    class _UCDcontentHandler(xml.sax.ContentHandler):
      # state values:
      #  -1 = initial
      #   0 = within a <group> element, but not a desired one
      #   1 = within a desired <group> element
      #   2 = within <description> element
      def __init__(self, ucd, blkRegex):
        self.state = -1;
        self.pattern = blkRegex
        self.ucd = ucd
        self.ucd["version"] = ""
        xml.sax.ContentHandler.__init__(self)
      
      def startElement(self, name, attrs):
        if name == "description":
          self.state = 2
        elif name == "group":
          if "blk" in attrs and self.pattern.search(attrs.getValue("blk")):
            self.state = 1
            self.groupattrs = {}
            for name in attrs.getNames():
              self.groupattrs[name] = attrs.getValue(name)
          else:
            self.state = 0
        elif name == "char" and (self.state == 1 or \
               (self.state == -1 and "blk" in attrs and self.pattern.search(attrs.getValue("blk")))):
          # character data element.  Explanation of the above logic:
          #   If state == 1, then we're in a group and we know the group's block attribute matches what the caller wants.
          #   If state == -1, then we've never seen any groups, and thus this must be a "flat" UCD XML file. In this case
          #        every character has to have its block attribute tested.
          usv = int(attrs.getValue("cp"), 16)
          #print "%04X : %s" % (usv, attrs.getValue("na"))
          if self.state == 1:
            self.ucd[usv] = self.groupattrs.copy()
          else:
            self.ucd[usv] = {}
          for name in attrs.getNames():
            self.ucd[usv][name] = attrs.getValue(name)
      
      def endElement(self, name):
        if name == "description":
          self.ucd["version"] = re.search(r'(\d+\.\d+(?:\.\d+))', self.ucd["version"]).group()
          self.state = -1
          
      def characters(self, content):
        if self.state == 2:
          self.ucd["version"] += content

    self._ucd = {}
    source = open(UCDxmlFile)
    xml.sax.parse(source, _UCDcontentHandler(self._ucd, blkRegex))
    self._version = self._ucd.pop("version", None)
  
  def getprop(self, prop, char, default = None):
    '''Returns arbitrary Unicode Character property, as Unicode string.
    
    Arguments:
    prop: the property's name alias as defined in 
      Unicode's PropertyAliases.txt file (required).
    char: Unicode character (required).
    default: value to return if the property is not defined (optional).
    
    If no such property is defined for the specified character, default 
    is returned, or, if not given, ValueError is raised.
    '''
    # figure out what character is wanted.
    if isinstance(char,int):
      i = char
      #print "Integer: %d" % i
    elif isinstance(char,str):
      if _usvRegex.match(char):
        i = int(char,16)
        #print "Hex string: %d" % i
      else:
        i = ord(char[0])
        #print "String: %d" % i
    elif isinstance(char, unicode):
      i = ord(char[0])
      #print "Unicode: %d" % i
    else:
      # Can't interpret the parameter
      raise TypeError("cannot interpret character parameter:" + char)
    
    if not i in self._ucd:
      raise KeyError(char + " not found in ucd subset")
    elif not prop in self._ucd[i]:
      if default:
        return default
      else:
        raise KeyError("property %s not specified for U+%04X" % (prop, i))
    else:
      return self._ucd[i][prop]


  # for reference, UCD XML property aliases are defined at http://www.unicode.org/Public/UCD/latest/ucd/PropertyAliases.txt

  def category(self, char):
    '''Returns (as string) the general category assigned to char.'''
    return str(self.getprop('gc',char))
  
  def bidirectional(self, char):
    '''Returns (as string) the bidirectional class assigned to char.''' 

    # I think all characters have bidi property, so the default param should never get used,
    # but this is the way unicodedata module specs it
    return str(self.getprop('bc',char,'')) 
  
  def combining(self, char):
    '''Returns (as integer) the canonical combining class assigned char.'''
    return int(self.getprop('ccc',char, '0'))
  
  def east_asian_width(self, char):
    '''Returns (as string) the east asian width assigned to char.''' 
    return str(self.getprop('ea',char))

  def mirrored(self, char):
    '''Returns 1 if the character has the mirrored property, else 0.'''
    return 1 if self.getprop('Bidi_M', char, "N") == "Y" else 0

  def decomposition(self, char):
    '''Returns (as string) the character decomposition mapping assigned to char.'''
    x = self.getprop('dm', char)
    return ("" if x == "#" else x)
  
  def name(self, char, *args):
    '''Returns (as string) the name assigned to char.
    
    If no name is defined, default is returned, or, if not given, ValueError is raised.'''
    # UCD has empty string for 'na' property value for things that don't have names,
    # so we can't use our built-in default mechanism to mimic what unicodedata.name() does
    if len(args) > 1:  raise TypeError("name() takes at most 2 arguments (%s given)" % (len(args)+1))
    x = str(self.getprop('na', char))
    if x != "":        return x
    if len(args) == 1: return args[0]
    raise ValueError("no such name")

  def unidata_version(self):
    '''Returns (as string) the version of the Unicode database represented by UCDxmlFile.'''
    return self._version

# Not yet implemented:

#  def lookup(self, name, default = None):
#    raise NotImplementedError
#  
    
#  def decimal(self, char,default):
#    raise NotImplementedError
#  
#  def digit(self, char, default):
#    raise NotImplementedError
#  
#  def numeric(self, char, default):
#    raise NotImplementedError
#  
#  def normalize(self, form, unistr):
#    raise NotImplementedError

 
if __name__ == "__main__":
  ucd = ucdXML('ucd.nounihan.grouped.xml', re.compile(r'ascii|arabic', re.IGNORECASE))
  for c in (32, '(', u'\u0623', '0650', '08FF'):
    print ucd.getprop('cp', c), ': ', ucd.name(c)
    print '           mirrored: ', ucd.mirrored(c)
    print '      decomposition: ', ucd.decomposition(c)
    print '   general category: ', ucd.category(c)
    print '         bidi class: ', ucd.bidirectional(c)
    print '    combining class: ', ucd.combining(c)
    print '     arabic joining: ', ucd.getprop('jt', c)
    print '                age: ', ucd.getprop('age', c)
    print
  print "UnicodeData version: ", ucd.unidata_version()
