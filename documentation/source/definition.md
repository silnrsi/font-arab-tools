---
title: Definition of terms
---

## Definition of terms


* **Arabic:** since this whole document is about Arabic script, from here on we’ll use the term “Arabic” to mean the _Arabic language_. If we need to identify the script, we’ll say “ABS”.
* **shadda:** U+0651 ARABIC SHADDA, a combining mark used to represent gemination (elongation) of a consonant, drawn above the consonant it modifies.
* **vowel mark:** generic term to identify the combining marks that are most often used to represent vowels, such marks are drawn above or below the consonant that the vowel logically follows.
* **kasra:** U+0650 ARABIC KASRA, a particularly common vowel mark below. Unless otherwise indicated rules related to _kasra_ also apply to U+064D ARABIC KASRATAN.
* **hamza:** U+0654 ARABIC HAMZA ABOVE or U+0655 ARABIC HAMZA BELOW and also used as part of existing compositions such as U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE.
* **maddah:** U+0653 ARABIC MADDAH ABOVE and also part of existing composition U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE. Unless otherwise indicated, rules related to _maddah_ also apply to U+06E4 ARABIC SMALL HIGH MADDA.
* **CGJ:** U+034F COMBINING GRAPHEME JOINER


### Caveats

* We recognize that different calligraphic or language traditions may disagree about some things, e.g., Persian and Arabic rules may be different, or things that are semantically identical in Arabic may not be so in another language. 
* We also recognize that a lot of the dictates regarding correctness are based on existing renderings of the Qur’an and thus may be more particular or stringent than required for practical orthographies.
* Finally it is clear that the Unicode-normalized ordering of diacritics, while helpful for its intended purpose (string equality testing), is not particularly helpful for rendering. Specifically, the Unicode normal order does not put marks in an order that is “logical” to the reader or is graphically appropriate. We might hope, for example, that marks that are rendered “closer” to the base would appear early in a normalized string, but they don’t. Shadda and hamza are particularly problematic in this regard. 


### Unicode Normal Order

For reference, here are the Arabic combining marks shown in ascending order by their Unicode Combining Class values. If text is presented to the rendering engine in NFD, this is the ordering of the marks:

Character | Combining Class
--------- | ---------------
U+064B ARABIC FATHATAN<br/>U+08F0 ARABIC OPEN FATHATAN | 27
U+064C ARABIC DAMMATAN<br/>U+08F1 ARABIC OPEN DAMMATAN | 28
U+064D ARABIC KASRATAN<br/>U+08F2 ARABIC OPEN KASRATAN | 29
U+0618 ARABIC SMALL FATHA</br>U+064E ARABIC FATHA | 30
U+0619 ARABIC SMALL DAMMA<br/>U+064F ARABIC DAMMA | 31
U+061A ARABIC SMALL KASRA<br/>U+0650 ARABIC KASRA | 32
<span style="color:blue">U+0651 ARABIC SHADDA</span> | 33
U+0652 ARABIC SUKUN | 34
U+0670 ARABIC LETTER SUPERSCRIPT ALEF | 35
<span style="color:red">U+0655 ARABIC HAMZA BELOW</span><br/>U+0656 ARABIC SUBSCRIPT ALEF<br/>U+065C ARABIC VOWEL SIGN DOT BELOW<br/>U+065F ARABIC WAVY HAMZA BELOW<br/><span style="color:red">U+06E3 ARABIC SMALL LOW SEEN</span><br/>U+06EA ARABIC EMPTY CENTRE LOW STOP<br/>U+06ED ARABIC SMALL LOW MEEM<br/><span style="color:red">U+08CF ARABIC LARGE ROUND DOT BELOW</span><br/>U+08D0 ARABIC SUKUN BELOW<br/>U+08D1 ARABIC LARGE CIRCLE BELOW<br/>U+08D2 ARABIC LARGE ROUND DOT INSIDE CIRCLE BELOW<br/><span style="color:red">U+08D3 ARABIC SMALL LOW WAW</span><br/>U+08E3 ARABIC TURNED DAMMA BELOW<br/>U+08E6 ARABIC CURLY KASRA<br/>U+08E9 ARABIC CURLY KASRATAN<br/>U+08ED ARABIC TONE ONE DOT BELOW<br/>U+08EE ARABIC TONE TWO DOTS BELOW<br/>U+08EF ARABIC TONE LOOP BELOW<br/>U+08F6 ARABIC KASRA WITH DOT BELOW<br/>U+08F9 ARABIC LEFT ARROWHEAD BELOW<br/>U+08FA ARABIC RIGHT ARROWHEAD BELOW | 220
U+0610 ARABIC SIGN SALLALLAHOU ALAYHE WASSALLAM<br/>U+0611 ARABIC SIGN ALAYHE ASSALLAM<br/>U+0612 ARABIC SIGN RAHMATULLAH ALAYHE<br/>U+0613 ARABIC SIGN RADI ALLAHOU ANHU<br/>U+0614 ARABIC SIGN TAKHALLUS<br/>U+0615 ARABIC SMALL HIGH TAH<br/>U+0616 ARABIC SMALL HIGH LIGATURE ALEF WITH LAM WITH YEH<br/>U+0617 ARABIC SMALL HIGH ZAIN<br/>U+0653 ARABIC MADDAH ABOVE<br/><span style="color:red">U+0654 ARABIC HAMZA ABOVE</span><br/>U+0657 ARABIC INVERTED DAMMA<br/><span style="color:red">U+0658 ARABIC MARK NOON GHUNNA</span><br/>U+0659 ARABIC ZWARAKAY<br/>U+065A ARABIC VOWEL SIGN SMALL V ABOVE<br/>U+065B ARABIC VOWEL SIGN INVERTED SMALL V ABOVE<br/>U+065D ARABIC REVERSED DAMMA<br/>U+065E ARABIC FATHA WITH TWO DOTS<br/>U+06D6 ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA<br/>U+06D7 ARABIC SMALL HIGH LIGATURE QAF WITH LAM WITH ALEF MAKSURA<br/>U+06D8 ARABIC SMALL HIGH MEEM INITIAL FORM<br/>U+06D9 ARABIC SMALL HIGH LAM ALEF<br/>U+06DA ARABIC SMALL HIGH JEEM<br/>U+06DB ARABIC SMALL HIGH THREE DOTS<br/><span style="color:red">U+06DC ARABIC SMALL HIGH SEEN</span><br/>U+06DF ARABIC SMALL HIGH ROUNDED ZERO<br/>U+06E0 ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO<br/>U+06E1 ARABIC SMALL HIGH DOTLESS HEAD OF KHAH<br/>U+06E2 ARABIC SMALL HIGH MEEM ISOLATED FORM<br/>U+06E4 ARABIC SMALL HIGH MADDA<br/><span style="color:red">U+06E7 ARABIC SMALL HIGH YEH</span><br/><span style="color:red">U+06E8 ARABIC SMALL HIGH NOON</span><br/>U+06EB ARABIC EMPTY CENTRE HIGH STOP<br/>U+06EC ARABIC ROUNDED HIGH STOP WITH FILLED CENTRE<br/><span style="color:red">U+08CA ARABIC SMALL HIGH FARSI YEH</span><br/><span style="color:red">U+08CB ARABIC SMALL HIGH YEH BARREE WITH TWO DOTS BELOW</span><br/>U+08CC ARABIC SMALL HIGH WORD SAH<br/><span style="color:red">U+08CD ARABIC SMALL HIGH ZAH</span><br/><span style="color:red">U+08CE ARABIC LARGE ROUND DOT ABOVE</span><br/>U+08D4 ARABIC SMALL HIGH WORD AR-RUB<br/>U+08D5 ARABIC SMALL HIGH SAD<br/>U+08D6 ARABIC SMALL HIGH AIN<br/>U+08D7 ARABIC SMALL HIGH QAF<br/>U+08D8 ARABIC SMALL HIGH NOON WITH KASRA<br/>U+08D9 ARABIC SMALL LOW NOON WITH KASRA<br/>U+08DA ARABIC SMALL HIGH WORD ATH-THALATHA<br/>U+08DB ARABIC SMALL HIGH WORD AS-SAJDA<br/>U+08DC ARABIC SMALL HIGH WORD AN-NISF<br/>U+08DD ARABIC SMALL HIGH WORD SAKTA<br/>U+08DE ARABIC SMALL HIGH WORD QIF<br/>U+08DF ARABIC SMALL HIGH WORD WAQFA<br/>U+08E0 ARABIC SMALL HIGH FOOTNOTE MARKER<br/>U+08E1 ARABIC SMALL HIGH SIGN SAFHA<br/>U+08E4 ARABIC CURLY FATHA<br/>U+08E5 ARABIC CURLY DAMMA<br/>U+08E7 ARABIC CURLY FATHATAN<br/>U+08E8 ARABIC CURLY DAMMATAN<br/>U+08EA ARABIC TONE ONE DOT ABOVE<br/>U+08EB ARABIC TONE TWO DOTS ABOVE<br/>U+08EC ARABIC TONE LOOP ABOVE<br/><span style="color:red">U+08F3 ARABIC SMALL HIGH WAW</span><br/>U+08F4 ARABIC FATHA WITH RING<br/>U+08F5 ARABIC FATHA WITH DOT ABOVE<br/>U+08F7 ARABIC LEFT ARROWHEAD ABOVE<br/>U+08F8 ARABIC RIGHT ARROWHEAD ABOVE<br/>U+08FB ARABIC DOUBLE RIGHT ARROWHEAD ABOVE<br/>U+08FC ARABIC DOUBLE RIGHT ARROWHEAD ABOVE WITH DOT<br/>U+08FD ARABIC RIGHT ARROWHEAD ABOVE WITH DOT<br/>U+08FE ARABIC DAMMA WITH DOT<br/>U+08FF ARABIC MARK SIDEWAYS NOON GHUNNA | 230

Red characters are part of the Modifier Combining Marks (MCM) as discussed in [Unicode Technical Report #53](https://unicode.org/reports/tr53/). The blue character _shadda_ is also discussed in UTR #53.


