from texttable import Texttable
import inspect

def test_text_table():
    table = Texttable()
    table.set_cols_align(["l", "r", "c"])
    table.set_cols_valign(["t", "m", "b"])
    table.add_rows([["Name", "Age", "Nickname"],
                    ["Mr\nXavier\nHuon", 32, "Xav'"],
                    ["Mr\nBaptiste\nClement", 1, "Baby"],
                    ["Mme\nLouise\nBourgeau", 28, "Lou\n \nLoue"]])
    expected = inspect.cleandoc("""
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
    """)
    assert table.draw() == expected


def test_dtype_table():
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype(['t',  # text
                          'f',  # float (decimal)
                          'e',  # float (exponent)
                          'i',  # integer
                          'a']) # automatic
    table.set_cols_align(["l", "r", "r", "r", "l"])
    table.add_rows([["text",    "float", "exp", "int", "auto"],
                    ["abcd",    "67",    654,   89,    128.001],
                    ["efghijk", 67.5434, .654,  89.6,  12800000000000000000000.00023],
                    ["lmn",     5e-78,   5e-78, 89.4,  .000000000000128],
                    ["opqrstu", .023,    5e+78, 92.,   12800000000000000000000]])

    expected = inspect.cleandoc("""
     text     float       exp      int     auto    
    ==============================================
    abcd      67.000   6.540e+02    89   128.001   
    efghijk   67.543   6.540e-01    90   1.280e+22 
    lmn        0.000   5.000e-78    89   0.000     
    opqrstu    0.023   5.000e+78    92   1.280e+22 
    """)
    assert table.draw() == expected
