#!/usr/bin/env python
'generate ftml tests from glyph_data.csv and UFO'
__url__ = 'http://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2018 SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Bob Hallissy'

import re
from silfont.core import execute
import silfont.ftml_builder as FB
from palaso.unicode.ucd import get_ucd

argspec = [
    ('ifont',{'help': 'Input UFO'}, {'type': 'infont'}),
    ('output',{'help': 'Output file ftml in XML format', 'nargs': '?'}, {'type': 'outfile', 'def': '_out.ftml'}),
    ('-i','--input',{'help': 'Glyph info csv file'}, {'type': 'incsv', 'def': 'glyph_data.csv'}),
    ('-f','--fontcode',{'help': 'letter to filter for glyph_data'},{}),
    ('-l','--log',{'help': 'Set log file name'}, {'type': 'outfile', 'def': '_ftml.log'}),
    ('--langs',{'help':'List of bcp47 language tags', 'default': None}, {}),
    ('--rtl', {'help': 'enable right-to-left features', 'action': 'store_true'}, {}),
    ('-t', '--test', {'help': 'which test to build', 'default': None}, {}),
    ('-s','--fontsrc',{'help': 'default font source', 'action': 'append'}, {}),
    ('--scale', {'help': '% to scale rendered text'}, {}),
    ('--ap', {'help': 'regular expression describing APs to examine', 'default': '.'}, {}),
    ('--xsl', {'help': 'XSL stylesheet to use'}, {}),
]


joinGroupKeys = {
    'Ain' : 1,
    'Alef' : 2,
    'Beh' : 3,
    'Yeh' : 4, 'Farsi_Yeh' :4 , # Near Beh Due To Medial Form
    'Noon' :5, 'African_Noon' : 5,  # Near Yeh Due To Medial Form
    'Nya' : 6,  # Near Noon Due To Final Form
    'Sad' : 7,  # Near Noon Due To Final Form
    'Seen' : 8,
    'Yeh_With_Tail' : 9,
    'Rohingya_Yeh' : 10,
    'Yeh_Barree' : 11, 'Burushaski_Yeh_Barree' : 11,
    'Dal' : 12,
    'Feh' : 13, 'African_Feh' : 13,
    'Gaf' : 14, 'Kaf' : 14,
    'Swash_Kaf' :15 ,
    'Hah' : 16,
    'Heh' : 17,
    'Heh_Goal' : 18,
    'Teh_Marbuta' : 19, 'Teh_Marbuta_Goal' : 19,
    'Knotted_Heh' :20,
    'Lam' : 21,
    'Meem' : 22,
    'Qaf' : 23, 'African_Qaf' : 23,
    'Reh' :24 ,
    'Tah' : 26,
    'Waw' : 27,
    'Straight_Waw' : 28,
}

def joinGoupSortKey(uid:int):
    return joinGroupKeys.get(get_ucd(uid, 'jg'), 99) * 65536 + uid

def doit(args):
    logger = args.logger

    # Read input csv
    builder = FB.FTMLBuilder(logger, incsv = args.input, fontcode = args.fontcode, font = args.ifont, ap = args.ap,
                             rtlenable = True, langs = args.langs)

    # Override default base (25CC) for displaying combining marks
    builder.diacBase = 0x0628   # beh

    # Initialize FTML document:
    test = args.test or "AllChars (NG)"  # Default to AllChars
    ftml = FB.FTML(test, logger, rendercheck = True, fontscale = args.scale, xslfn = args.xsl, fontsrc = args.fontsrc,
                   defaultrtl = args.rtl)

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
            if len(c.langs):
                for langID in builder.allLangs:
                    ftml.setLang(langID)
                    builder.render((uid,), ftml)
                ftml.clearLang()

        # Add specials and ligatures that were in the glyph_data:
        ftml.startTestGroup('Specials & ligatures from glyph_data')
        for basename in sorted(builder.specials()):
            special = builder.special(basename)
            for featlist in builder.permuteFeatures(uids = special.uids, feats = special.feats):
                ftml.setFeatures(featlist)
                builder.render(special.uids, ftml)
                ftml.closeTest()
            ftml.clearFeatures()
            if len(special.langs):
                for langID in builder.allLangs:
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
                if lam == 0x0644:
                    # Also test lam with hamza above for warsh variants
                    for featlist in builder.permuteFeatures(uids=(lam, 0x0654, alef),feats=('cv02',)):
                        ftml.setFeatures(featlist)
                        builder.render((lam, 0x0654, alef), ftml)
                        ftml.closeTest()
                    ftml.clearFeatures()

        # Add Allah data manually
        ftml.startTestGroup('Allah ligatures')
        ftml.addToTest(None, "\uFDF2 \u0627\u0644\u0644\u200C \uFDF2 ", label="Rule 1")
        ftml.closeTest()
        ftml.addToTest(None, "\u0627\u0644\u0644\u0651\u0670\u0647", label = "Rule 2 (daggeralef)")
        ftml.addToTest(None, "\u0627\u0644\u0644\u0670\u0651\u0647")
        ftml.addToTest(None, "\u0627\u0644\u0644\u0651\u0670\u06C1")
        ftml.addToTest(None, "\u0627\u0644\u0644\u0670\u0651\u06C1")
        ftml.closeTest()
        ftml.addToTest(None, "\u0627\u0644\u0644\u0651\u064E\u0647", label = "Rule 2 (fatha)")
        ftml.addToTest(None, "\u0627\u0644\u0644\u064E\u0651\u0647")
        ftml.addToTest(None, "\u0627\u0644\u0644\u0651\u064E\u06C1")
        ftml.addToTest(None, "\u0627\u0644\u0644\u064E\u0651\u06C1")
        ftml.closeTest()
        ftml.addToTest(None, " \u0644\u0644\u0651\u064E\u0647", label = "Rule 2d")
        ftml.addToTest(None, "\u0641\u0627\u0644\u0644\u064E\u0651\u06C1")
        ftml.addToTest(None, "\u0641\u06EB\u0627\u0644\u0644\u064E\u0651\u06C1")
        ftml.closeTest()
        ftml.addToTest(None, "\u0627\u0644\u0644\u0647", label="Rule 3")
        ftml.addToTest(None, "\u0622\u0644\u0644\u0647")
        ftml.addToTest(None, "\u0623\u0644\u0644\u0647")
        ftml.addToTest(None, "\u0671\u0644\u0644\u0647")
        ftml.addToTest(None, "\u0627\u06EB\u0644\u0644\u0647")
        ftml.addToTest(None, "\u0641\u0627\u0644\u0644\u0647")
        ftml.addToTest(None, "\u0641\u0644\u0644\u0647")
        ftml.closeTest()
        ftml.addToTest(None, "\u0627\u0644\u200D\u0644\u0651\u0670\u0647", label="Rule 4a")
        ftml.closeTest()

    if test.lower().startswith("diac"):
        # Diac attachment:

        doLongTest = 'short' not in test.lower()

        # Representative base and diac chars:
        if doLongTest:
            repDiac = filter(lambda x: x in builder.uids(), (0x064E, 0x0650, 0x065E, 0x0670, 0x0616, 0x06E3, 0x08F0, 0x08F2))
            repBase = filter(lambda x: x in builder.uids(), (0x0627, 0x0628, 0x062B, 0x0647, 0x064A, 0x77F, 0x08AC))
            lamlist = filter(lambda x: x in builder.uids(), (0x0644, 0x06B5, 0x06B6, 0x06B7, 0x06B8, 0x076A, 0x08A6))
            aleflist = filter(lambda x: x in builder.uids(), (0x0627, 0x0622, 0x0623, 0x0625, 0x0671, 0x0672, 0x0673, 0x0675, 0x0773, 0x0774))
        else:
            repDiac = filter(lambda x: x in builder.uids(), (0x064E, 0x0650, 0x0670))
            repBase = filter(lambda x: x in builder.uids(), (0x0627, 0x0628))
            lamlist = filter(lambda x: x in builder.uids(), (0x0644, 0x06B5, 0x06B6, 0x06B7, 0x06B8, 0x076A, 0x08A6))
            aleflist = filter(lambda x: x in builder.uids(), (0x0627, 0x0622, 0x0623, 0x0625, 0x0671, 0x0672, 0x0673, 0x0675, 0x0773, 0x0774))

        ftml.startTestGroup('Representative diacritics on all bases that take diacritics')
        for uid in sorted(builder.uids()):
            if uid < 32 or uid in (0xAA, 0xBA): continue
            c = builder.char(uid)
            # Always process Lo, but others only if that take marks:
            if c.general == 'Lo' or c.isBase:
                for diac in repDiac:
                    for featlist in builder.permuteFeatures(uids = (uid,diac)):
                        ftml.setFeatures(featlist)
                        builder.render((uid,diac), ftml, addBreaks = True)
                        if doLongTest:
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
            if c.general == 'Mn':
                for base in repBase:
                    for featlist in builder.permuteFeatures(uids = (uid,base)):
                        ftml.setFeatures(featlist)
                        builder.render((base,uid), ftml, keyUID = uid, addBreaks = False)
                        if doLongTest:
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
                c = chr(uid)
                label = "U+{0:04X} {1}".format(uid, 'latn' if digitOne == 0x0031 else 'arab' if digitOne == 0x0661 else 'urdu')
                comment = builder.char(uid).basename
                for featlist in builder.permuteFeatures(uids=(uid,)):
                    ftml.setFeatures(featlist)
                    ftml.addToTest(uid, "\u0628" + c + "\u0645", label, comment)
                    for ln in range(1,lgt+1):
                        ftml.addToTest(uid, c + chr(digitSample)*ln)
                    ftml.addToTest(uid, c + chr(digitOne) + chr(digitOne+1))
                ftml.clearFeatures()
                ftml.closeTest()

                if uid == 0x06DD and digitOne == 0x06F1:
                    # Extra items for Eastern digits
                    for featlist in builder.permuteFeatures(uids=(uid, 0x06F7)):
                        ftml.setFeatures(featlist)
                        ftml.addToTest(uid, c + "\u06F4\u06F6\u06F7", label, "4 6 7")
                    ftml.clearFeatures()
                    for langID in builder.allLangs:
                        ftml.setLang(langID)
                        ftml.addToTest(uid, c + "\u06F4\u06F6\u06F7", label, "4 6 7")
                    ftml.clearLang()
                    ftml.closeTest()

    if test.lower().startswith("showinv"):
        # Sample data for chars that have a "show invisible" feature
        # The 'r', 'a', 'ra' indicates whether this is standard in Roman fonts, Arabic fonts, or both.
        invlist = [
            (0x034F, 'r' ), (0x061C, 'a' ), (0x200B, 'r' ), (0x200C, 'ra'), (0x200D, 'ra'), (0x200E, 'ra'),
            (0x200F, 'ra'), (0x202A, 'ra'), (0x202B, 'ra'), (0x202C, 'ra'), (0x202D, 'ra'), (0x202E, 'ra'),
            (0x202E, 'r' ), (0x2060, 'r' ), (0x2061, 'r' ), (0x2062, 'r' ), (0x2063, 'r' ), (0x2066, 'a' ),
            (0x2067, 'a' ), (0x2068, 'a' ), (0x2069, 'a' ), (0xFE00, 'ra'), (0xFE01, 'ra'), (0xFE02, 'ra'),
            (0xFE03, 'ra'), (0xFE04, 'ra'), (0xFE05, 'ra'), (0xFE06, 'ra'), (0xFE07, 'ra'), (0xFE08, 'ra'),
            (0xFE09, 'ra'), (0xFE0A, 'ra'), (0xFE0B, 'ra'), (0xFE0C, 'ra'), (0xFE0D, 'ra'), (0xFE0E, 'ra'),
            (0xFE0F, 'ra')
        ]
        featlist = (('invs', '1'), ('ss06', '1'))
        ftml.setFeatures(featlist)
        for inv in invlist:
            uid = inv[0]
            c = chr(uid)
            label = 'U+{0:04X} ({1})'.format(uid, inv[1])
            comment = builder.char(uid).basename if uid in builder.uids() else ""
            ftml.addToTest(uid, " " + c + " ", label, comment)
            ftml.closeTest()
        ftml.clearFeatures()

    if test.lower().startswith('daggeralef'):
        for uid in sorted(builder.uids(), key=joinGoupSortKey):
            if get_ucd(uid,'jg') not in ('Sad', 'Seen', 'Yeh'):
                # If not Yeh, Sad or seen joining group we're not interested
                continue
            for featlist in builder.permuteFeatures(uids=(uid, 0x0670)):
                ftml.setFeatures(featlist)
                builder.render((uid, 0x0670), ftml)
            ftml.clearFeatures()
            ftml.closeTest()

    if test.lower().startswith('kern'):
        rehs = sorted(filter(lambda uid: get_ucd(uid,'jg') == 'Reh', builder.uids() ))
        waws = sorted(filter(lambda uid: get_ucd(uid,'jg') == 'Waw', builder.uids()))
        uids = filter(lambda uid: get_ucd(uid, 'jt') in ('D', 'R') or uid == 0xFD3E, builder.uids())
        # NB: I wondered about including punctuation, i.e.,  get_ucd(uid, 'gc').startswith('P'), but the default
        #     spacing is pretty good and graphite collision avoidance makes it worse, so the only one we need is FDFE
        uids = sorted(uids, key=joinGoupSortKey)
        #
        dbehf = chr(0x066E) + chr(0x200D)  # dotless beh final
        alef = chr(0x0627)   # alef
        zwj  = chr(0x200D)   # Zero width joiner

        ftml.startTestGroup('All the rehs')
        for uid in rehs:
                c = chr(uid)
            label = 'U+{0:04X}'.format(uid)
            comment = builder.char(uid).basename
            for featlist in builder.permuteFeatures(uids=(uid,)):
                ftml.setFeatures(featlist)
                ftml.addToTest(uid, c + dbehf + ' ' + zwj + c + dbehf, label, comment)
            ftml.clearFeatures()
            ftml.closeTest()

        ftml.startTestGroup('All the waws')
        for uid in waws:
                c = chr(uid)
            label = 'U+{0:04X}'.format(uid)
            comment = builder.char(uid).basename
            for featlist in builder.permuteFeatures(uids=(uid,)):
                ftml.setFeatures(featlist)
                ftml.addToTest(uid, c + dbehf + ' ' + zwj + c + dbehf, label, comment)
            ftml.clearFeatures()
            ftml.closeTest()

        # reh or waw plus the others
        for uid1 in (0x631, 0x648):  # (reh, waw)
                ftml.startTestGroup('{} + all the others'.format(get_ucd(uid1, 'jg')))
                c1 = chr(uid1)
            for uid2 in uids:
                    c2 = chr(uid2)
                comment = builder.char(uid2).basename
                label = 'U+{:04X}'.format(uid2)
                for featlist in builder.permuteFeatures(uids=(uid1,uid2)):
                    ftml.setFeatures(featlist)
                        if get_ucd(uid2, 'jt') == 'D':
                        ftml.addToTest(uid2, zwj + c1 + c2 + zwj, label, comment)
                        ftml.addToTest(uid2,       c1 + c2 + zwj)
                    ftml.addToTest(    uid2, zwj + c1 + c2      , label, comment)
                    ftml.addToTest(    uid2,       c1 + c2      )
                ftml.clearFeatures()
                ftml.closeTest()

    ftml.writeFile(args.output)


def cmd() : execute("UFO",doit,argspec)
if __name__ == "__main__": cmd()
