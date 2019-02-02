#!/usr/bin/env python
'generate ftml tests from glyph_data.csv and UFO'
__url__ = 'http://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2018 SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Bob Hallissy'

import re
from silfont.core import execute
import silfont.ftml_builder as FB
from icu import UCharCategory as GC

argspec = [
    ('ifont',{'help': 'Input UFO'}, {'type': 'infont'}),
    ('output',{'help': 'Output file ftml in XML format', 'nargs': '?'}, {'type': 'outfile', 'def': '_out.ftml'}),
    ('-i','--input',{'help': 'Glyph info csv file'}, {'type': 'incsv', 'def': 'glyph_data.csv'}),
    ('-f','--fontcode',{'help': 'letter to filter for glyph_data'},{}),
    ('-l','--log',{'help': 'Set log file name'}, {'type': 'outfile', 'def': '_ftml.log'}),
    ('--rtl', {'help': 'enable right-to-left features', 'action': 'store_true'}, {}),
    ('-t', '--test', {'help': 'which test to build', 'default': None, 'action': 'store'}, {}),
    ('-s','--fontsrc',{'help': 'default font source', 'action': 'append'}, {}),
    ('--scale', {'help': '% to scale rendered text'}, {}),
    ('--ap', {'help': 'regular expression describing APs to examine', 'default': '.', 'action': 'store'}, {}),
    ('--xsl', {'help': 'XSL stylesheet to use'}, {}),

]


def doit(args):
    logger = args.logger

    # Read input csv
    builder = FB.FTMLBuilder(logger, incsv = args.input, fontcode = args.fontcode, font = args.ifont, ap = args.ap, rtlenable = True)

    # Override default base (25CC) for displaying combining marks
    builder.diacBase = 0x0628   # beh

    # Initialize FTML document:
    test = args.test or "AllChars (NG)"  # Default to AllChars
    ftml = FB.FTML(test, logger, rendercheck = True, fontscale = args.scale, xslfn = args.xsl, fontsrc = args.fontsrc, defaultrtl = args.rtl)

    if test.lower().startswith("allchars"):
        # all chars that should be in the font:
        ftml.startTestGroup('Encoded characters')
        for uid in sorted(builder.uids()):
            if uid < 32: continue
            c = builder.char(uid)
            for featlist in builder.permuteFeatures(uids = (uid,)):
                ftml.setFeatures(featlist)
                builder.render((uid,), ftml)
            ftml.clearFeatures()
            for langID in sorted(c.langs):
                ftml.setLang(langID)
                builder.render((uid,), ftml)
            ftml.clearLang()

        # Add specials and ligatures that were in the glyph_data:
        ftml.startTestGroup('Specials & ligatures from glyph_data')
        for basename in sorted(builder.specials()):
            special = builder.special(basename)
            for featlist in builder.permuteFeatures(uids = special.uids):
                ftml.setFeatures(featlist)
                builder.render(special.uids, ftml)
                ftml.closeTest()
            ftml.clearFeatures()
            if len(special.langs):
                for langID in sorted(special.langs):
                    ftml.setLang(langID)
                    builder.render(special.uids, ftml)
                    ftml.closeTest()
                ftml.clearLang()

        # Add Lam-Alef data manually
        ftml.startTestGroup('Lam-Alef')
        lamlist = filter(lambda x: x in builder.uids(), (0x0644, 0x06B5, 0x06B6, 0x06B7, 0x06B8, 0x076A, 0x08A6))
        aleflist = filter(lambda x: x in builder.uids(), (0x0627, 0x0622, 0x0623, 0x0625, 0x0671, 0x0672, 0x0673, 0x0675, 0x0773, 0x0774))
        for lam in lamlist:
            for alef in aleflist:
                for featlist in builder.permuteFeatures(uids = (lam, alef)):
                    ftml.setFeatures(featlist)
                    builder.render((lam,alef), ftml)
                    ftml.closeTest()
                ftml.clearFeatures()

    if test.lower().startswith("diac"):
        # Diac attachment:

        # Representative base and diac chars:
        repDiac = filter(lambda x: x in builder.uids(), (0x064E, 0x0650, 0x065E, 0x0670, 0x0616, 0x06E3, 0x08F0, 0x08F2))
        repBase = filter(lambda x: x in builder.uids(), (0x0627, 0x0628, 0x062B, 0x0647, 0x064A, 0x77F, 0x08AC))
        lamlist = filter(lambda x: x in builder.uids(), (0x0644, 0x06B5, 0x06B6, 0x06B7, 0x06B8, 0x076A, 0x08A6))
        aleflist = filter(lambda x: x in builder.uids(), (0x0627, 0x0622, 0x0623, 0x0625, 0x0671, 0x0672, 0x0673, 0x0675, 0x0773, 0x0774))

        ftml.startTestGroup('Representative diacritics on all bases that take diacritics')
        for uid in sorted(builder.uids()):
            if uid < 32 or uid in (0xAA, 0xBA): continue
            c = builder.char(uid)
            # Always process Lo, but others only if that take marks:
            if c.general == GC.OTHER_LETTER or c.isBase:
                for diac in repDiac:
                    for featlist in builder.permuteFeatures(uids = (uid,diac)):
                        ftml.setFeatures(featlist)
                        builder.render((uid,diac), ftml, addBreaks = False)
                        if diac != 0x0651:  # If not shadda
                            # include shadda, in either order:
                            builder.render((uid, diac, 0x0651), ftml, addBreaks = False)
                            builder.render((uid, 0x0651, diac), ftml, addBreaks = False)
                        if diac != 0x0654:  # If not hamza above
                            # include hamza above, in either order:
                            builder.render((uid, diac, 0x0654), ftml, addBreaks = False)
                            builder.render((uid, 0x0654, diac), ftml, addBreaks = False)
                    ftml.clearFeatures()
                ftml.closeTest()

        ftml.startTestGroup('All diacritics on representative bases')
        for uid in sorted(builder.uids()):
            # ignore non-ABS marks
            if uid < 0x600 or uid in range(0xFE00, 0xFE10): continue
            c = builder.char(uid)
            if c.general == GC.NON_SPACING_MARK:
                for base in repBase:
                    for featlist in builder.permuteFeatures(uids = (uid,base)):
                        ftml.setFeatures(featlist)
                        builder.render((base,uid), ftml, keyUID = uid, addBreaks = False)
                        if uid != 0x0651: # if not shadda
                            # include shadda, in either order:
                            builder.render((base, uid, 0x0651), ftml, keyUID=uid, addBreaks=False)
                            builder.render((base, 0x0651, uid), ftml, keyUID=uid, addBreaks=False)
                        if diac != 0x0670:  # If not superscript alef
                            # include superscript alef, in either order:
                            builder.render((uid, diac, 0x0670), ftml, addBreaks=False)
                            builder.render((uid, 0x0670, diac), ftml, addBreaks=False)
                    ftml.clearFeatures()
                ftml.closeTest()

        ftml.startTestGroup('Special cases')
        builder.render((0x064A, 0x065E), ftml)   # Yeh + Fatha should keep dots
        builder.render((0x064A, 0x0654), ftml)   # Yeh + Hamza should loose dots
        ftml.closeTest()

        ftml.startTestGroup('LamAlef ligatures')
        diaB = 0x064D
        diaA = 0x064B
        for lam in lamlist:
            for alef in aleflist:
                for featlist in builder.permuteFeatures(uids=(lam,alef)):
                    ftml.setFeatures(featlist)
                    builder.render((lam, alef),             ftml, addBreaks=False)
                    builder.render((lam, diaA, alef, diaA), ftml, addBreaks=False)
                    builder.render((lam, diaB, alef),       ftml, addBreaks=False)
                    builder.render((lam, alef, diaB),       ftml, addBreaks=False)
                    builder.render((lam, diaB, alef, diaB), ftml, addBreaks=False)
                    ftml.clearFeatures()
                ftml.closeTest()

    if test.lower().startswith("subtending"):
        # Generates sample data for all subtending marks. Data includes sequences of 0 to n+1
        # digits, where n is the maximum expected to be supported on the mark. Latin, Arbic-Indic,
        # and Extended Arabic-Indic digits are included.
        for digitSample in filter(lambda x: x in builder.uids(), (0x0032, 0x0668, 0x06F8)):
            digitOne = (digitSample & 0xFFF0) + 1
            for uid,lgt in filter(lambda x: x[0] in builder.uids(), ([0x600,3], [0x0601,4], [0x0602,2], [0x0603,4], [0x0604,4], [0x0605,4], [0x06DD,3])):
                c = unichr(uid)
                label = "U+{0:04X}".format(uid)
                comment = builder.char(uid).basename
                for featlist in builder.permuteFeatures(uids=(uid,)):
                    ftml.setFeatures(featlist)
                    ftml.addToTest(uid, "\u0628" + c + "\u0645", label, comment)
                    for ln in range(1,lgt+1):
                        ftml.addToTest(uid, c + unichr(digitSample)*ln)
                    ftml.addToTest(uid, c + unichr(digitOne) + unichr(digitOne+1))
                ftml.clearFeatures()
                ftml.closeTest()

                if uid == 0x06DD and digitOne == 0x06F1:
                    # Extra items for Eastern digits
                    for featlist in builder.permuteFeatures(uids=(uid, 0x06F7)):
                        ftml.setFeatures(featlist)
                        ftml.addToTest(uid, c + "\u06F4\u06F6\u06F7", label, "4 6 7")
                    ftml.clearFeatures()
                    for langID in sorted(builder.char(0x06F7).langs):
                        ftml.setLang(langID)
                        ftml.addToTest(uid, c + "\u06F4\u06F6\u06F7", label, "4 6 7")
                    ftml.clearLang()
                    ftml.closeTest()

    if test.lower().startswith("showinv"):
        # Sample data for chars that have a "show invisible" feature
        invlist = filter(lambda x: x in builder.uids(), (0x061C, 0x200C, 0x200D, 0x200E, 0x200F, 0x202A, 0x202B, 0x202C, 0x202D, 0x202E, 0x2066, 0x2067, 0x2068, 0x2069,
                                                         0xFE00, 0xFE01, 0xFE02, 0xFE03, 0xFE04, 0xFE05, 0xFE06, 0xFE07, 0xFE08, 0xFE09, 0xFE0A, 0xFE0B, 0xFE0C, 0xFE0D, 0xFE0E, 0xFE0F))
        for uid in invlist:
            c = unichr(uid)
            label = "U+{0:04X}".format(uid)
            comment = builder.char(uid).basename
            for featlist in builder.permuteFeatures(uids=(uid,)):
                ftml.setFeatures(featlist)
                ftml.addToTest(uid, "\u0628" + c + "\u0645", label, comment)
            ftml.clearFeatures()
            ftml.closeTest()

    if test.lower().startswith("daggeralef"):
        for uid in sorted(builder.uids(), cmp=lambda l,r: cmp(builder.char(l).icuJG, builder.char(r).icuJG) or cmp(l,r)):
            if builder.char(uid).icuJG not in (33,35,45):
                # If not Yeh, Sad or seen joining group we're not interested
                continue
            for featlist in builder.permuteFeatures(uids=(uid, 0x0670)):
                ftml.setFeatures(featlist)
                builder.render((uid, 0x0670), ftml)
            ftml.clearFeatures()
            ftml.closeTest()

    ftml.writeFile(args.output)


def cmd() : execute("UFO",doit,argspec)
if __name__ == "__main__": cmd()
