---
title: Ligatures and ZWJ
---

For most scripts, originally including Arabic script, the ZERO WIDTH JOINER (ZWJ) is intended to increase the connectedness of adjacent glyphs. The following summary has been in The Unicode Standard (TUS) essentially unchanged since Version 3.1, but is here quoted from Version 14.0, Section 23.2:

>In other words, given the three broad categories
below, ZWJ requests that glyphs in the highest available category (for the given font) be
used:<br/>
    1. Ligated<br/>
    2. Cursively connected<br/>
    3. Unconnected[[1](#1)]

However, due to a number of issues, this rule does not apply to Arabic script. All versions of TUS since 4.0 have included this exception to the above rule:

>For backward compatibility, between Arabic characters a ZWJ acts just like the sequence <ZWJ, ZWNJ, ZWJ>, preventing a ligature from forming instead of requesting the use of a ligature that would not normally be used. **As a result, there is no plain text mechanism for requesting the use of a ligature in Arabic text.**[[2](#2)] [emphasis added]


For Arabic script fonts, therefore, it is inappropriate for font developers to attempt to devise plain-text mechanisms for authors to request optional ligature formation.

Instead, font developers should consider adding the [Discretionary Ligature (dlig)](https://docs.microsoft.com/en-us/typography/opentype/spec/features_ae#tag-dlig) feature to their OpenType or Graphite font logic, thus allowing applications to access optional ligatures through document markup/formatting. 

For those who want to do some research, you might look at:

* [https://www.unicode.org/L2/L2000/00023.txt](http://www.unicode.org/L2/L2000/00023.txt) for the reasons why ligature encouragement was added to the function of ZWJ
* [https://www.unicode.org/L2/L2002/02363-nelson-zwj-zwnj.pdf](http://www.unicode.org/L2/L2002/02363-nelson-zwj-zwnj.pdf) for reasons the exception for Arabic script was added in TUS 14.0

----

<a name="1">1</a> The Unicode Consortium. The Unicode Standard, Version 14.0.0, (Mountain View, CA: The Unicode Consortium, 2021. ISBN 978-1-936213-29-0), [pg 906](https://www.unicode.org/versions/Unicode14.0.0/ch23.pdf#page=9).

<a name="2">2</a> ibid., [pg 908](https://www.unicode.org/versions/Unicode14.0.0/ch23.pdf#page=11).
