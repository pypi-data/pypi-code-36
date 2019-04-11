
# noinspection PyUnresolvedReferences
from pythoncom import com_error

from datetime import date
from datetime import datetime

from .. util.iter import modify_iteration_depth
from .. excel_com.excel_address import col_letter
from .. excel_com.excel_address import col_number
from .. excel_com.excel_address import max_cols

from .workbook import app_to_foreground
from .excel_constants import *


def get_worksheet(wb, tab_name,
                  *,
                  clear_filter=False,
                  activate=False):

    if tab_name.__class__.__name__ in {'CDispatch', '_Worksheet'}:
        return tab_name

    if wb is None:
        raise AssertionError("Cannot retrieve tab: '{}' Excel workbook has not been initialized!".format(tab_name))

    ws = None
    if isinstance(tab_name, str):
        for ws in wb.Sheets:
            if ws.Name.lower() == tab_name.lower():
                break

    elif isinstance(tab_name, int):
        ws = wb.sheets[tab_name]

    if ws is None:
        raise NameError("tab: '{}' not found in workbook: '{}'".format(tab_name, wb.name))

    ws.Visible = True

    if clear_filter:
        clear_worksheet_filter(ws)

    if activate:
        app_to_foreground(ws.Application)
        ws.Activate()

    return ws


def is_filtered(ws):
    if ws.AutoFilter is not None:
        return ws.AutoFilter.FilterMode


def clear_worksheet_filter(ws):
    if is_filtered(ws):
        # noinspection PyProtectedMember
        ws._AutoFilter.ShowAllData()


def is_range_empty(excel_range):
    num_cells = int(excel_range.Application.WorksheetFunction.CountA(excel_range))
    return num_cells == 0


def activate_sheet(ws):
    app_to_foreground(ws.Application)
    ws.Visible = True
    ws.Activate()


def write_to_excel_range(v, excel_range):
    m = modify_iteration_depth(v, 2)
    m = list(__excel_friendly_matrix(m))

    a = excel_range.Address
    if ':' not in a:
        a = '{}:{}'.format(a, excel_range.Resize(len(m), len(m[0])).Address)
    else:
        a = excel_range.Resize(len(m), len(m[0])).Address

    excel_range.Parent.Range(a).Value = m


def gen_range_rows(excel_range):
    for row in __convert_excel_errors(excel_range):
        yield row


def __convert_excel_errors(excel_range):
    m = excel_range.Value
    m = modify_iteration_depth(m, 2)
    m = [list(row) for row in m]

    try:
        range_errors = excel_range.SpecialCells(xl_cell_type_formulas, xl_errors)
        cell = first_cell(excel_range)
        r_0  = cell.Row
        c_0  = cell.Column

        for cell_error in range_errors:
            r = cell_error.Row - r_0
            c = cell_error.Column - c_0
            m[r][c] = excel_errors.get(m[r][c], 'unknown error')

    except com_error:
        pass

    return m


def __excel_friendly_matrix(m):
    """ modify matrix values so they can be written to an excel range without error """

    if len(m[0]) > max_cols:
        raise ValueError("matrix columns ({:,}) exceeds Excel's column limit\n(did you mean to transpose this matrix?)"
                         .format(len(m[0])))

    for row in m:
        row_ = []

        for c, v in enumerate(row):
            if isinstance(v, (bool, int, float, str)) or v is None:
                pass
            elif isinstance(v, date):
                v = datetime(v.year, v.month, v.day)
            else:
                v = repr(v)

            row_.append(v)

        yield row_


def range_find(excel_range,
               what,
               after=None,
               look_in=xl_values,
               look_at=xl_whole,
               search_order=xl_by_rows,
               search_direction=xl_previous,
               match_case=False):

    if after is None:
        if search_direction == xl_next:
            after = last_cell(excel_range)
        elif search_direction == xl_previous:
            after = first_cell(excel_range)

    search = excel_range.Find(what,
                              after,
                              look_in,
                              look_at,
                              search_order,
                              search_direction,
                              match_case)

    return search


def first_cell(excel_range):
    return excel_range.Cells(1)


def last_cell(excel_range):
    """ excel_range.Cells(excel_range.Cells.Count) causes an overflow error
    this is not always reliable when excel_range.Cells() requires both row and column arguments
    """
    a = excel_range.Address.split(':')[-1]
    return excel_range.Parent.Range(a)


def first_row(excel_range, default_r=1):
    search = range_find(excel_range,
                        what='*',
                        search_order=xl_by_rows,
                        search_direction=xl_next)

    if search:
        r = max(search.Row, default_r)
    else:
        r = default_r

    return r


def last_row(excel_range, default_r=1):
    search = range_find(excel_range,
                        what='*',
                        search_order=xl_by_rows,
                        search_direction=xl_previous)

    if search:
        r = max(search.Row, default_r)
    else:
        r = default_r

    return r


def first_col(excel_range, default_c='A'):
    search = range_find(excel_range,
                        what='*',
                        search_order=xl_by_columns,
                        search_direction=xl_next)

    if search:
        c = max(search.Column, col_number(default_c))
        c_lttr = col_letter(c)
    else:
        c_lttr = default_c

    return c_lttr


def last_col(excel_range, default_c='A'):
    search = range_find(excel_range,
                        what='*',
                        search_order=xl_by_columns,
                        search_direction=xl_previous)

    if search:
        c = max(search.Column, col_number(default_c))
        c_lttr = col_letter(c)
    else:
        c_lttr = default_c

    return c_lttr


def first_non_blank_col(excel_range, default_c='A'):
    search = range_find(excel_range,
                        what='',
                        search_order=xl_by_columns,
                        search_direction=xl_next)

    if search:
        c = max(search.Column - 1, col_number(default_c))
        c_lttr = col_letter(c)
    else:
        c_lttr = default_c

    return c_lttr


def parse_range(excel_range):
    c_1 = first_cell(excel_range).Column
    c_1 = col_letter(c_1)

    c_2 = last_cell(excel_range).Column
    c_2 = col_letter(c_2)

    r_1 = first_cell(excel_range).Row
    r_2 = last_cell(excel_range).Row

    return c_1, r_1, c_2, r_2

