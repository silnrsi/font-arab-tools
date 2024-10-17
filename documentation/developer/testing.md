# Using ftml and other test files

## FTML
FTML is an xml-based format for organizing test data, including the test strings along 
with feature and language selection and other test metadata. 
For more info about FTML see [Font Test Markup Language](https://github.com/silnrsi/ftml).

One useful capability is that ftml files can be opened directly in Firefox which will then render the test strings using freshly built fonts without needing to install the fonts. Two things must be in place in order to do this:

- The ftml file must identify a suitable .xsl file such as `tools/ftml.xsl`. (All the ftml files in the `tests/` folder are configured this way)
- Firefox's "strict URI" policy must be relaxed by going to `about:config` and setting 
[security.fileuri.strict_origin_policy](https://kb.mozillazine.org/Security.fileuri.strict_origin_policy) to false.

(For more information see [Using Browsers for no-install font testing](https://silnrsi.github.io/FDBP/en-US/Browsers%20as%20a%20font%20test%20platform.html))

This means that after a successful `smith build`, the `tests/*.ftml` documents can be opened directly in Firefox (which supports both Graphite and OpenType rendering).

## Regression testing

After a successful `smith test` or `smith alltests`, the `results/test` folder will contain
regression testing data which compares rendering of test files (e.g., `ftml` files) using the built fonts (in `results/`) with that using corresponding fonts in the `reference/` folder.

Be aware, however, that due to bugs in smith, at present the regression tests may indicate differences in rendering when there are none.
