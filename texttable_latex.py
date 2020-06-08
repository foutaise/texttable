"""
Drawing functions for outputting a table in a Latex format.
"""


class DropColumnError(Exception):

    def __init__(self, column, header):
        super().__init__("Cannot drop column {:s} - column not in table header ({:s})\n".format(column, str(header)))


def draw(table, caption, label, drop_columns):
    """Draw the table in Latex format

    - The 'caption' argument is a string that adds a caption to the Latex formatting.
    - The 'label' argument is a string that adds a referencing label to the Latex formatting.
    - The 'drop_columns' argument is an array of column names that won't be in the Latex output.
      Each column name must be in the table header.

    - The formatted table is returned as a whole string
    """
    _sanitise_drop_columns(table._header, drop_columns)
    out = ""
    out += _draw_latex_preamble(table)
    out += _draw_latex_header(table, drop_columns)
    out += _draw_latex_content(table, drop_columns)
    out += _draw_latex_postamble(table, caption, label)
    return out


def _draw_latex_preamble(table):
    """Draw the Latex table preamble.

    - Applies column horizontal alignment
    - Applies columns vlines and table vertical border if appropriate.

    Example Output:
        \begin{table}
            \begin{center}
                \begin{tabular}{|l|r|c|}
    """
    out = "\\begin{table}\n"
    out += _indent_text("\\begin{center}\n", 1)

    # Column setup with/without vlines
    if table._has_vlines():
        column_str = "|".join(table._align)
    else:
        column_str = " ".join(table._align)

    # Border with/without edges
    if table._has_border():
        tabular_str = "\\begin{tabular}{|" + column_str + "|}\n"
    else:
        tabular_str = "\\begin{tabular}{" + column_str + "}\n"
    out += _indent_text(tabular_str, 2)

    return out


def _draw_latex_header(table, drop_columns):
    """Draw the Latex header.

    - Applies header border if appropriate.

    Example Output:
        \hline
        Name & Age & Nickname \\
        \hline
    """
    out = ""
    if table._has_border():
        out += _indent_text("\\hline\n", 3)

    # Drop header columns if required
    header = _drop_columns(table._header.copy(), table._header, drop_columns)
    out += _indent_text(" & ".join(header) + " \\\\\n", 3)

    if table._has_header():
        out += _indent_text("\\hline\n", 3)
    return out


def _draw_latex_content(table, drop_columns):
    """Draw the Latex table content.

    - Applies table hlines if appropriate.

    Example Output:
        MrXavierHuon & 32 & Xav' \\
        \hline
        MrBaptisteClement & 1 & Baby \\
        \hline
        MmeLouiseBourgeau & 28 & Lou Loue \\
    """
    out = ""
    for idx, row in enumerate(table._rows):
        row = _drop_columns(row, table._header, drop_columns)
        clean_row = _clean_row(row)
        out += _indent_text(" & ".join(clean_row) + " \\\\\n", 3)
        if table._has_hlines() and idx != len(table._rows) - 1:
            out += _indent_text("\\hline\n", 3)
    return out


def _draw_latex_postamble(table, caption, label):
    """Draw the Latex table postamble.

    - Adds caption and label if given.
    - Applies table bottom border if appropriate.

    Example Output:
                \hline
                \end{tabular}
            \end{center}
            \caption{An example table.}
            \label{table:example_table}
        \end{table}
    """
    out = ""
    if table._has_border():
        out += _indent_text("\\hline\n", 3)
    out += _indent_text("\\end{tabular}\n", 2)
    out += _indent_text("\\end{center}\n", 1)
    if caption is not None:
        out += _indent_text("\\caption{" + caption + "}\n", 1)
    if label is not None:
        out += _indent_text("\\label{" + label + "}\n", 1)
    out += "\\end{table}"
    return out


def _clean_row(row):
    """Clean a row prior to drawing.

    - Removes newlines.
    """
    clean_row = []
    for element in row:
        clean_row.append(element.replace("\n", ""))
    return clean_row


def _sanitise_drop_columns(header, drop_columns):
    """Check the columns to be dropped.

    - Each column to be dropped must be in the header.
    """
    if drop_columns is None:
        return
    # Check columns (ignores case).
    for column in drop_columns:
        if column.upper() not in [h.upper() for h in header]:
            raise DropColumnError(column, header)


def _drop_columns(target, header, drop_columns):
    """Drop columns from a target array.

    - The 'target' argument is the array from which the columns should be dropped.
    - The 'header' argument is the table header.
      This is used to identify the column index in target that should be dropped.
    - 'drop_columns' specifies which columns should be dropped. Each column should be in the header.
    """
    if drop_columns is None:
        return target
    # Get indices to delete
    to_delete = []
    for column in drop_columns:
        column_idx = header.index(column)
        to_delete.append(column_idx)
    # Delete relevant indices (in reverse order so deletion doesn't affect other index positions)
    for i in sorted(to_delete, reverse=True):
        del target[i]
    return target


def _indent_text(text, indent):
    """Indent a string by a certain number of tabs.

    - 'text' is the text to be indented
    - 'indent' is the number of tabs to prepend to the string.
    """
    return '\t' * indent + text
