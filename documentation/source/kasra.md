---
title: Kasra position relative to shadda
---
Note that everything said here about _kasra_ also applies to _kasratan_.

## Introduction
The _shadda_ is drawn above the consonant it modifies, and the _kasra_ is normally drawn below the consonant it follows. When both _shadda_ and _kasra_ follow a consonant, there is a difference in traditions about where the _kasra_ is drawn: in some traditions, including Sindhi, the _kasra_ remains below the consonant. In other traditions, including Arabic, the _kasra_ is drawn above the consonant but below the _shadda_. 

### UTR53 implications

[Unicode Technical Report #53 (UTR53)](https://unicode.org/reports/tr53/) does not address the raised _kasra_ convention. As such it doesn’t tell us what to do if there are other “above marks” on the base. But we can make some observations:

1. With a UTR53 implementation, in the absence of CGJ, the _kasra_ will immediately follow the _shadda_ (since we won’t also have _damma_ or _fatha_)

1. With CGJ, or in DirectWrite/Uniscribe, the results are unpredictable: the _kasra_ could precede the _shadda_ and there could be multiple marks between the two 

1. If there is a _kasra_ out beyond a CGJ, there are several possible interpretations we could make:

   a. The CGJ prevents the raised _kasra_

   b. The CGJ prevents the ligation (to allow _shadda_ and _kasra_ to be colored differently) but _kasra_ remains raised (and just under the _shadda_)

   c. The CGJ has no impact (we go ahead and ligate _shadda+kasra_ (or _kasra+shadda_) (**This is the solution SIL has gone with in their fonts**)

1. But an interpretation we cannot make is

   d. The _kasra_ should -- because of the inside-out rendering assumed by UTR53 -- somehow be rendered above the _shadda_.  (This cannot be correct since it would then appear to be a _fatha_)


## Language preferences

Languages known to use raised _shadda+kasra_ ligature: Arabic, Northern Kurdish (kmr), Kyrgyz (kir).

Languages known to leave the _kasra_ lowered in the context of _shadda_: Rohingya (rhg), Sindhi (snd), Urdu (urd), Wolof (wol), and all Ajami use.

## SIL implementation

- SIL fonts implement a default _kasra_ position ("raised" above the base or "lowered" below the base) that matches the expectations of users in the target audience for the font.
- Some SIL fonts override the default behavior when specific languages have been selected.
- Some SIL fonts provide a user-selectable feature (cv62) that, in apps that support such features, will override both the default and language-specific behaviors.

See font-specific documentation for details.
