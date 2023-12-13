#!/usr/bin/env python3
__doc__ = '''for all UFOs in current folder, construct all desired lam-alef ligatures, being careful to preserve
anchors diaA, diaB, diaB2 and alef from the components.
For example, construct lam_alef-ar.fina from lam-ar.medi.preAlef and alef-ar.fina.postLamMed
'''
__url__ = 'https://github.com/silnrsi/font-arab-tools'
__copyright__ = 'Copyright (c) 2021-2024 SIL International  (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'Bob Hallissy'

from fontParts.world import OpenFont
from glob import glob
from silfont.core import execute
import silfont.ftml_builder as FB
from palaso.unicode.ucd import get_ucd
from silfont.ftml_builder import FTMLBuilder

argspec = [
    ('-i', '--incsv', {'help': 'Input csv file, default: glyph_data.csv'}, {'type': 'incsv', 'def': 'glyph_data.csv'}),
    ('-l','--log',{'help': 'Log file'}, {'type': 'outfile', 'def': '_mkLamAlef.log'}),
    ('--prefix', {'help': 'prefix string for lam-alef component glyphs, default = "_"', 'default': '_'}, {}),
    ('--dryrun', {'help': 'dry-run (don\'t actually create any ligatures', 'action': 'store_true'}, {}),
    ('UFOs', {'help': 'one or more UFO fonts', 'nargs': '+'}, {})
]

def doit(args):
    logger = args.logger

    # Read the input csv file
    builder = FB.FTMLBuilder(logger, incsv=args.incsv)

    # Find all lam-alef ligatures in the glyph_data -- these are the ones we want to make/update:
    ligs2make = []
    for spcName in builder.specials():
        s = builder.special(spcName)
        if len(s.uids) != 2:
            continue
        (uid1, uid2) = s.uids
        if get_ucd(uid1,'jg') != 'Lam' or get_ucd(uid2,'jg') != 'Alef':
            continue
        # Found one!
        ligs2make.append(s)
    if len(ligs2make) == 0:
        logger.log(f'"{args.incsv}" mentions no lam-alef ligatures', 'S')


    def getAnchor(g, a):
        """ g = glyph object
            a = name of anchor to retrieve
        """
        for ac in g.anchors:
            if ac.name == a:
                return (ac.x, ac.y)
        raise KeyError  # No anchor by that name... raise error.

    def addComponent(g, c, x, y,n):
        """ g = glyph object getting new component
            c = component glyph name
            x = x offset for next component in g
            n = ligature component index (1, 2, ...)
        """
        g.appendComponent(c, offset=(x, y))
        for ac in g.layer[c].anchors:  # existing anchor in the component
            if ac.name in ('diaA', 'diaB', 'dia2B' 'alef'):
                g.appendAnchor(f'{ac.name}_{n}', (ac.x + x, ac.y))  # new anchor in ligature

    # Process all UFOs on commandline, allowing wildcards
    ufoCount = 0
    for ufos in args.UFOs:
        for ufo in glob(ufos):
            try:
                font = OpenFont(ufo, showInterface=False)
                fontname = font.info.familyName
                stylename = font.info.styleName
            except:
                logger.log(f'unable to open "{ufo}" -- bypassing', 'W')
                continue
            logger.log(f'{"dry-running" if args.dryrun else "processing"} "{ufo}" = {fontname} {stylename}', 'P')
            ufoCount += 1

            # Keep track of glyphs added or modified:
            countAdded = 0
            countModified = 0

            # We're only going to process the default layer
            layer = font.defaultLayer

            missingUids = set()  # Used so we only generate one "glyph wanted" warning message per missing lam or alef.
            lamAlefClasses = {} # indexed by final alefs in ligatures; value is tuple of (lam, lam-alef-ligature)
            for lig in ligs2make:
                basenames = []
                for uid in lig.uids:
                    try:
                        basename = builder.char(uid).basename
                    except KeyError:
                        if uid not in missingUids:
                            logger.log(f'cannot find glyph encoded at U+{uid:04x} needed for {lig.basename}', 'W')
                            missingUids.add(uid)
                        continue
                    basenames.append(basename)
                # Both the uids are in the glyphlist, so we can get their names minus the '-ar':
                (lam, alef) = [ x[:-3] for x in basenames]

                if False:  # lig.uids[1] in (0x0623, 0x0624):
                    # Need to build Warsh ("touching") variants also:
                    langexts = ('', '.warsh')
                else:
                    langexts = ('',)

                for langext in langexts:
                    # Ok, try to build isolate and final ligature glyphs for one pair:
                    for ext in ('', '.fina'):
                        gname = f'{lam}_{alef}-ar{ext}{langext}'
                        # logger.log(f'considering {gname} ...', 'I')

                        # calculate name of components needed
                        if ext == '.fina':
                            l = f'{args.prefix}{lam}-ar.medi.preAlef'
                            a = f'{args.prefix}{alef}-ar.fina.postLamMed{langext}'
                        else:
                            l = f'{args.prefix}{lam}-ar.init.preAlef'
                            a = f'{args.prefix}{alef}-ar.fina.postLamIni{langext}'

                        # Verify needed components are in the UFO, and retrieve width
                        try:
                            lw = int(layer[l].width)  #lam component width
                        except:
                            logger.log(f'component glyph {l} not in UFO -- ligature {gname} not made', 'W')
                            continue
                        try:
                            aw = int(layer[a].width)  # alef component width
                        except:
                            logger.log(f'component glyph {a} not in UFO -- ligature {gname} not made', 'W')
                            continue

                        # Finally it should be safe to create the new ligature glyph
                        if gname in layer:
                            logger.log(f'replacing {gname}', 'I')
                            countModified += 1
                        else:
                            logger.log(f'adding {gname}', 'I')
                            countAdded += 1
                        # Find lam component's exit anchor and alef component's entry anchor
                        # with default values of origin and width, respectively.
                        (lx, ly) = next(( (ac.x, ac.y) for ac in layer[l].anchors if ac.name == 'exit'), (0, 0))
                        (ax, ay) = next(( (ac.x, ac.y) for ac in layer[a].anchors if ac.name == 'entry'), (aw, 0))

                        if not args.dryrun:
                            g = layer.newGlyph(gname, clear=True)
                            addComponent(g, l, ax-lx, 0, 1)
                            addComponent(g, a, 0, ly-ay, 2)
                            g.width = ax + (lw - lx)

                        # Remember info to generate lam-alef lookup classes:
                        lamAlefClasses.setdefault(basenames[1], []).append((basenames[0], gname))

            logger.log(f'{countAdded} glyphs added; {countModified} glyphs modified.', 'P')

            font.close(save=False if args.dryrun else True)

        logger.log(f'{ufoCount} UFO fonts processed', 'P')

def cmd() : execute(None,doit,argspec)
if __name__ == "__main__": cmd()