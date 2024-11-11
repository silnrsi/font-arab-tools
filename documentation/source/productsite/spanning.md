
Some characters in Arabic script are signs that span (or enclose) numbers, such as U+06DD End of Ayah and U+0605 Number Mark Above:

<img class='fullsize' alt='Spanning sign examples' src='https://software.sil.org/arabicfonts/wp-content/uploads/sites/28/2024/11/spanning_signs.png' />
[caption]<em>Spanning sign examples</em>[/caption]

Over time these have been variously called:

* _prepended concatenation marks_
* _subtending marks_
* _prefixed format control characters_

For the purposes of this document, we will use the term _spanning signs_ (or more simply, _signs_) to refer to these characters and _sign glyphs_ for the glyphs within the font that will represent them.

Since digit choice is dependent on regional use, these marks may be used with European digits (U+0030..U+0039), ARABIC-INDIC digits (U+0660..U+0669) or with EXTENDED ARABIC-INDIC digits (U+06F0..U+06F9). 

Many applications are able to display these properly, just by typing the spanning signs (such as U+06DD _end of ayah_) before the digit(s). This will not work unless your application is set up to handle complex scripts.

Occasionally some applications may require the following hack: 

* precede the entire sequence (spanning sign plus following digits) with
    * 202D LEFT-TO-RIGHT OVERRIDE _or_
    * 202E RIGHT-TO-LEFT OVERRIDE
* follow the entire sequence with U+202C POP DIRECTIONAL FORMATTING. 

Exactly which of these might work depends on your application. 

From a practical standpoint there isn't a need to support an arbitrary-length sequence of digits. For SIL fonts, we have found the maximum number of digits as documented in the following table to be sufficient for most uses.

Examples of how these appear are shown below using varying numbers of digits with _hamza_ used as a separator.

<!-- Note: The table below includes the U+202D/U+202C hack so that our generated PDFs display correctly
(particularly for 0890 ARABIC POUND MARK ABOVE and 0891 ARABIC PIASTRE MARK ABOVE) -->

Characters | Glyph | max # digits
:---------- | ----:  | :-----
0600 ARABIC NUMBER SIGN | <span class='scheherazadenew-R normal'>&#x0621;&#x202d;&#x0600;&#x0661;&#x202c;&#x0621;&#x202d;&#x0600;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0600;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;</span> | 3
0601 ARABIC SIGN SANAH (year sign) | <span class='scheherazadenew-R normal'>&#x0621;&#x202d;&#x0601;&#x0661;&#x202c;&#x0621;&#x202d;&#x0601;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0601;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;&#x202d;&#x0601;&#x0661;&#x0662;&#x0663;&#x0664;&#x202c;&#x0621;</span> | 4
0602 ARABIC FOOTNOTE MARKER | <span class='scheherazadenew-R normal'>&#x0621;&#x202d;&#x0602;&#x0661;&#x202c;&#x0621;&#x202d;&#x0602;&#x0661;&#x0662;&#x202c;&#x0621;</span> | 2
0603 ARABIC SIGN SAFHA | <span class='scheherazadenew-R normal'>&#x0621;&#x202d;&#x0603;&#x0661;&#x202c;&#x0621;&#x202d;&#x0603;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0603;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;&#x202d;&#x0603;&#x0661;&#x0662;&#x0663;&#x0664;&#x202c;&#x0621;</span> | 4
0604 ARABIC SIGN SAMVAT | <span class='scheherazadenew-R normal'>&#x0621;&#x202d;&#x0604;&#x0661;&#x202c;&#x0621;&#x202d;&#x0604;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0604;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;&#x202d;&#x0604;&#x0661;&#x0662;&#x0663;&#x0664;&#x202c;&#x0621;</span> | 4
0605 ARABIC NUMBER MARK ABOVE | <span class='scheherazadenew-R normal'>&#x0621;&#x202d;&#x0605;&#x0661;&#x202c;&#x0621;&#x202d;&#x0605;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0605;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;&#x202d;&#x0605;&#x0661;&#x0662;&#x0663;&#x0664;&#x202c;&#x0621;</span> | 4
0890 ARABIC POUND MARK ABOVE | <span class='scheherazadenew-R normal'>&#x0621;&#x202d;&#x0890;&#x0661;&#x202c;&#x0621;&#x202d;&#x0890;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0890;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;&#x202d;&#x0890;&#x0661;&#x0662;&#x0663;&#x0664;&#x202c;&#x0621;</span> | 4
0891 ARABIC PIASTRE MARK ABOVE | <span class='scheherazadenew-R normal'>&#x0621;&#x202d;&#x0891;&#x0661;&#x202c;&#x0621;&#x202d;&#x0891;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x0891;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;&#x202d;&#x0891;&#x0661;&#x0662;&#x0663;&#x0664;&#x202c;&#x0621;</span> | 4
06DD ARABIC END OF AYAH | <span class='scheherazadenew-R normal'>&#x0621;&#x202d;&#x06dd;&#x0661;&#x202c;&#x0621;&#x202d;&#x06dd;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x06dd;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;</span> | 3
08E2 ARABIC DISPUTED END OF AYAH | <span class='scheherazadenew-R normal'>&#x0621;&#x202d;&#x08e2;&#x0661;&#x202c;&#x0621;&#x202d;&#x08e2;&#x0661;&#x0662;&#x202c;&#x0621;&#x202d;&#x08e2;&#x0661;&#x0662;&#x0663;&#x202c;&#x0621;</span> | 3

For more Unicode information about these characters, see _Signs Spanning Numbers_ in [Section 9.2](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-9/#G50226) and _Prepended Concatenation Marks_ in [Section 23.2](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-23/#G37908) of The Unicode Standard.

[font id='scheherazadenew' face='ScheherazadeNew-Regular' bold='ScheherazadeNew-Bold' size='200%' rtl=1]
