#coding: utf-8

import re
import sys
from textwrap import dedent
from texttable import Texttable

def clean(text):
    return re.sub(r'( +)$', '', text, flags=re.MULTILINE) + '\n'

def test_texttable():
    table = Texttable()
    table.set_cols_align(["l", "r", "c"])
    table.set_cols_valign(["t", "m", "b"])
    table.add_rows([
        ["Name", "Age", "Nickname"],
        ["Mr\nXavier\nHuon", 32, "Xav'"],
        ["Mr\nBaptiste\nClement", 1, "Baby"],
        ["Mme\nLouise\nBourgeau", 28, "Lou\n \nLoue"],
    ])
    assert clean(table.draw()) == dedent('''\
        +----------+-----+----------+
        |   Name   | Age | Nickname |
        +==========+=====+==========+
        | Mr       |     |          |
        | Xavier   |  32 |          |
        | Huon     |     |   Xav'   |
        +----------+-----+----------+
        | Mr       |     |          |
        | Baptiste |   1 |          |
        | Clement  |     |   Baby   |
        +----------+-----+----------+
        | Mme      |     |   Lou    |
        | Louise   |  28 |          |
        | Bourgeau |     |   Loue   |
        +----------+-----+----------+
    ''')

def test_texttable_header():
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype([
        't',  # text
        'f',  # float (decimal)
        'e',  # float (exponent)
        'i',  # integer
        'a',  # automatic
    ])
    table.set_cols_align(["l", "r", "r", "r", "l"])
    table.add_rows([
        ["text",    "float", "exp", "int", "auto"],
        ["abcd",    "67",    654,   89,    128.001],
        ["efghijk", 67.5434, .654,  89.6,  12800000000000000000000.00023],
        ["lmn",     5e-78,   5e-78, 89.4,  .000000000000128],
        ["opqrstu", .023,    5e+78, 92.,   12800000000000000000000],
    ])
    assert clean(table.draw()) == dedent('''\
         text     float       exp      int     auto
        ==============================================
        abcd      67.000   6.540e+02    89   128.001
        efghijk   67.543   6.540e-01    90   1.280e+22
        lmn        0.000   5.000e-78    89   0.000
        opqrstu    0.023   5.000e+78    92   1.280e+22
    ''')

def test_set_cols_width():
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_width([10, 10])
    table.add_rows([
        ["key", "value"],
        [1,     "a"],
        [2,     "b"],
    ])
    assert clean(table.draw()) == dedent('''\
           key         value
        =======================
        1            a
        2            b
    ''')

def test_exceeding_max_width():
    table = Texttable(max_width=35)
    table.set_deco(Texttable.HEADER)
    table.add_rows([
        ["key", "value"],
        [1,     "a"],
        [2,     "b"],
        [3,     "very long, very long, very long"],
    ])
    assert clean(table.draw()) == dedent('''\
        key               value
        ===================================
        1     a
        2     b
        3     very long, very long, very
              long
    ''')

def test_exceeding_max_width2():
    table = Texttable(max_width=14)
    table.add_rows([
        ["a", "b"],
        [1, "+"],
        [22, "++++++++"],
    ])
    assert clean(table.draw()) == dedent('''\
	+----+-------+
	| a  |   b   |
	+====+=======+
	| 1  | +     |
	+----+-------+
	| 22 | +++++ |
	|    | +++   |
	+----+-------+
    ''')

def test_obj2unicode():
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.add_rows([
        ["key", "value"],
        [1,     "a"],
        [2,     1],
        [3,     None],
    ])
    assert clean(table.draw()) == dedent('''\
        key   value
        ===========
        1     a
        2     1
        3     None
    ''')

def test_combining_char():
    if sys.version >= '3':
        u_dedent = dedent
    else:
        def u_dedent(b):
           return unicode(dedent(b), 'utf-8')
    table = Texttable()
    table.set_cols_align(["l", "r", "r"])
    table.add_rows([
        ["str", "code-point\nlength", "display\nwidth"],
        ["ā", 2, 1],
        ["a", 1, 1],
    ])
    assert clean(table.draw()) == u_dedent('''\
        +-----+------------+---------+
        | str | code-point | display |
        |     |   length   |  width  |
        +=====+============+=========+
        | ā   |          2 |       1 |
        +-----+------------+---------+
        | a   |          1 |       1 |
        +-----+------------+---------+
    ''')
