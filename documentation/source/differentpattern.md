---
title: Characters which follow a different dot pattern
---

The _nukat_ (dots) on most _dual joining_ characters follow a consistent pattern. There are a few characters which do not follow this pattern. These are:

Characters | Glyph | Comment
:---------- | ----:  | :-------
06BA ARABIC LETTER NOON GHUNNA | <span class='scheherazadenewL-R normal'>&#x06ba; &#x06ba;&#x06ba;&#x06ba;</span> | all forms are dotless [[See note](#note)] |
06BD ARABIC LETTER NOON WITH THREE DOTS ABOVE | <span class='scheherazadenewL-R normal'>&#x06bd;&#x0020;&#x06bd;&#x06bd;&#x06bd;</span> | initial and medial forms of this letter have dots below instead of above
06CC ARABIC LETTER FARSI YEH | <span class='scheherazadenewL-R normal'>&#x06cc;&#x0020;&#x06cc;&#x06cc;&#x06cc;</span> | initial and medial forms of this letter have dots below
0775 ARABIC LETTER FARSI YEH WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE | <span class='scheherazadenewL-R normal'>&#x0775;&#x0020;&#x0775;&#x0775;&#x0775;</span> | initial and medial forms of this letter have dots below
0776 ARABIC LETTER FARSI YEH WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE | <span class='scheherazadenewL-R normal'>&#x0776;&#x0020;&#x0776;&#x0776;&#x0776;</span> | initial and medial forms of this letter have dots below
077A ARABIC LETTER YEH BARREE WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE | <span class='scheherazadenewL-R normal'>&#x077a;&#x0020;&#x077a;&#x077a;&#x077a;</span> | initial and medial forms of this letter have dots below
077B ARABIC LETTER YEH BARREE WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE | <span class='scheherazadenewL-R normal'>&#x077b;&#x0020;&#x077b;&#x077b;&#x077b;</span> | initial and medial forms of this letter have dots below
08BB ARABIC LETTER AFRICAN FEH | <span class='scheherazadenewL-R normal'>&#x08bb;&#x0020;&#x08bb;&#x08bb;&#x08bb;</span> | initial and medial forms of this letter have a single dot below
08BC ARABIC LETTER AFRICAN QAF | <span class='scheherazadenewL-R normal'>&#x08bc;&#x0020;&#x08bc;&#x08bc;&#x08bc;</span> | initial and medial forms of this letter have a single dot above
08BD ARABIC LETTER AFRICAN NOON | <span class='scheherazadenewL-R normal'>&#x08bd;&#x0020;&#x08bd;&#x08bd;&#x08bd;</span> | initial and medial forms of this letter have a single dot above
08C4 ARABIC LETTER AFRICAN QAF WITH THREE DOTS ABOVE | <span class='scheherazadenewL-R normal'>&#x08c4;&#x0020;&#x08c4;&#x08c4;&#x08c4;</span> | initial and medial forms of this letter have an additional single dot above|

## Different behavior with hamza

Characters | Glyph | Comment
:---------- | ----:  | :-------
064A ARABIC LETTER YEH | <span class='scheherazadenewL-R normal'>&#x064a;&#x0654; &#x064a;&#x0654;&#x064a;&#x0654;&#x064a;&#x0654; &#x064a;&#x064f; &#x064a;&#x064f;&#x064a;&#x064f;&#x064a;&#x064f;</span> | loses its dots when used in combination with 0654, retains its dots when used in combination with other combining marks [[See note](#note)] |
06CC ARABIC LETTER FARSI YEH | <span class='scheherazadenewL-R normal'>&#x06cc;&#x0654; &#x06cc;&#x0654;&#x06cc;&#x0654;&#x06cc;&#x0654; &#x06cc;&#x064f; &#x06cc;&#x064f;&#x06cc;&#x064f;&#x06cc;&#x064f;</span> | should *not* lose its dots when used in combination with 0654 [[See note](#note)] |


<a name="note">Note:</a> 

There has been much variety among Arabic script fonts as to whether or not U+06BA ARABIC LETTER NOON GHUNNA has dots in its initial and medial forms. However, since Unicode 7 (June, 2014), Unicode documentation[[1](#1)] says that U+06BA ARABIC LETTER NOON GHUNNA should be dotless in all four contextual forms. In cases where nasalization needs to be marked in initial or medial contexts, the ordinary noon, U+0646 ARABIC LETTER NOON, should be used, optionally with U+0658 ARABIC MARK NOON GHUNNA. 

The annotation for U+064A ARABIC LETTER YEH specifically says "loses its dots when used in combination with 0654" and "retains its dots when used in combination with other combining marks".

As of Unicode 15.1.0 the annotation for U+06CC ARABIC LETTER FARSI YEH says "initial and medial forms of this letter have two
horizontal dots below" and "retains its dots in initial and medial forms when used in combination with 0654" This is how SIL fonts have implemented it.

---

<a name="1">1</a> The Unicode Consortium. The Unicode Standard, Version 16.0.0, (South San Francisco, CA: The Unicode Consortium, September 10, 2024. ISBN 978-1-936213-34-4), [Noon Ghunna](https://www.unicode.org/versions/latest/core-spec/chapter-9/#G47721).

