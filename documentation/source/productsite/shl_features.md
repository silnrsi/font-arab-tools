
Scheherazade New, Harmattan and Lateef are OpenType-enabled font families that support the Arabic script. They include a number of optional features that provide alternative rendering that might be preferable for use in some contexts. The sections below enumerate the details of these features. Some of the features have different default settings or the feature may only be implemented in one or two of the fonts. Whether these features are available to users will depend on both the application and the rendering technology being used. Some applications let the user control certain features such as Character Variants to turn on the rendering of variant characters. However, at this point, most applications do not make use of those features so another solution is needed to show the variant characters. [TypeTuner](http://scripts.sil.org/ttw/fonts2go.cgi) creates tuned fonts that use the variant glyph in place of the standard glyph. TypeTuner also provides the ability to turn on support for the Kurdish, Kyrgyz, Rohingya, Sindhi, Urdu, and Wolof language variants.

See [Using Font Features](https://software.sil.org/fonts/features/). Although that page is not targeted at Arabic script support, it does provide a comprehensive list of applications that make full use of the OpenType font technology.

See also [Arabic Fonts — Application Support](http://software.sil.org/arabicfonts/support/application-support/). It provides a fairly comprehensive list of applications that make full use of the OpenType font technology.

This page uses web fonts (WOFF) to demonstrate font features and should display correctly in all modern browsers. 

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## End of Ayah (U+06DD), Disputed End of Ayah (U+08E2), and subtending marks (U+0600..U+0605, U+0890..U+0891)

These Arabic characters are intended to enclose or hold one or more digits. 

Specific technical details of how to use them are discussed in the [Arabic fonts FAQ -- Subtending marks](http://software.sil.org/arabicfonts/support/faq#Ayah).

Additionally, all three fonts include two simplified alternates for U+06DD ARABIC END OF AYAH under the Stylistic Alternates (salt) feature, but at this time we know of no OpenType-based applications that can access these. The two alternates are also available through the Character Variants feature discussed below.

## Customizing with TypeTuner

For applications that do not make use of the OpenType Character Variants, you can now download fonts customized with the variant glyphs you choose. Read this document, visit [TypeTuner Web](http://scripts.sil.org/ttw/fonts2go.cgi), then choose the variants and download your font.


### Language 

<span class='affects'>Affects: U+062F, U+0630, U+0688..U+068F, U+0690, U+06EE, U+0759, U+075A, U+08AE, U+0645, U+0765, U+0766, U+08A7, U+06BE, U+0626, U+06F4, U+06F5, U+06F6, U+06F7, U+0650, U+064F, U+064C, U+0657</span>

Unfortunately, the UI needed to access the language-specific behavior is not yet present in many applications. LibreOffice and Microsoft Word 2016 support language-specific behavior for Kurdish, Sindhi and Urdu (but not Kyrgyz, Rohingya or Wolof). Some Harfbuzz-based apps, e.g., XeTeX, can access language-specific behavior.

#### Scheherazade New

##### Kurdish (Northern), Rohingya, Sindhi, Urdu

Language | Meem | Heh Doachashmee (06BE) | 4 | 6 | 7 | 0650/064E | 064C | Feature Setting
-- | ---: | ----: | -: | -: | -: | --: | --: | ---
default | <span dir="rtl" class='scheherazadenew-R normal'>&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='scheherazadenew-R normal' >&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='scheherazadenew-R normal'>&#x06F4;</span> |<span dir="rtl" class='scheherazadenew-R normal'>&#x06F6;</span> | <span dir="rtl" class='scheherazadenew-R normal'>&#x06F7;</span> | <span dir="rtl" class='scheherazadenew-R normal'>&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='scheherazadenew-R normal'>&#x0628;&#x064C;</span> |
Kurdish</br>(Northern) | <span dir="rtl" class='scheherazadenew-R normal' lang='ku'>&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ku' style="color:red">&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ku'>&#x06F4;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ku'>&#x06F6;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ku'>&#x06F7;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ku'>&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ku'>&#x0628;&#x064C;</span> |  `lang='ku'`
Rohingya | <span dir="rtl" class='scheherazadenew-R normal' lang='rhg'>&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='rhg'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='rhg' style="color:red">&#x06F4;</span> | <span dir="rtl" class='scheherazadenew-R small' lang='rhg' style="color:red">&#x06F6;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='rhg' style="color:red">&#x06F7;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='rhg' style="color:red">&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='rhg' style="color:red">&#x0628;&#x064C;</span>| `lang='rhg'`
Sindhi | <span dir="rtl" class='scheherazadenew-R normal' lang='sd' style="color:red">&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='sd'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='sd'>&#x06F4;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='sd' style="color:red">&#x06F6;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='sd' style="color:red">&#x06F7;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='sd' style="color:red">&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='sd'>&#x0628;&#x064C;</span> | `lang='sd'`
Urdu | <span dir="rtl" class='scheherazadenew-R normal' lang='ur'>&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ur'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ur' style="color:red">&#x06F4;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ur' style="color:red">&#x06F6;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ur' style="color:red">&#x06F7;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ur' style="color:red">&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ur'>&#x0628;&#x064C;</span> | `lang='ur'`

##### Kyrgyz and Wolof

Language | Dal  | 0626 | 0650/064E | 064F | 0657 | Feature Setting
-- | -: |  ---: | --: | --: | --: | ---
default | <span dir="rtl" class='scheherazadenew-R normal'> &#x062F;</span> | <span dir="rtl" class='scheherazadenew-R normal'>&#x0626;&#x0020;&#x0626;&#x0626;&#x0626;</span> | <span dir="rtl" class='scheherazadenew-R normal'>&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='scheherazadenew-R normal'>&#x0628;&#x064F;</span> | <span dir="rtl" class='scheherazadenew-R normal'>&#x0628;&#x0657;</span>|
Kyrgyz | <span dir="rtl" class='scheherazadenew-R normal' lang='ky'> &#x062F;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ky' style="color:red">&#x0626;&#x0020;&#x0626;&#x0626;&#x0626;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ky'>&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ky'>&#x0628;&#x064F;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='ky'>&#x0628;&#x0657;</span>| `lang='ky'`
Wolof | <span dir="rtl" class='scheherazadenew-R normal' lang='wo' style="color:red"> &#x062F;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='wo'>&#x0626;&#x0020;&#x0626;&#x0626;&#x0626;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='wo' style="color:red">&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='wo' style="color:red">&#x0628;&#x064F;</span> | <span dir="rtl" class='scheherazadenew-R normal' lang='wo' style="color:red">&#x0628;&#x0657;</span>| `lang='wo'`

#### Harmattan

##### Kurdish (Northern), Rohingya, Sindhi, Urdu

Language | Meem | Heh Doachashmee (06BE) | 4 | 6 | 7 | 0650/064E | 064C | Feature Setting
-- | ---: | ----: | -: | -: | -: | --: | --: | ---
default | <span dir="rtl" class='harmattan-R normal'>&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='harmattan-R normal' >&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='harmattan-R normal'>&#x06F4;</span> |<span dir="rtl" class='harmattan-R normal'>&#x06F6;</span> | <span dir="rtl" class='harmattan-R normal'>&#x06F7;</span> | <span dir="rtl" class='harmattan-R normal'>&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='harmattan-R normal'>&#x0628;&#x064C;</span> |
Kurdish</br>(Northern) | <span dir="rtl" class='harmattan-R normal' lang='ku'>&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='harmattan-R normal' lang='ku' style="color:red">&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='harmattan-R normal' lang='ku'>&#x06F4;</span> | <span dir="rtl" class='harmattan-R normal' lang='ku'>&#x06F6;</span> | <span dir="rtl" class='harmattan-R normal' lang='ku'>&#x06F7;</span> | <span dir="rtl" class='harmattan-R normal' lang='ku'>&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='harmattan-R normal' lang='ku'>&#x0628;&#x064C;</span> |  `lang='ku'`
Rohingya | <span dir="rtl" class='harmattan-R normal' lang='rhg'>&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='harmattan-R normal' lang='rhg'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='harmattan-R normal' lang='rhg' style="color:red">&#x06F4;</span> | <span dir="rtl" class='harmattan-R small' lang='rhg' style="color:red">&#x06F6;</span> | <span dir="rtl" class='harmattan-R normal' lang='rhg' style="color:red">&#x06F7;</span> | <span dir="rtl" class='harmattan-R normal' lang='rhg' style="color:red">&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='harmattan-R normal' lang='rhg' style="color:red">&#x0628;&#x064C;</span>| `lang='rhg'`
Sindhi | <span dir="rtl" class='harmattan-R normal' lang='sd' style="color:red">&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='harmattan-R normal' lang='sd'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='harmattan-R normal' lang='sd'>&#x06F4;</span> | <span dir="rtl" class='harmattan-R normal' lang='sd' style="color:red">&#x06F6;</span> | <span dir="rtl" class='harmattan-R normal' lang='sd' style="color:red">&#x06F7;</span> | <span dir="rtl" class='harmattan-R normal' lang='sd' style="color:red">&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='harmattan-R normal' lang='sd'>&#x0628;&#x064C;</span> | `lang='sd'`
Urdu | <span dir="rtl" class='harmattan-R normal' lang='ur'>&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='harmattan-R normal' lang='ur'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='harmattan-R normal' lang='ur' style="color:red">&#x06F4;</span> | <span dir="rtl" class='harmattan-R normal' lang='ur' style="color:red">&#x06F6;</span> | <span dir="rtl" class='harmattan-R normal' lang='ur' style="color:red">&#x06F7;</span> | <span dir="rtl" class='harmattan-R normal' lang='ur' style="color:red">&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='harmattan-R normal' lang='ur'>&#x0628;&#x064C;</span> | `lang='ur'`

##### Kyrgyz and Wolof

Language | Dal  | 0626 | 0650/064E | 064F | 0657 | Feature Setting
-- | -: |  ---: | --: | --: | --: | ---
default | <span dir="rtl" class='harmattan-R normal'> &#x062F;</span> | <span dir="rtl" class='harmattan-R normal'>&#x0626;&#x0020;&#x0626;&#x0626;&#x0626;</span> | <span dir="rtl" class='harmattan-R normal'>&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='harmattan-R normal'>&#x0628;&#x064F;</span> | <span dir="rtl" class='harmattan-R normal'>&#x0628;&#x0657;</span>|
Kyrgyz | <span dir="rtl" class='harmattan-R normal' lang='ky'> &#x062F;</span> | <span dir="rtl" class='harmattan-R normal' lang='ky' style="color:red">&#x0626;&#x0020;&#x0626;&#x0626;&#x0626;</span> | <span dir="rtl" class='harmattan-R normal' lang='ky'>&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='harmattan-R normal' lang='ky'>&#x0628;&#x064F;</span> | <span dir="rtl" class='harmattan-R normal' lang='ky'>&#x0628;&#x0657;</span>| `lang='ky'`
Wolof | <span dir="rtl" class='harmattan-R normal' lang='wo' style="color:red"> &#x062F;</span> | <span dir="rtl" class='harmattan-R normal' lang='wo'>&#x0626;&#x0020;&#x0626;&#x0626;&#x0626;</span> | <span dir="rtl" class='harmattan-R normal' lang='wo' style="color:red">&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='harmattan-R normal' lang='wo' style="color:red">&#x0628;&#x064F;</span> | <span dir="rtl" class='harmattan-R normal' lang='wo' style="color:red">&#x0628;&#x0657;</span>| `lang='wo'`

#### Lateef

##### Kurdish (Northern), Rohingya, Sindhi, Urdu

Language | Meem | Heh Doachashmee (06BE) | 4 | 6 | 7 | 0650/064E | 064C | Feature Setting
-- | ---: | ----: | -: | -: | -: | --: | --: | ---
default | <span dir="rtl" class='lateef-R normal'>&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='lateef-R normal' >&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='lateef-R normal'>&#x06F4;</span> |<span dir="rtl" class='lateef-R normal'>&#x06F6;</span> | <span dir="rtl" class='lateef-R normal'>&#x06F7;</span> | <span dir="rtl" class='lateef-R normal'>&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='lateef-R normal'>&#x0628;&#x064C;</span> |
Kurdish</br>(Northern) | <span dir="rtl" class='lateef-R normal' lang='ku'>&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='lateef-R normal' lang='ku' style="color:red">&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='lateef-R normal' lang='ku'>&#x06F4;</span> | <span dir="rtl" class='lateef-R normal' lang='ku'>&#x06F6;</span> | <span dir="rtl" class='lateef-R normal' lang='ku'>&#x06F7;</span> | <span dir="rtl" class='lateef-R normal' lang='ku'>&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='lateef-R normal' lang='ku'>&#x0628;&#x064C;</span> |  `lang='ku'`
Rohingya | <span dir="rtl" class='lateef-R normal' lang='rhg'>&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='lateef-R normal' lang='rhg'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='lateef-R normal' lang='rhg' style="color:red">&#x06F4;</span> | <span dir="rtl" class='lateef-R small' lang='rhg' style="color:red">&#x06F6;</span> | <span dir="rtl" class='lateef-R normal' lang='rhg' style="color:red">&#x06F7;</span> | <span dir="rtl" class='lateef-R normal' lang='rhg' style="color:red">&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='lateef-R normal' lang='rhg' style="color:red">&#x0628;&#x064C;</span>| `lang='rhg'`
Sindhi | <span dir="rtl" class='lateef-R normal' lang='sd' style="color:red">&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='lateef-R normal' lang='sd'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='lateef-R normal' lang='sd'>&#x06F4;</span> | <span dir="rtl" class='lateef-R normal' lang='sd' style="color:red">&#x06F6;</span> | <span dir="rtl" class='lateef-R normal' lang='sd' style="color:red">&#x06F7;</span> | <span dir="rtl" class='lateef-R normal' lang='sd' style="color:red">&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='lateef-R normal' lang='sd'>&#x0628;&#x064C;</span> | `lang='sd'`
Urdu | <span dir="rtl" class='lateef-R normal' lang='ur'>&#x0645;&#x0020;&#x0645;&#x0645;&#x0645;</span> | <span dir="rtl" class='lateef-R normal' lang='ur'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span> | <span dir="rtl" class='lateef-R normal' lang='ur' style="color:red">&#x06F4;</span> | <span dir="rtl" class='lateef-R normal' lang='ur' style="color:red">&#x06F6;</span> | <span dir="rtl" class='lateef-R normal' lang='ur' style="color:red">&#x06F7;</span> | <span dir="rtl" class='lateef-R normal' lang='ur' style="color:red">&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='lateef-R normal' lang='ur'>&#x0628;&#x064C;</span> | `lang='ur'`

##### Kyrgyz and Wolof

Language | Dal  | 0626 | 0650/064E | 064F | 0657 | Feature Setting
-- | -: |  ---: | --: | --: | --: | ---
default | <span dir="rtl" class='lateef-R normal'> &#x062F;</span> | <span dir="rtl" class='lateef-R normal'>&#x0626;&#x0020;&#x0626;&#x0626;&#x0626;</span> | <span dir="rtl" class='lateef-R normal'>&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='lateef-R normal'>&#x0628;&#x064F;</span> | <span dir="rtl" class='lateef-R normal'>&#x0628;&#x0657;</span>|
Kyrgyz | <span dir="rtl" class='lateef-R normal' lang='ky'> &#x062F;</span> | <span dir="rtl" class='lateef-R normal' lang='ky' style="color:red">&#x0626;&#x0020;&#x0626;&#x0626;&#x0626;</span> | <span dir="rtl" class='lateef-R normal' lang='ky'>&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='lateef-R normal' lang='ky'>&#x0628;&#x064F;</span> | <span dir="rtl" class='lateef-R normal' lang='ky'>&#x0628;&#x0657;</span>| `lang='ky'`
Wolof | <span dir="rtl" class='lateef-R normal' lang='wo' style="color:red"> &#x062F;</span> | <span dir="rtl" class='lateef-R normal' lang='wo'>&#x0626;&#x0020;&#x0626;&#x0626;&#x0626;</span> | <span dir="rtl" class='lateef-R normal' lang='wo' style="color:red">&#x0628;&#x0651;&#x0650;</span> | <span dir="rtl" class='lateef-R normal' lang='wo' style="color:red">&#x0628;&#x064F;</span> | <span dir="rtl" class='lateef-R normal' lang='wo' style="color:red">&#x0628;&#x0657;</span>| `lang='wo'`

### Character variants

There are some character shape differences in different languages which use the Arabic script. These can be accessed by using OpenType Character Variants, or through the language support mentioned above.

#### Jeem/Hah 

<span class='affects'>Affects: U+062C, U+062D, U+062E, U+0682, U+0683, U+0684, U+0685, U+0686, U+06BF, U+0757, U+0758, U+088A, U+08A2, U+08C1, U+08C5, U+08C6</span>

Feature   | Scheherazade New | Harmattan  | Lateef     | Feature setting
:-------- | ---------:       | ---------: | ---------: | :------------- 
Standard    | <span dir="rtl" class='scheherazadenew-R normal'>&#x062C;&#x0020;&#x062C;&#x062C;&#x062C;&#x0020;&#x062D;&#x0020;&#x062d;&#x062d;&#x062d; &#x062E;&#x0020;&#x062e;&#x062e;&#x062e; &#x0682;&#x0020;&#x0682;&#x0682;&#x0682; &#x0683;&#x0020;&#x0683;&#x0683;&#x0683; &#x0684;&#x0020;&#x0684;&#x0684;&#x0684; &#x0685;&#x0020;&#x0685;&#x0685;&#x0685; &#x0686;&#x0020;&#x0686;&#x0686;&#x0686; &#x06bf;&#x0020;&#x06bf;&#x06bf;&#x06bf; &#x0757;&#x0020;&#x0757;&#x0757;&#x0757; &#x0758;&#x0020;&#x0758;&#x0758;&#x0758; &#x088a;&#x0020;&#x088a;&#x088a;&#x088a; &#x08a2;&#x0020;&#x08a2;&#x08a2;&#x08a2; &#x08c1;&#x0020;&#x08c1;&#x08c1;&#x08c1; &#x08c5;&#x0020;&#x08c5;&#x08c5;&#x08c5; &#x08c6;&#x0020;&#x08c6;&#x08c6;&#x08c6; </span>|<span dir="rtl" class='harmattan-R normal'>&#x062C;&#x0020;&#x062C;&#x062C;&#x062C;&#x0020;&#x062D;&#x0020;&#x062d;&#x062d;&#x062d; &#x062E;&#x0020;&#x062e;&#x062e;&#x062e; &#x0682;&#x0020;&#x0682;&#x0682;&#x0682; &#x0683;&#x0020;&#x0683;&#x0683;&#x0683; &#x0684;&#x0020;&#x0684;&#x0684;&#x0684; &#x0685;&#x0020;&#x0685;&#x0685;&#x0685; &#x0686;&#x0020;&#x0686;&#x0686;&#x0686; &#x06bf;&#x0020;&#x06bf;&#x06bf;&#x06bf; &#x0757;&#x0020;&#x0757;&#x0757;&#x0757; &#x0758;&#x0020;&#x0758;&#x0758;&#x0758; &#x088a;&#x0020;&#x088a;&#x088a;&#x088a; &#x08a2;&#x0020;&#x08a2;&#x08a2;&#x08a2; &#x08c1;&#x0020;&#x08c1;&#x08c1;&#x08c1; &#x08c5;&#x0020;&#x08c5;&#x08c5;&#x08c5; &#x08c6;&#x0020;&#x08c6;&#x08c6;&#x08c6; </span>|<span dir="rtl" class='lateef-R normal'>&#x062C;&#x0020;&#x062C;&#x062C;&#x062C;&#x0020;&#x062D;&#x0020;&#x062d;&#x062d;&#x062d; &#x062E;&#x0020;&#x062e;&#x062e;&#x062e; &#x0682;&#x0020;&#x0682;&#x0682;&#x0682; &#x0683;&#x0020;&#x0683;&#x0683;&#x0683; &#x0684;&#x0020;&#x0684;&#x0684;&#x0684; &#x0685;&#x0020;&#x0685;&#x0685;&#x0685; &#x0686;&#x0020;&#x0686;&#x0686;&#x0686; &#x06bf;&#x0020;&#x06bf;&#x06bf;&#x06bf; &#x0757;&#x0020;&#x0757;&#x0757;&#x0757; &#x0758;&#x0020;&#x0758;&#x0758;&#x0758; &#x088a;&#x0020;&#x088a;&#x088a;&#x088a; &#x08a2;&#x0020;&#x08a2;&#x08a2;&#x08a2; &#x08c1;&#x0020;&#x08c1;&#x08c1;&#x08c1; &#x08c5;&#x0020;&#x08c5;&#x08c5;&#x08c5; &#x08c6;&#x0020;&#x08c6;&#x08c6;&#x08c6; </span>| `cv08=0`
Handwritten | N/A | <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv08" 1'>&#x062C;&#x0020;&#x062C;&#x062C;&#x062C;&#x0020;&#x062D;&#x0020;&#x062d;&#x062d;&#x062d; &#x062E;&#x0020;&#x062e;&#x062e;&#x062e; &#x0682;&#x0020;&#x0682;&#x0682;&#x0682; &#x0683;&#x0020;&#x0683;&#x0683;&#x0683; &#x0684;&#x0020;&#x0684;&#x0684;&#x0684; &#x0685;&#x0020;&#x0685;&#x0685;&#x0685; &#x0686;&#x0020;&#x0686;&#x0686;&#x0686; &#x06bf;&#x0020;&#x06bf;&#x06bf;&#x06bf; &#x0757;&#x0020;&#x0757;&#x0757;&#x0757; &#x0758;&#x0020;&#x0758;&#x0758;&#x0758; &#x088a;&#x0020;&#x088a;&#x088a;&#x088a; &#x08a2;&#x0020;&#x08a2;&#x08a2;&#x08a2; &#x08c1;&#x0020;&#x08c1;&#x08c1;&#x08c1; &#x08c5;&#x0020;&#x08c5;&#x08c5;&#x08c5; &#x08c6;&#x0020;&#x08c6;&#x08c6;&#x08c6; </span>| N/A | `cv08=1`

#### Dal 

<span class='affects'>Affects: U+062F, U+0630, U+0688, U+0689, U+068A, U+068B, U+068C, U+068D, U+068E, U+068F, U+0690, U+06EE, U+0759, U+075A, U+08AE</span>

Feature   | Scheherazade New | Harmattan  | Lateef     | Feature setting
:-------- | ---------:       | ---------: | ---------: | :------------- 
Standard  | <span dir="rtl" class='scheherazadenew-R normal'> د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ </span>| <span dir="rtl" class='harmattan-R normal'> د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ </span>| <span dir="rtl" class='lateef-R normal'> د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ </span> | `cv12=0`
Alternate | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv12" 1'> د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ </span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv12" 1'> د ذ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ۮ ݙ ݚ ࢮ </span>| N/A | `cv12=1`

#### Sad/Dad 

<span class='affects'>Affects: U+0635, U+0636, U+069D, U+069E, U+06FB, U+08AF</span>

Feature   | Scheherazade New | Harmattan  | Lateef     | Feature setting
:-------- | ---------:       | ---------: | ---------: | :------------- 
Standard | <span dir="rtl" class='scheherazadenew-R normal'>ص صصص ض ضضض ڝ ڝڝڝ ڞ ڞڞڞ ࢯࢯࢯ ࢯ ۻ ۻۻۻ</span>|<span dir="rtl" class='harmattan-R normal'>ص صصص ض ضضض ڝ ڝڝڝ ڞ ڞڞڞ ࢯࢯࢯ ࢯ ۻ ۻۻۻ</span>|<span dir="rtl" class='lateef-R normal'>ص صصص ض ضضض ڝ ڝڝڝ ڞ ڞڞڞ ࢯࢯࢯ ࢯ ۻ ۻۻۻ</span>| `cv20=0`
Half     | N/A |<span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv20" 1'>ص صصص ض ضضض ڝ ڝڝڝ ڞ ڞڞڞ ࢯࢯࢯ ࢯ ۻ ۻۻۻ</span>| N/A | `cv20=1`

#### Meem 

<span class='affects'>Affects: U+0645, U+0765, U+0766, U+08A7</span>

Feature      | Scheherazade New | Harmattan | Lateef | Feature setting
:--------    | ---------: | ---------: | ---------: | :------------- 
Standard     | <span dir="rtl" class='scheherazadenew-R normal'> م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ </span>                                        | <span dir="rtl" class='harmattan-R normal'> م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ </span> |<span dir="rtl" class='lateef-R normal'> م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ </span>| `cv44=0`
Sindhi-style | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv44" 1'> م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ </span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv44" 1'> م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ </span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv44" 1'> م ممم ݥ ݥݥݥ ݦ ݦݦݦ ࢧ ࢧࢧࢧ </span>| `cv44=1`


#### Heh 

<span class='affects'>Affects: U+0647</span>

Feature       | Scheherazade New | Harmattan  | Lateef     | Feature setting
:--------     | ---------:       | ---------: | ---------: | :------------- 
Standard      | <span dir="rtl" class='scheherazadenew-R normal'> ه ههه </span>                                        | <span dir="rtl" class='harmattan-R normal'> ه ههه </span>                                        | <span dir="rtl" class='lateef-R normal'> ه ههه </span>                                        | `cv48=0`
Kurdish-style | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv48" 3'> ه ههه </span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv48" 3'> ه ههه </span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv48" 3'> ه ههه </span>| `cv48=3`
Sindhi-style  | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv48" 1'> ه ههه </span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv48" 1'> ه ههه </span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv48" 1'> ه ههه </span>| `cv48=1`
Urdu-style    | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv48" 2'> ه ههه </span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv48" 2'> ه ههه </span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv48" 2'> ه ههه </span>| `cv48=2`

#### Heh Doachashmee 

<span class='affects'>Affects: U+06BE</span>

Feature       | Scheherazade New | Harmattan | Lateef | Feature setting
:--------     | ---------: | ---------: | ---------: | :------------- 
Standard      | <span dir="rtl" class='scheherazadenew-R normal'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span>                                        | <span dir="rtl" class='harmattan-R normal'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span>                                        | <span dir="rtl" class='lateef-R normal'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span>                                        |   `cv49=0`
Knotted-style | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv49" 1'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv49" 1'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv49" 1'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span>|   `cv49=1`
Kurdish-style | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv49" 3'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv49" 3'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv49" 3'>&#x06be;&#x0020;&#x06be;&#x06be;&#x06be;</span>|   `cv49=3`

#### Kirghiz OE 

<span class='affects'>Affects: U+06C5</span>

Feature   | Scheherazade New | Harmattan  | Lateef     | Feature setting
:-------- | ---------:       | ---------: | ---------: | :------------- 
Loop      | <span dir="rtl" class='scheherazadenew-R normal'>ۅ</span>                                        | <span dir="rtl" class='harmattan-R normal'>ۅ</span>                                        | <span dir="rtl" class='lateef-R normal'>ۅ</span>                                        |   `cv51=0`
Bar       | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv51" 1'>ۅ</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv51" 1'>ۅ</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv51" 1'>ۅ</span>|   `cv51=1`

#### Yeh Hamza 

<span class='affects'>Affects: U+0626</span>

Feature     | Scheherazade New | Harmattan | Lateef | Feature setting
:--------   | ---------: | ---------: | ---------: | :------------- 
Standard    | <span dir="rtl" class='scheherazadenew-R normal'>ئ ‍ئ</span>                                        | <span dir="rtl" class='harmattan-R normal'>ئ ‍ئ</span>                                        | <span dir="rtl" class='lateef-R normal'>ئ ‍ئ</span>                                        |   `cv54=0`
Right hamza | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv54" 1'>ئ ‍ئ</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv54" 1'>ئ ‍ئ</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv54" 1'>ئ ‍ئ</span>|   `cv54=1`

#### Maddah 

<span class='affects'>Affects: U+0622, U+0627, U+0653, U+0653</span>

Feature   | Scheherazade New | Harmattan | Lateef | Feature setting
:-------- | ---------: | ---------: | ---------: | :------------- 
Small     | <span dir="rtl" class='scheherazadenew-R normal'> آ آ ◌ٓ </span>                                       | <span dir="rtl" class='harmattan-R normal'> آ آ ◌ٓ </span>     |  <span dir="rtl" class='lateef-R normal'> آ آ ◌ٓ </span> | `cv60=0`
Large     | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv60" 1'>آ آ ◌ٓ </span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv60" 1'>آ آ ◌ٓ </span>| N/A | `cv60=1`


#### Shadda+kasra placement 

<span class='affects'>Affects: U+064D, U+0650 with U+0651</span>

Feature   | Scheherazade New | Harmattan | Lateef | Feature setting
:-------- | ---------: | ---------: | ---------: | :------------- 
Default   | <span dir="rtl" class='scheherazadenew-R normal'> بِّ ◌ِّ بٍّ ◌ٍّ </span>  | <span dir="rtl" class='harmattan-R normal'> بِّ ◌ِّ بٍّ ◌ٍّ </span>|<span dir="rtl" class='lateef-R normal'> بِّ ◌ِّ بٍّ ◌ٍّ </span> | `cv62=0`
Lowered   | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv62" 1'> بِّ ◌ِّ بٍّ ◌ٍّ </span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv62" 1'> بِّ ◌ِّ بٍّ ◌ٍّ </span> | <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv62" 1'> بِّ ◌ِّ بٍّ ◌ٍّ </span> | `cv62=1`
Raised    | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv62" 2'> بِّ ◌ِّ بٍّ ◌ٍّ </span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv62" 2'> بِّ ◌ِّ بٍّ ◌ٍّ </span> | <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv62" 2'> بِّ ◌ِّ بٍّ ◌ٍّ </span> | `cv62=2`

#### Damma 

<span class='affects'>Affects: U+064F</span>

Feature   | Scheherazade New | Harmattan | Lateef | Feature setting
:-------- | ---------: | ---------: | ---------: | :------------- 
Default  | <span dir="rtl" class='scheherazadenew-R normal'> بُ ◌ُ</span>                                       | <span dir="rtl" class='harmattan-R normal'> بُ ◌ُ</span>                                       | <span dir="rtl" class='lateef-R normal'> بُ ◌ُ</span>                                       | `cv70=0`
Filled    | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv70" 1'>بُ ◌ُ</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv70" 1'>بُ ◌ُ</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv70" 1'>بُ ◌ُ</span>| `cv70=1`
Short     | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv70" 2'>بُ ◌ُ</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv70" 2'>بُ ◌ُ</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv70" 2'>بُ ◌ُ</span>| `cv70=2`

#### Dammatan 

<span class='affects'>Affects: U+064C</span>

Feature   | Scheherazade New | Harmattan | Lateef | Feature setting
:-------- | ---------: | ---------: | ---------: | :------------- 
Standard  | <span dir="rtl" class='scheherazadenew-R normal'>بٌ ◌ٌ</span>                                        | <span dir="rtl" class='harmattan-R normal'>بٌ ◌ٌ</span>                                        | <span dir="rtl" class='lateef-R normal'>بٌ ◌ٌ</span>                                        | `cv72=0`
Six-nine  | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv72" 1'>بٌ ◌ٌ</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv72" 1'>بٌ ◌ٌ</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv72" 1'>بٌ ◌ٌ</span>| `cv72=1`

#### Inverted Damma 

<span class='affects'>Affects: U+0657</span>

Feature   | Scheherazade New | Harmattan  | Lateef     | Feature setting
:-------- | ---------:       | ---------: | ---------: | :------------- 
Default   | <span dir="rtl" class='scheherazadenew-R normal'>بٗ ◌ٗ</span>                                        | <span dir="rtl" class='harmattan-R normal'>بٗ ◌ٗ</span>                                        | <span dir="rtl" class='lateef-R normal'>بٗ ◌ٗ</span>                                        | `cv74=0`
Hollow    | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv74" 1'>بٗ ◌ٗ</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv74" 1'>بٗ ◌ٗ</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv74" 1'>بٗ ◌ٗ</span>| `cv74=1`
Filled    | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv74" 2'>بٗ ◌ٗ</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv74" 2'>بٗ ◌ٗ</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv74" 2'>بٗ ◌ٗ</span>| `cv74=2`


#### Superscript Alef 

<span class='affects'>Affects: U+0670 on all yeh, sad and seen-like characters 
U+0649 U+064A U+06D0 U+06D1 U+0777 U+06CC U+0635 U+0636 U+069D U+069E U+06FB U+08AF U+0633 U+0634 U+069A U+069B U+069C U+06FA U+075C U+076D U+0770 U+077D U+077E</span>

Feature   | Scheherazade New | Harmattan  | Lateef     | Feature setting
:-------- | ---------:       | ---------: | ---------: | :------------- 
Default | <span dir="rtl" class='scheherazadenew-R normal'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span>                                        | <span dir="rtl" class='harmattan-R normal'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span> |<span dir="rtl" class='lateef-R normal'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span> | `cv76=0`
Large | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv76" 1'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span>|<span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv76" 1'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span> |<span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv76" 1'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span> | `cv76=1`
Small | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv76" 2'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span>|<span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv76" 2'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span> |<span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv76" 2'>ئٰ ئٰئٰئٰ ىٰ ىٰىٰىٰ يٰ يٰيٰيٰ ٸٰ ٸٰٸٰٸٰ ېٰ ېٰېٰېٰ ۑٰ ۑٰۑٰۑٰ ݷٰ ݷٰݷٰݷٰ ࢨٰ ࢨٰࢨٰࢨٰ ࢩٰ ࢩٰࢩٰࢩٰ ؽٰ ؽٰؽٰؽٰ ؾٰ ؾٰؾٰؾٰ ؿٰ ؿٰؿٰؿٰ یٰ یٰیٰیٰ ێٰ ێٰێٰێٰ ݵٰ ݵٰݵٰݵٰ ݶٰ ݶٰݶٰݶٰ صٰ صٰصٰصٰ ضٰ ضٰضٰضٰ ڝٰ ڝٰڝٰڝٰ ڞٰ ڞٰڞٰڞٰ ۻٰ ۻٰۻٰۻٰ ࢯٰ ࢯٰࢯٰࢯٰ سٰ سٰسٰسٰ شٰ شٰشٰشٰ ښٰ ښٰښٰښٰ ڛٰ ڛٰڛٰڛٰ ڜٰ ڜٰڜٰڜٰ ۺٰ ۺٰۺٰۺٰ ݜٰ ݜٰݜٰݜٰ ݭٰ ݭٰݭٰݭٰ ݰٰ ݰٰݰٰݰٰ ݽٰ ݽٰݽٰݽٰ ݾٰ ݾٰݾٰݾٰ </span> | `cv76=2`

#### Sukun 

<span class='affects'>Affects: U+0652</span>

Feature   | Scheherazade New | Harmattan | Lateef | Feature setting
:--------  | ---------: | ---------: | ---------: | :------------- 
Closed    | <span dir="rtl" class='scheherazadenew-R normal'>بْ ◌ْ</span>                                        | <span dir="rtl" class='harmattan-R normal'>بْ ◌ْ</span>                                        | <span dir="rtl" class='lateef-R normal'>بْ ◌ْ</span>                                        |   `cv78=0`
Open down | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv78" 1'>بْ ◌ْ</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv78" 1'>بْ ◌ْ</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv78" 1'>بْ ◌ْ</span>|   `cv78=1`
Open left | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv78" 2'>بْ ◌ْ</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv78" 2'>بْ ◌ْ</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv78" 2'>بْ ◌ْ</span>|   `cv78=2`

#### End of ayah 


<span class='affects'>Affects: U+06DD</span>

Firefox allows you to use U+06DD followed by the digits and proper rendering occurs. Some applications require the following:

* precede the entire sequence (subtending mark plus following digits) with
        202D LEFT-TO-RIGHT OVERRIDE
* follow the entire sequence with U+202C POP DIRECTIONAL FORMATTING.

Surrounding the sequence with U+202D and U+202C seems to give the most reliable results in different browsers. However, we have not found a solution that works in Internet Explorer/Edge.

In the example below, the following codepoints are used: U+202D U+06DD U+0031 U+0032 U+0033 U+202C U+202D U+06DD U+0611 U+0622 U+0663 U+202C.

Feature   | Scheherazade New | Harmattan | Lateef | Feature setting
:--------  | ---------: | ---------: | ---------: | :------------- 
Standard     | <span dir="rtl" class='scheherazadenew-R normal'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>                                        |<span dir="rtl" class='harmattan-R normal'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>                                        |<span dir="rtl" class='lateef-R normal'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>                                        | `cv80=0`
Simplified A | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv80" 1'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>|<span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv80" 1'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>|<span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv80" 1'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>| `cv80=1`
Simplified B | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv80" 2'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>|<span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv80" 2'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>|<span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv80" 2'>&#x202D;&#x6DD;&#x31;&#x32;&#x33;&#x202C; &#x202D;&#x6DD;&#x0661;&#x0662;&#x0663;&#x202C;</span>| `cv80=2`

The DISPUTED END OF AYAH (U+08E2) is also now available in the font. It works in the same way as End of ayah. 

<span dir="rtl" class='scheherazadenew-R normal'>&#x202D;&#x8E2;&#x663;&#x664;&#x665;&#x202C;</span> (Scheherazade New)

<span dir="rtl" class='harmattan-R normal'>&#x202D;&#x8E2;&#x663;&#x664;&#x665;&#x202C;</span> (Harmattan)

<span dir="rtl" class='lateef-R normal'>&#x202D;&#x8E2;&#x663;&#x664;&#x665;&#x202C;</span> (Lateef)

#### Honorific ligatures 

<span class='affects'>Affects: U+FD40..U+FD4F, U+FDCF, U+FDFA..U+FDFB, U+FDFD..U+FDFF</span>

Feature | Scheherazade New | Feature setting
:------------- | ---------------: | :------------- 
Calligraphic | <span dir="rtl" class='scheherazadenew-R normal'>&#xFD40;&#xFD41;&#xFD42;&#xFD43;&#xFD44;&#xFD45;&#xFD46;&#xFD47;&#xFD48;&#xFD49;&#xFD4A;&#xFD4B;&#xFD4C;&#xFD4D;&#xFD4E;&#xFD4F;</br>&#xFDCF;&#xFDFA;&#xFDFB;&#xFDFD;&#xFDFF;&#xFDFF;</span> | `cv81=0`
Simplified | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv81" 1'>&#xFD40;&#xFD41;&#xFD42;&#xFD43;&#xFD44;&#xFD45;&#xFD46;&#xFD47;&#xFD48;&#xFD49;&#xFD4A;&#xFD4B;&#xFD4C;&#xFD4D;&#xFD4E;&#xFD4F;</br>&#xFDCF;&#xFDFA;&#xFDFB;&#xFDFD;&#xFDFF;&#xFDFF;</span>| `cv81=1`


#### Eastern digits 

<span class='affects'>Affects: U+06F4, U+06F6, U+06F7</span>

Feature    | Scheherazade New | Harmattan | Lateef | Feature setting
:--------  | ---------: | ---------: | ---------: | :------------- 
Standard       | <span dir="rtl" class='scheherazadenew-R normal'>&#x06F4;&#x06F6;&#x06F7;</span>                                        | <span dir="rtl" class='harmattan-R normal'>&#x06F4;&#x06F6;&#x06F7;</span>                                        | <span dir="rtl" class='lateef-R normal'>&#x06F4;&#x06F6;&#x06F7;</span>                                        | `cv82=0`
Sindhi-style   | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv82" 1'>&#x06F4;&#x06F6;&#x06F7;</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv82" 1'>&#x06F4;&#x06F6;&#x06F7;</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv82" 1'>&#x06F4;&#x06F6;&#x06F7;</span>| `cv82=1`
Urdu-style     | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv82" 2'>&#x06F4;&#x06F6;&#x06F7;</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv82" 2'>&#x06F4;&#x06F6;&#x06F7;</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv82" 2'>&#x06F4;&#x06F6;&#x06F7;</span>| `cv82=2`
Rohingya-style | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv82" 4'>&#x06F4;&#x06F6;&#x06F7;</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv82" 4'>&#x06F4;&#x06F6;&#x06F7;</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv82" 4'>&#x06F4;&#x06F6;&#x06F7;</span>| `cv82=4`


#### Comma 

<span class='affects'>Affects: U+060C, U+061B</span>

Feature   | Scheherazade New | Harmattan | Lateef | Feature setting
:--------  | ---------: | ---------: | ---------: | :------------- 
Upward   | <span dir="rtl" class='scheherazadenew-R normal'>، ؛</span> | <span dir="rtl" class='harmattan-R normal'>، ؛</span> | <span dir="rtl" class='lateef-R normal'>، ؛</span> | `cv84=0`
Downward | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv84" 1'>، ؛</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv84" 1'>، ؛</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv84" 1'>، ؛</span>| `cv84=1`

#### Decimal separator 

<span class='affects'>Affects: U+066B</span>

Feature   | Scheherazade New | Harmattan | Lateef | Feature setting
:--------  | ---------: | ---------: | ---------: | :------------- 
Small reh | <span dir="rtl" class='scheherazadenew-R normal'>&#x066B;</span> | <span dir="rtl" class='harmattan-R normal'>&#x066B;</span> | <span dir="rtl" class='lateef-R normal'>&#x066B;</span> | `cv85=0`
Slash | <span dir="rtl" class='scheherazadenew-R normal' style='font-feature-settings: "cv85" 1'>&#x066B;</span>| <span dir="rtl" class='harmattan-R normal' style='font-feature-settings: "cv85" 1'>&#x066B;</span>| <span dir="rtl" class='lateef-R normal' style='font-feature-settings: "cv85" 1'>&#x066B;</span>| `cv85=1`





[font id='scheherazadenew' face='ScheherazadeNew-Regular' bold='ScheherazadeNew-Bold' size='150%' rtl=1]
[font id='scheherazadenewL' face='ScheherazadeNew-Regular' bold='ScheherazadeNew-Bold' size='100%' ltr=1]
[font id='harmattan' face='Harmattan-Regular' bold='Harmattan-Bold' size='150%' rtl=1]
[font id='harmattanL' face='Harmattan-Regular' bold='Harmattan-Bold' size='100%' ltr=1]
[font id='lateef' face='Lateef-Regular' bold='Lateef-Bold' size='200%' rtl=1]
[font id='lateefL' face='Lateef-Regular' bold='Lateef-Bold' size='100%' ltr=1]



