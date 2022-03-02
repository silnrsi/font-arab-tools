---
title: Lam-Alef and Kashida
---

This note from one of the [Amiri font’s fea](https://github.com/aliftype/amiri/blob/main/sources/kashida.fea) files explains the problem:

```
# Kashida justification as implemented in most, if not all, applications is
# broken by design; it inserts kashidas *after* doing OT layout which makes it
# impossible for OT code to interact with those kashidas breaking all sorts of
# things.
```

Most fonts ligate _lam+alef_ so it is a single glyph. Historically, SIL fonts did not do that. As a result, MS Word (at least 2013, 2016) would sometimes insert a kashida between lam and alef when justifying text rendered in our fonts. For this reason, we have begun implementing _lam+alef_ as a single glyph.

Amiri’s designer, Khaled Hosney, goes on to say:

```
# To trick LibreOffice/MS Office to not do kashida justification we set the
# default kashida to a zero width, blank glyph which makes them to think there
# is no suitable kashida glyph, resorting back to regular justification
# To get manually inserted kashida working we use an rlig feature to map to the
# actual kashida glyph(s).
```

Because Amiri has curved connections, and thus lots of different kashida glyphs (for different numbers of kashidas inserted), the fea logic is somewhat complex. For our fonts, with flat joins, the solution is much simpler. We simply include both an encoded zero-width glyph, kashida-ar, and an unencoded non-zero width glyph, kashida-ar.haswidth, in our fonts. Then at some point in the fea/gdl, replace kashida-ar with kashida-ar.haswidth.

**Decision:** In Scheherazade New we chose not to create lam/alef ligatures for the alef with high hamza. This is for two reasons. 

* Unicode has discouraged the use of alef with high hamza (U+0675) because the decomposition does not reflect the preferred order of representation. 
* High hamza is only word initial and so it is unlikely that a _lam+alef_ with _high hamza_ would ever occur. Additionally, there is a terrible collision with the vertical position we have been asked to position the high hamza at and it doesn’t seem worth trying to make it look right when it doesn’t occur in the real world. 

## Papers

This is an interesting paper that discusses ligatures (not just lam/alef and lam/lam/heh but other typographic ligatures). It’s a very old document, but it discusses some of the problems: Haralambous, Yannis. 1995. [The traditional Arabic typecase extended to the Unicode set of glyphs](https://www.academia.edu/733363/The_traditional_Arabic_typecase_extended_to_the_Unicode_set_of_glyphs?email_work_card=title)
