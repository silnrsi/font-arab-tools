# Definition of terms

* **Arabic:** By itself, this term can refer to the _script_, which is used by many languages including Arabic, or specifically the _language_ as distinct from other languages that use the script. In this document where the distinction is important we'll try to qualify the term by saying "Arabic script" or "Arabic language".
* **shadda:** U+0651 ARABIC SHADDA, a combining mark used to represent gemination (elongation) of a consonant, drawn above the consonant it modifies.
* **vowel mark:** generic term to identify the combining marks that are most often used to represent vowels, such marks are drawn above or below the consonant that the vowel logically follows.
* **kasra:** U+0650 ARABIC KASRA, a particularly common vowel mark below. Unless otherwise indicated rules related to _kasra_ also apply to U+064D ARABIC KASRATAN.
* **hamza:** U+0654 ARABIC HAMZA ABOVE or U+0655 ARABIC HAMZA BELOW and also used as part of existing compositions such as U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE.
* **maddah:** U+0653 ARABIC MADDAH ABOVE and also part of existing composition U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE. Unless otherwise indicated, rules related to _maddah_ also apply to U+06E4 ARABIC SMALL HIGH MADDA.
* **ligature:** the special form that specific sequences of letters can take that is different to how the letters might otherwise appear. The *lam-alef* ligature is a well known example. Note that within a font, ligature forms can be _implemented_ as one glyph (often called a _ligature glyph_) or as multiple contextually-shaped glyphs that result in the desired display.
* **CGJ:** U+034F COMBINING GRAPHEME JOINER


## Caveats

* We recognize that different calligraphic or language traditions may disagree about some things, e.g., Persian and Arabic rules may be different, or things that are semantically identical in Arabic may not be so in another language. 
* We also recognize that a lot of the dictates regarding correctness are based on existing renderings of the Qur’an and thus may be more particular or stringent than required for practical orthographies.
* Finally it is clear that the Unicode-normalized ordering of diacritics, while helpful for its intended purpose (string equality testing), is not particularly helpful for rendering. Specifically, the Unicode normal order does not put marks in an order that is “logical” to the reader or is graphically appropriate. We might hope, for example, that marks that are rendered “closer” to the base would appear early in a normalized string, but they don’t. Shadda and hamza are particularly problematic in this regard. 


## Unicode Normal Order

For reference, here are the Arabic combining marks shown in ascending order by their Unicode Combining Class values. If text is presented to the rendering engine in NFD, this is the ordering of the marks:

Character | Combining Class
:--- | :---
064B ARABIC FATHATAN<br/>08F0 ARABIC OPEN FATHATAN | 27
064C ARABIC DAMMATAN<br/>08F1 ARABIC OPEN DAMMATAN | 28
064D ARABIC KASRATAN<br/>08F2 ARABIC OPEN KASRATAN | 29
0618 ARABIC SMALL FATHA</br>064E ARABIC FATHA | 30
0619 ARABIC SMALL DAMMA<br/>064F ARABIC DAMMA | 31
061A ARABIC SMALL KASRA<br/>0650 ARABIC KASRA | 32
_**0651 ARABIC SHADDA**_ | 33
0652 ARABIC SUKUN | 34
0670 ARABIC LETTER SUPERSCRIPT ALEF | 35
**0655 ARABIC HAMZA BELOW**<br/>0656 ARABIC SUBSCRIPT ALEF<br/>065C ARABIC VOWEL SIGN DOT BELOW<br/>065F ARABIC WAVY HAMZA BELOW<br/>**06E3 ARABIC SMALL LOW SEEN**<br/>06EA ARABIC EMPTY CENTRE LOW STOP<br/>06ED ARABIC SMALL LOW MEEM<br/>**08CF ARABIC LARGE ROUND DOT BELOW**<br/>08D0 ARABIC SUKUN BELOW<br/>08D1 ARABIC LARGE CIRCLE BELOW<br/>08D2 ARABIC LARGE ROUND DOT INSIDE CIRCLE BELOW<br/>**08D3 ARABIC SMALL LOW WAW**<br/>08E3 ARABIC TURNED DAMMA BELOW<br/>08E6 ARABIC CURLY KASRA<br/>08E9 ARABIC CURLY KASRATAN<br/>08ED ARABIC TONE ONE DOT BELOW<br/>08EE ARABIC TONE TWO DOTS BELOW<br/>08EF ARABIC TONE LOOP BELOW<br/>08F6 ARABIC KASRA WITH DOT BELOW<br/>08F9 ARABIC LEFT ARROWHEAD BELOW<br/>08FA ARABIC RIGHT ARROWHEAD BELOW | 220
0610 ARABIC SIGN SALLALLAHOU ALAYHE WASSALLAM<br/>0611 ARABIC SIGN ALAYHE ASSALLAM<br/>0612 ARABIC SIGN RAHMATULLAH ALAYHE<br/>0613 ARABIC SIGN RADI ALLAHOU ANHU<br/>0614 ARABIC SIGN TAKHALLUS<br/>0615 ARABIC SMALL HIGH TAH<br/>0616 ARABIC SMALL HIGH LIGATURE ALEF WITH LAM WITH YEH<br/>0617 ARABIC SMALL HIGH ZAIN<br/>0653 ARABIC MADDAH ABOVE<br/>**0654 ARABIC HAMZA ABOVE**<br/>0657 ARABIC INVERTED DAMMA<br/>**0658 ARABIC MARK NOON GHUNNA**<br/>0659 ARABIC ZWARAKAY<br/>065A ARABIC VOWEL SIGN SMALL V ABOVE<br/>065B ARABIC VOWEL SIGN INVERTED SMALL V ABOVE<br/>065D ARABIC REVERSED DAMMA<br/>065E ARABIC FATHA WITH TWO DOTS<br/>06D6 ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA<br/>06D7 ARABIC SMALL HIGH LIGATURE QAF WITH LAM WITH ALEF MAKSURA<br/>06D8 ARABIC SMALL HIGH MEEM INITIAL FORM<br/>06D9 ARABIC SMALL HIGH LAM ALEF<br/>06DA ARABIC SMALL HIGH JEEM<br/>06DB ARABIC SMALL HIGH THREE DOTS<br/>**06DC ARABIC SMALL HIGH SEEN**<br/>06DF ARABIC SMALL HIGH ROUNDED ZERO<br/>06E0 ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO<br/>06E1 ARABIC SMALL HIGH DOTLESS HEAD OF KHAH<br/>06E2 ARABIC SMALL HIGH MEEM ISOLATED FORM<br/>06E4 ARABIC SMALL HIGH MADDA<br/>**06E7 ARABIC SMALL HIGH YEH**<br/>**06E8 ARABIC SMALL HIGH NOON**<br/>06EB ARABIC EMPTY CENTRE HIGH STOP<br/>06EC ARABIC ROUNDED HIGH STOP WITH FILLED CENTRE<br/>**08CA ARABIC SMALL HIGH FARSI YEH**<br/>**08CB ARABIC SMALL HIGH YEH BARREE WITH TWO DOTS BELOW**<br/>08CC ARABIC SMALL HIGH WORD SAH<br/>**08CD ARABIC SMALL HIGH ZAH**<br/>**08CE ARABIC LARGE ROUND DOT ABOVE**<br/>08D4 ARABIC SMALL HIGH WORD AR-RUB<br/>08D5 ARABIC SMALL HIGH SAD<br/>08D6 ARABIC SMALL HIGH AIN<br/>08D7 ARABIC SMALL HIGH QAF<br/>08D8 ARABIC SMALL HIGH NOON WITH KASRA<br/>08D9 ARABIC SMALL LOW NOON WITH KASRA<br/>08DA ARABIC SMALL HIGH WORD ATH-THALATHA<br/>08DB ARABIC SMALL HIGH WORD AS-SAJDA<br/>08DC ARABIC SMALL HIGH WORD AN-NISF<br/>08DD ARABIC SMALL HIGH WORD SAKTA<br/>08DE ARABIC SMALL HIGH WORD QIF<br/>08DF ARABIC SMALL HIGH WORD WAQFA<br/>08E0 ARABIC SMALL HIGH FOOTNOTE MARKER<br/>08E1 ARABIC SMALL HIGH SIGN SAFHA<br/>08E4 ARABIC CURLY FATHA<br/>08E5 ARABIC CURLY DAMMA<br/>08E7 ARABIC CURLY FATHATAN<br/>08E8 ARABIC CURLY DAMMATAN<br/>08EA ARABIC TONE ONE DOT ABOVE<br/>08EB ARABIC TONE TWO DOTS ABOVE<br/>08EC ARABIC TONE LOOP ABOVE<br/>**08F3 ARABIC SMALL HIGH WAW**<br/>08F4 ARABIC FATHA WITH RING<br/>08F5 ARABIC FATHA WITH DOT ABOVE<br/>08F7 ARABIC LEFT ARROWHEAD ABOVE<br/>08F8 ARABIC RIGHT ARROWHEAD ABOVE<br/>08FB ARABIC DOUBLE RIGHT ARROWHEAD ABOVE<br/>08FC ARABIC DOUBLE RIGHT ARROWHEAD ABOVE WITH DOT<br/>08FD ARABIC RIGHT ARROWHEAD ABOVE WITH DOT<br/>08FE ARABIC DAMMA WITH DOT<br/>08FF ARABIC MARK SIDEWAYS NOON GHUNNA | 230

Bold characters are part of the Modifier Combining Marks (MCM) as discussed in [Unicode Technical Report #53](https://unicode.org/reports/tr53/). The bold-italic character _shadda_ is also discussed in UTR #53.


