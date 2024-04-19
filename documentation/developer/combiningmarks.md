# Combining mark ordering and positioning

SIL Arabic script fonts contain complex logic related to reordering combining marks so that they are displayed in a manner expected by the reader. Why these rules are necessary and how they work is described below.

## Problem statement

Consider the case where a base character is followed by one or more combining marks (Unicode calls this a _Combinging Character Sequence_). In essence the problem is this: 

* For scripts like Latin it is pretty obvious how to render the combining marks, for example marks above the base are rendered in a stack moving outward from the base. Unicode calls this the "inside-out" rule: marks that occur earlier in the text sequence are rendered closer the base than those that occur later. 

* For Arabic script it isn't so easy. For example a combining character sequence including a _hamza_ and _fatha_ should almost always be rendered with the _fatha_ above the _hamza_ no matter which order the characters appear in the text. But how does a font developer know the correct display order?

One might hope that, between the OpenType font specification and Unicode character encoding specification, this problem would have been solved years ago. Unfortunately it wasn't until 2018 that the first solution was adopted. Unfortunately there are many systems and applications that pre-date 2018, and so we're left with a mix of technologies to deal with. 

## Potential solutions to mark-to-mark positioning

Since data comes from a variety of sources with all kinds of variation in mark order, the obvious fix to the Arabic mark ordering problem is to re-order the characters in such a way that the standard available OpenType mark positioning rules "just work". 

Unicode provides two "normalized" mark orders that could be considered: Normal Form Composed (NFC) and Normal Form Decomposed (NFD). Both of these are based on a Unicode character property called Combining Character Class (ccc) and a standardized algorithm that reorders combining marks into ascending order by ccc. The primary purpose for NFC and NFD are to provide the ability to compare strings of characters for equality, but one might consider using them for rendering.

Unfortunately neither of these prove adequate for rendering (for reasons, see the first link in the next section). That leaves us with inventing a bespoke order that does work for rendering, getting it standardized and approved, and then convincing the world to use it.

## UTR53 and AMTRA

To that end, in 2018, Unicode approved [Unicode Technical Report #53](https://www.unicode.org/reports/tr53/), titled _Unicode Arabic Mark Rendering_, which provides a recommended solution to the combining mark rendering problem for Arabic script. The solution is in the form of an algorithm that rendering stacks can use to reorder Arabic combining marks in such a way that, when presented to a reasonably simple font, the correct display falls out naturally. 

The algorithm itself is called _Arabic Mark Transient Reordering Algorithm_, or _AMTRA_ for short, and it is essential that Arabic font developers understand what the algorithm does, and also what happens with rendering stacks that do not implement the algorithm. To that end, we encourage the reader to become familiar with UTR#53 at this point. The remainder of this document will assume familiarity with UTR53 as well as Unicode normalization as it applies to Arabic script combining marks.

## Status of UTR53 deployment

At the time of this writing, the biggest adopter of UTR53 is the [HarfBuzz text shaping engine](https://github.com/harfbuzz/harfbuzz), which means that applications using HarfBuzz (for example LibreOffice and Firefox) will present AMTRA-ordered Arabic texts to fonts for rendering. 

Well, nearly. The implementers of HarfBuzz have some disagreements with UTR53, which are discussed below.

Most non-HarfBuzz applications will use OS-provided rendering stacks, e.g., DirectWrite on Windows. Major exceptions are Microsoft Office and Adobe Creative Suite applications which each have their own rendering stacks. 

## Disgreement with UTR53

TBD.  See [harfbuzz#3179 "not decomposing arabic per UTR#53"](https://github.com/harfbuzz/harfbuzz/issues/3179)

The crux of the disagreement with Harfbuzz is whether U+0653 ARABIC MADDAH ABOVE (madda) should be a Modifier Combining Mark (MCM) or not. Khaled Hosney argues that madda is a form of hamza and, like hamza, should be MCM. However, Roozbeh Pournader had written earlier that, when used with other vowel marks above, the madda should be written above the vowels, and that's the way UTR53 was written.  Whether any of this can be rectified at this time is unclear.

## SIL Implementation

At this point SIL fonts are designed to position the maddah above other vowels using the following steps:

Step 1: Decompose U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE  (along with U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE and U+0625 ARABIC LETTER ALEF WITH HAMZA BELOW)
```
lookup DecomposeForColor {
  lookupflag IgnoreMarks ;
    sub @AlefPlusMark by alef-ar @AlefMark ;
} DecomposeForColor;
```

This also has the benefit of giving applications like Word, which can color diacritics, the opportunity to color madda or hamza marks even when they appear as part of composite characters, thus the name of the feature.

Step 2: If there is a combining mark with 0 < ccc < 230 immediately after the madda, swap the madda and that mark using a pair of contextual lookups:

```
@MaddaSkip = [ @UTR53_shadda @UTR53_fixedPos @UTR53_alef @UTR53_220MCM @UTR53_220other ] ;

lookup _ReorderMaddaVowel1 {
  lookupflag 0 ;
    sub @MaddaSkip  by  @MaddaSkip  @MaddaInsert ;
} _ReorderMaddaVowel1 ;

lookup ReorderMaddaVowel1 {
  lookupflag 0 ;
    sub @MaddaPlain  @MaddaSkip' lookup _ReorderMaddaVowel1 ;
} ReorderMaddaVowel1;

lookup _ReorderMaddaVowel2 {
  lookupflag 0 ;
    sub @MaddaPlain  @MaddaSkip by @MaddaSkip ;
} _ReorderMaddaVowel2 ;

lookup ReorderMaddaVowel2 {
  lookupflag 0 ;
    sub @MaddaPlain' lookup _ReorderMaddaVowel2  @MaddaSkip  @MaddaInsert ;
} ReorderMaddaVowel2;
```

This has the effect of gradually moving the madda past any arabic combining mark except another ccc=230 (or a ccc=0 such as CGJ). This is essentially what UTR53 properly implemented would have done.

