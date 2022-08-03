---
title: Signs Spanning Numbers
---

Some characters in Arabic script are signs that span (or enclose) numbers. Over time these have been variously called:

* _prepended concatenation marks_
* _subtending marks_
* _prefixed format control characters_

Since digit choice is dependent on regional use, these marks may be used with European digits (U+0030..U+0039), ARABIC-INDIC digits (U+0660..U+0669) or with EXTENDED ARABIC-INDIC digits (U+06F0..U+06F9). 

From a practical standpoint there isn't a need to support an arbitrary-length sequence of digits. For SIL fonts, we have found the maximum number of digits as documented in the following table to be sufficient for most uses.

Examples of how these are formatted are shown below using varying number of digits with _hamza_ used as a separator.

Characters | Glyph | max # digits
:---------- | ----:  | :-----
0600 ARABIC NUMBER SIGN | <span class='scheherazadenewL-R normal'>&#x0621;&#x202d;&#x0600;&#x0661;&#x202c;&#x0621;&#x202d;&#x0600;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0600;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;</span> | 3
0601 ARABIC SIGN SANAH (year sign) | <span class='scheherazadenewL-R normal'>&#x0621;&#x202d;&#x0601;&#x0661;&#x202c;&#x0621;&#x202d;&#x0601;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0601;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;&#x202d;&#x0601;&#x0661;&#x0662;&#x0663;&#x0664;&#x202c;&#x0621;</span> | 4
0602 ARABIC FOOTNOTE MARKER | <span class='scheherazadenewL-R normal'>&#x0621;&#x202d;&#x0602;&#x0661;&#x202c;&#x0621;&#x202d;&#x0602;&#x0661;&#x0662;&#x202c;&#x0621;</span> | 2
0603 ARABIC SIGN SAFHA | <span class='scheherazadenewL-R normal'>&#x0621;&#x202d;&#x0603;&#x0661;&#x202c;&#x0621;&#x202d;&#x0603;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0603;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;&#x202d;&#x0603;&#x0661;&#x0662;&#x0663;&#x0664;&#x202c;&#x0621;</span> | 4
0604 ARABIC SIGN SAMVAT | <span class='scheherazadenewL-R normal'>&#x0621;&#x202d;&#x0604;&#x0661;&#x202c;&#x0621;&#x202d;&#x0604;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0604;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;&#x202d;&#x0604;&#x0661;&#x0662;&#x0663;&#x0664;&#x202c;&#x0621;</span> | 4
0605 ARABIC NUMBER MARK ABOVE | <span class='scheherazadenewL-R normal'>&#x0621;&#x202d;&#x0605;&#x0661;&#x202c;&#x0621;&#x202d;&#x0605;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0605;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;&#x202d;&#x0605;&#x0661;&#x0662;&#x0663;&#x0664;&#x202c;&#x0621;</span> | 4
0890 ARABIC POUND MARK ABOVE | <span class='scheherazadenewL-R normal'>&#x0621;&#x202d;&#x0890;&#x0661;&#x202c;&#x0621;&#x202d;&#x0890;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0890;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;&#x202d;&#x0890;&#x0661;&#x0662;&#x0663;&#x0664;&#x202c;&#x0621;</span> | 4
0891 ARABIC PIASTRE MARK ABOVE | <span class='scheherazadenewL-R normal'>&#x0621;&#x202d;&#x0891;&#x0661;&#x202c;&#x0621;&#x202d;&#x0891;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0891;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;&#x202d;&#x0891;&#x0661;&#x0662;&#x0663;&#x0664;&#x202c;&#x0621;</span> | 4
06DD ARABIC END OF AYAH | <span class='scheherazadenewL-R normal'>&#x0621;&#x202d;&#x06dd;&#x0661;&#x202c;&#x0621;&#x202d;&#x06dd;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x06dd;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;</span> | 3
08E2 ARABIC DISPUTED END OF AYAH | <span class='scheherazadenewL-R normal'>&#x0621;&#x202d;&#x08e2;&#x0661;&#x202c;&#x0621;&#x202d;&#x08e2;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x08e2;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;</span> | 3
