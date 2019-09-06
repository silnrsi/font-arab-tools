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
    ('--langs',{'help':'List of bcp47 language tags', 'default': None}, {}),
    ('--rtl', {'help': 'enable right-to-left features', 'action': 'store_true'}, {}),
    ('-t', '--test', {'help': 'which test to build', 'default': None}, {}),
    ('-s','--fontsrc',{'help': 'default font source', 'action': 'append'}, {}),
    ('--scale', {'help': '% to scale rendered text'}, {}),
    ('--ap', {'help': 'regular expression describing APs to examine', 'default': '.'}, {}),
    ('--xsl', {'help': 'XSL stylesheet to use'}, {}),
]

# The following should be exposed by PyICU, but does not seem to be implemented.

# UJoiningType
NON_JOINING = 0
JOIN_CAUSING = 1
DUAL_JOINING = 2
LEFT_JOINING = 3
RIGHT_JOINING = 4
TRANSPARENT = 5

# UJoiningGroup
NO_JOINING_GROUP = 0
AIN = 1
ALAPH = 2
ALEF = 3
BEH = 4
BETH = 5
DAL = 6
DALATH_RISH = 7
E = 8
FEH = 9
FINAL_SEMKATH = 10
GAF = 11
GAMAL = 12
HAH = 13
TEH_MARBUTA_GOAL = 14
HAMZA_ON_HEH_GOAL = TEH_MARBUTA_GOAL
HE = 15
HEH = 16
HEH_GOAL = 17
HETH = 18
KAF = 19
KAPH = 20
KNOTTED_HEH = 21
LAM = 22
LAMADH = 23
MEEM = 24
MIM = 25
NOON = 26
NUN = 27
PE = 28
QAF = 29
QAPH = 30
REH = 31
REVERSED_PE = 32
SAD = 33
SADHE = 34
SEEN = 35
SEMKATH = 36
SHIN = 37
SWASH_KAF = 38
SYRIAC_WAW = 39
TAH = 40
TAW = 41
TEH_MARBUTA = 42
TETH = 43
WAW = 44
YEH = 45
YEH_BARREE = 46
YEH_WITH_TAIL = 47
YUDH = 48
YUDH_HE = 49
ZAIN = 50
FE =  51
KHAPH = 52
ZHAIN = 53
BURUSHASKI_YEH_BARREE = 54
FARSI_YEH = 55
NYA =  56
ROHINGYA_YEH = 57
MANICHAEAN_ALEPH = 58
MANICHAEAN_AYIN = 59
MANICHAEAN_BETH = 60
MANICHAEAN_DALETH = 61
MANICHAEAN_DHAMEDH = 62
MANICHAEAN_FIVE = 63
MANICHAEAN_GIMEL = 64
MANICHAEAN_HETH = 65
MANICHAEAN_HUNDRED = 66
MANICHAEAN_KAPH = 67
MANICHAEAN_LAMEDH = 68
MANICHAEAN_MEM = 69
MANICHAEAN_NUN = 70
MANICHAEAN_ONE = 71
MANICHAEAN_PE = 72
MANICHAEAN_QOPH = 73
MANICHAEAN_RESH = 74
MANICHAEAN_SADHE = 75
MANICHAEAN_SAMEKH = 76
MANICHAEAN_TAW = 77
MANICHAEAN_TEN = 78
MANICHAEAN_TETH = 79
MANICHAEAN_THAMEDH = 80
MANICHAEAN_TWENTY = 81
MANICHAEAN_WAW = 82
MANICHAEAN_YODH = 83
MANICHAEAN_ZAYIN = 84
STRAIGHT_WAW = 85
AFRICAN_FEH = 86
AFRICAN_NOON = 87
AFRICAN_QAF = 88
MALAYALAM_BHA = 89
MALAYALAM_JA = 90
MALAYALAM_LLA = 91
MALAYALAM_LLLA = 92
MALAYALAM_NGA = 93
MALAYALAM_NNA = 94
MALAYALAM_NNNA = 95
MALAYALAM_NYA = 96
MALAYALAM_RA = 97
MALAYALAM_SSA = 98
MALAYALAM_TTA = 99
HANIFI_ROHINGYA_KINNA_YA = 100
HANIFI_ROHINGYA_P = 101


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
            if c.general == GC.OTHER_LETTER or c.isBase:
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
            if c.general == GC.NON_SPACING_MARK:
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
                c = unichr(uid)
                label = "U+{0:04X} {1}".format(uid, 'latn' if digitOne == 0x0031 else 'arab' if digitOne == 0x0661 else 'urdu')
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
            c = unichr(uid)
            label = 'U+{0:04X} ({1})'.format(uid, inv[1])
            comment = builder.char(uid).basename if uid in builder.uids() else ""
            ftml.addToTest(uid, " " + c + " ", label, comment)
            ftml.closeTest()
        ftml.clearFeatures()

    if test.lower().startswith('daggeralef'):
        for uid in sorted(builder.uids(), cmp=lambda l,r: cmp(builder.char(l).icuJG, builder.char(r).icuJG) or cmp(l,r)):
            if builder.char(uid).icuJG not in (SAD, SEEN, YEH):
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
