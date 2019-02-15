# Version History

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
* fix bug in wide chars handling (https://github.com/foutaise/texttable/issues/9)
* avoid use of sys.version to obtain Python version (https://github.com/foutaise/texttable/pull/24)
