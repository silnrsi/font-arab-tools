Copyright (c) 2018-2024, SIL Global (https://www.sil.org).
Released under the MIT license -- see [LICENSE](../LICENSE).

This folder contains reference material common to most of SIL's Arabic script
font projects.

## `absGlyphList.xlsx`

This file is the master glyph list for all the projects except Awami.
As such:
- It represent the union of all the font projects and is thus a superset of any
  individual font.
- It has two columns of glyph names since we have two naming conventions in
  current use as we transition from the old style "abs" names (e.g.,
  `absBehIni`) to the new GlyphsApp-compatible style (`beh-ar.init`).
- It has multiple records for some glyphs where a name change has occurred;
  the `Fonts` column indicates which name is currently used in which projects.
  (For example `absBehThreeDotsUpwardBelow` was renamed to the shorter to
  `absBehThreeDotsUpBelow` starting with Harmattan, but other projects 
  picked up this shorter name going forward)
- It contains data for legacy glyphs that we no longer need or use.

As a result of the above, the absGlyphList is not directly usable for any
of the font projects, but instead individual projects will need to excerpt
the file for their use.

An additional implication of the above is that the column headers do not --
indeed cannot -- conform exactly to WSTech conventions (because, for example,
those conventions allow only one `glyph_name` column).

### `absGlyphList.csv`

This is a comma-separated value text file that is equivalent to
the master `abGlyphList.xlsx`. Whenever the .xlsx file is updated, the
.csv file should be also be updated (by using "Save As...")

Notes:

- While it might be tempting to use the .csv file as the *master*
file, doing so will loose the 4-hex digit formatting of the USV column, so
is not recommended. Instead, all edits should be done to the .xlsx file
and that should be exported to the .csv and .txt formats.

### Excerpting project-specific `glyph_data.csv` files

The easiest way to create project-specific `glyph_data.csv` files is to 
use `../tools/make_glyphdata.py`. For example, to make the glyph_data file for 
Scheherazade use `-f s` as follows:

```
cd font-arab-tools/absGlyphList
../tools/make_glyphdata.py -f s
```
This will create Scheherazde-specific `glyph_data.csv` (in the current directory) 
which can then be moved to `.../font-scheherazade/source`.


The harder, manual procedure that can still be used:

- Open `absGlyphList.xlsx` (Excel or Calc should work equally well)
- Set the `Fonts` column filter to select records that are _not_ applicable
to the project in question. Using Harmattan as an example, select all of
the rows _except_ those containing `*` or `H` (e.g. `H`, `SH`,
`SHL`, `SHLM`, etc.).
- Delete all the resultant rows (except the column headers of course)
- Clear the `Fonts` column filter -- you should have just the glyphs for the
project in question.
- Depending on whether the project uses the old "abs" naming convention
or the new GlyphsApp-compatible names, delete either column B (`GlyphsName`)
or column A (`Name`) (respectively).
- Change the header of the remaining column A to `glyph_name`.
- Optionally: delete other columns you don't need for the project.
- DO NOT SAVE the modified `absGlyphList.xlsx` file.
- Rather, save the file as ascii-encoded comma-separated values (.csv) to the project repo as `source/glyph_data.csv`.
