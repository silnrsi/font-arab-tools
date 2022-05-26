#!/usr/bin/python3
"""generate project-specific subset of absGlyphData.csv"""

import csv
import sys
import argparse
import re

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='generate project-specific subset of absGlyphList.csv',
    epilog='''
For example, to generate the glyph_data.csv file for Scheherazade, use:

   cd font-arab-tools/absGlyphList
   %(prog)s -f s

By default it reads (absGlyphList.csv) and writes (glyph_data.csv) in the current directory. 
Alternate files/locations can provided on the commandline:

    %(prog)s -f s -i somedir/absGlyphList.csv  otherdir/output.csv
''')

parser.add_argument('-i', '--incsv', help='Input csv file, default: absGlyphList.csv', default='absGlyphList.csv')
parser.add_argument('outcsv', help='Output csv file, default: glyph_data.csv', nargs='?', default='glyph_data.csv')
parser.add_argument('-f', '--fontID', help='letter identifying font', type=str, required=True)
parser.add_argument('--noBcp47', help='omit bcp47 column', action='store_true')
parser.add_argument('--noFeat', help='omit Feat column', action='store_true')
args = parser.parse_args()

fields = ['glyph_name', 'ps_name', 'USV', 'DesignerOrder']
if not args.noBcp47: fields.append('bcp47tags')
if not args.noFeat:  fields.append('Feat')

def eprint(*args, **kwargs):
    """like print but to stderr"""
    print(*args, file=sys.stderr, **kwargs)

if len(args.fontID) != 1:
    eprint('fontID argument must be a single letter identifying the font project desired')
    sys.exit(2)

fontRE = re.compile(r'\*|' + args.fontID, re.IGNORECASE)

with open(args.incsv, newline='') as infile:
    reader = csv.DictReader(infile)
    missingFields = list(filter(lambda x: x not in reader.fieldnames, fields + ['fonts',]))
    if len(missingFields):
        eprint('Fields missing from input csv: ', ','.join(missingFields))
        sys.exit(2)

    with open(args.outcsv, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fields)
        for row in reader:
            if fontRE.search(row['fonts']):
                writer.writerow([row[x] for x in fields])
