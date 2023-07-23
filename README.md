# font-arab-tools
Tools and data shared by a number of Arabic script font projects


## How to use absgenftml

While the program can generate a number of different ftml test documents, each run of absgenftml creates one FTML file. The particular content included is determined by the `-t` option, and the name of the output file is provided on the command line.

Excerpts from running `absgenftml --help`, with comments:

```
usage: absgenftml [-h] [-i INPUT] [--langs LANGS]
                  [--rtl] [--norendercheck] [-t TEST] [-s FONTSRC]
                  [--scale SCALE] [--ap AP] [--xsl XSL] 
                  ifont [output]

generate ftml tests from glyph_data.csv and UFO

positional arguments:
  ifont                 Input UFO
  output                Output file ftml in XML format

other arguments:
  -i INPUT, --input INPUT
                        Glyph info csv file
```
The glyph info csv should have at least the following column headers:

- `glyph_name`  The working glyph name
- `USV`         The Unicode codepoint(s) in hex

For a given glyph, if the USV field can be:
- a single codepoint, indicating the glyph represents an encoded character.  
- a comma-separated list of codepoints, indicating the glyph is an unencoded ligature.
- blank, indicating the glyph is unencoded and not a ligature

If you want to test languages or features, then for unencoded glyphs, the include:

- `bcp47tags`   Comma-separated list of languages that should show this glyph, for example: `sd,ur,rhg`
- `Feat`        semicolon-separarated list of feat=val-set pairs that should show this glyph, for example: `cv82=1,2;ss01=1`

These fields are what enable absgenftml to determine what characters are impacted by what features and languages, and to then iterate over feature and language combinations for characters that need it.

```
  --langs LANGS         List of bcp47 language tags
```
If not supplied, then for any given character, the program iterates over the languages specified in the `bcp47tags` column of all variant glyphs _for that character_.  If `--langs` is specified, it should be a comma-speparated list of bcp47tags and then, for any character that has language-specific variants of any kind, program iterates over all the languages named in the `-langs`.

```
  --norendercheck       do not include the RenderingUnknown check

  -t TEST, --test TEST  name of the test to generate
```
This determines what ftml test is generated. Whatever you supply here will be the title of the FTML document, and then the first few letters of it will be compared (case insensitive) with the following to determine the test:
- `allchars` - all encoded characters, ligatures, lam-alef sequences, and allah sequences.
- `diac` - Is actually two tests depending on whether `short` also appears in the test name. The test displays representative diacritics on all bases that take them, and then all diacritics on representative bases. For the long test, also emits the base+diac string with an added shadda (in both possible mark orders) and also with an added hamza above (in both possible mark orders). Additionally it emits some special cases, including yeh+fatha (should lose dots) and yeh+hamza (should keep dots), and also all lam-alef combinations with some marks.
- `subtending` - tests all the subtending marks in the font with all 3 digit groups (latin, arabic-indic, and extended-arabic-indic).
- `daggeralef` - shows positioning (and if available, size variants) of dagger-alef on all sad-, seen- and yeh-like characters.


```
  -s FONTSRC, --fontsrc FONTSRC
                        default font source
```
Multiple -s parameters may be supplied, and each may use `local()` or `url()` notation. If `url()` notation is used, the path must be relative to the folder containing the ftml file.

```
  --scale SCALE         percentage to scale rendered text (default 100)

  --ap AP               regular expression describing APs to examine
```
The program examines AP names to determine which encoded glyphs are base characters (thus take diacritics) and which are marks. Typically only some AP names are used for mark positioning. To specify exactly which ones, the -ap parameter takes a regex to indicate which APs to examine. For example `--ap "_?dia[AB]$"` will examine just `_diaA`, `_diaB`, `diaA`, and `diaB`.

```
  --xsl XSL             XSL stylesheet to use
```
This needs to be the relative path from the folder containing the ftml document to the XSL file to use for viewing the document in a browser.

Example:

To generate allchars test in Harmattan:
```
cd source
absgenftml.py -t "AllChars (NG)" --ap "_?dia[AB]$" --xsl ../tools/ftml.xsl --scale 200 -i glyph_data.csv  -s url(../results/Harmattan-Regular.ttf)  -s url(../results/Harmattan-Bold.ttf) Harmattan-Regular.ufo ..\tests\AllChars-ng.ftml
```
