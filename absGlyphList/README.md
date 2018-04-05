Copyright (c) 2018, SIL International (http://www.sil.org).
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
  `absBehThreeDotsUpBelow` starting with Harmattan, but other projects will
  pick up this shorter name going forward)
- It contains multiple sort orders including legacy and current.
- It contains data for legacy glyphs that we no longer need or use.

As a result of the above, the absGlyphList is not directly usable for any
of the font projects, but instead individual projects will need to excerpt
the file for their use.

An additional implication of the above is that the column headers do not --
indeed cannot -- conform exactly to NRSI conventions (because, for example,
NRSI conventions allow only one `glyph_name` column).

### `absGlyphList.txt` and `absGlyphList.csv`

These are tab- and comma-separated value text files that are equivalents of
the master `abGlyphList.xlsx`. Whenever the .xlsx file is updated, the
.txt and .csv files should be also be updated (by using "Save As...")

Notes:

- The tab-separated (.txt) file remains in use by
some older projects and tools until they get transitioned to the new
workflow, at which time it will be dropped.

- While it might be tempting to use the .csv file as the *master*
file, doing so will loose the 4-hex digit formatting of the USV column, so
I don't recommend it. Instead, all edits should be done to the .xlsx file
and that should be exported to the .csv and .txt formats.


### Excerpting project-specific `glyph_data.csv` files

Here is one procedure that can be used:

- Open `absGlyphList.xlsx` (Word or Calc should work equally well)
- Set the `Fonts` column filter to select records that are _not_ applicable
to the project in question. For example, for Harmattan, select all of
the following: `-`, `L`, `S`, `SL`, and `SLM` but deselect `*`, `H`, `SH`,
`SHL`, `SHLM`, and `SHM`.
- Delete all the resultant rows (except the column headers of course)
- Clear the `Fonts` column filter -- you should have just the glyphs for the
project in question.
- Depending on whether the project uses the old "abs" naming convention
or the new GlyphsApp-compatible names, delete either column B (`GlyphsName`)
or column A (`Name`) (respectively).
- Change the header of the remaining column A to `glyph_name`.
- Optionally: delete other columns you don't need for the project.
- Save the file as ascii-encoded comma-separated values (.csv) _to the project
repo_ as `source/glyph_data.csv`.
