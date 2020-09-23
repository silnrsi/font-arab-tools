In order to bring consistency to the glyph name extensions, we are changing some of them.

For example, we want to change 
    meem-ar.sindhi.fina
to
    meem-ar.fina.sindhi

Not counting glyphs that are exclusive to Alkalami and Awami, there are 61 glyphs, 
with 21 unique extensions, in the absGlyphList that we want to change

Among other things, this change should allow us to use more of the automatically-
generated classes instead of manually maintained ones.

The files in this folder are used to make these changes in various project files:

- extensions.csv     a simple oldname,newname csv file covering all 61 glyph.
                     This is useful as input to psfrenameglyphs.

- extensions-fea.sed a sed script that changes just the extensions themselves,
                     e.g. changing .knottedHigh.fina --> .fina.knottedHigh
                     The script can be used, for example, to change glyph_data.csv,
                     classes.xml or any fea files.

- extensions-gdl.sed a sed script like above, but assumes gdl naming conventions
                     e.g., _knotted_flat_fina --> _fina_knotted_flat
                     This is useful for changing all gdl and gdh files

YMMV, but for a given project here are the typical steps to go through:

    cd source
    # for each font:
        psfrenameglyphs -p backup=false -i extensions.csv masters/<fontname>.ufo
    # At this point, ./preglyphs should work
    # If you don't have a composites definition file, omit last parameter on next line:
    sed -i -f extensions-fea.sed opentype/*.fea* classes.xml glyph_data.csv masters/composites.txt
    sed -i -f extensions-gdl.sed graphite/*.gd*
    cd ..
    ./preflight   # needed to fix productionnames in UFOs

You may have other files, such as filters for Glyphs. As long as they are simple text files using
the psnames, then the extensions-fea.sed file can be used as above.

resulting classes we could eliminate:
    Meem.sindhi         --> c_sindhi
    Meem                --> cno_sindhi
    AlefFinAfterLamMed  --> c_postLamIni
    AlefFin             --> cno_postLamIni
    AlefFinAfterLamIni  --> c_postLamMed
    AlefFin             --> cno_postLamMed
    [LamIniBeforeAlef LamMedBeforeAlef]  --> c_preAlef
    [LamIni LamMed]     --> cno_preAlef

Unfortunately we still need:
	LamIniBeforeAlef
	LamMedBeforeAlef
    LamIso
    LamFin
    AlefIso

which means we may as well manually maintain all the lam & alef classes needed.
