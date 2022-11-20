# Version History

v1.6.5 (2022-11-20)
* Modify setup.py to include missing stub file in wheel package (https://github.com/foutaise/texttable/issues/82)

v1.6.4 (2021-07-13)
* Fix alignment bug when deco is modified (https://github.com/foutaise/texttable/issues/76)

v1.6.3 (2020-09-06)
* Improve int conversion (https://github.com/foutaise/texttable/issues/70)

v1.6.2 (2019-07-01)
* Fix auto-formatting NaN (https://github.com/foutaise/texttable/pull/60)

v1.6.1 (2019-02-15)
* Include tests, license in source tarball (https://github.com/foutaise/texttable/issues/58)
* Add changelog

v1.6.0 (2019-01-17)
* Add basic emoji support (https://github.com/foutaise/texttable/issues/55)

v1.5.0 (2018-11-02)
* Create a method for redefining the max_width (https://github.com/foutaise/texttable/issues/54)
* Use setuptools instead of distutils to upload metadata to PyPI (https://github.com/foutaise/texttable/issues/49)
* Switch to MIT license

v1.4.0 (2018-06-22)
* Add set_header_align() method (https://github.com/foutaise/texttable/issues/45)

v1.3.1 (2018-06-12)
* Fix missing textwrapper command when cjkwrap is not used (https://github.com/foutaise/texttable/issues/43)

v1.3.0 (2018-06-11)
* Remove redundant code for unsupported/EOL Python (https://github.com/foutaise/texttable/pull/31)

v1.2.1 (2018-01-03)
* Use test_cjkwrap only when cjkwrap is available (https://github.com/foutaise/texttable/issues/35)

v1.2.0 (2018-01-03)
* Use cjkwrap for better CJK text support (https://github.com/foutaise/texttable/issues/34)

v1.1.1 (2017-10-26)
* Fallback to text on TypeError (https://github.com/foutaise/texttable/issues/28)

v1.1.0 (2017-10-22)
* Easier formatting, allow callable as a column datatype (PR https://github.com/foutaise/texttable/pull/27)

v1.0.0 (2017-10-14)
* Fix bug in wide chars handling (https://github.com/foutaise/texttable/issues/9)
* Avoid use of sys.version to obtain Python version (https://github.com/foutaise/texttable/pull/24)

v0.9.1 (2017-06-27)
* Add support for combining characters (https://github.com/foutaise/texttable/pull/19)

v0.9.0 (2017-05-16)
* Fix width of table exceeds max_width parameter (https://github.com/foutaise/texttable/pull/15)

v0.8.8 (2017-03-30)
* Add east asian support (https://github.com/foutaise/texttable/pull/12)
* Relative col widths improvements + unit tests (https://github.com/foutaise/texttable/pull/13)

v0.8.7 (2016-11-14)
* Proper handling of unicode in headers (https://github.com/foutaise/texttable/issues/9)

v0.8.6 (2016-10-21)
* Preserve empty lines (https://github.com/foutaise/texttable/pull/8)

v0.8.5 (2016-10-16)
* Better handling of unicode encodings (https://github.com/foutaise/texttable/pull/6)

v0.8.4 (2015-11-16)
* Fix pypi url

v0.8.3 (2015-11-16)
* Update README.md
