import re
from openpyxl import load_workbook
from objects import Household, Flat
from objects.Allocation import Allocation
from objects.HappyNumbers import HappyNumbers


def read_source(file, list_hh_wishes, list_flats, list_weights):
    wb = load_workbook(file)

    hh_wishes = wb.worksheets[0]
    last_row = int(re.search(r'\d*$', hh_wishes.dimensions).group(0))
    for row in range(2, last_row + 1):
        list_hh_wishes[hh_wishes["A" + str(row)].value] = \
            Household.Household(
                hh_wishes["A" + str(row)].value,
                hh_wishes["B" + str(row)].value,
                hh_wishes["C" + str(row)].value,
                hh_wishes["D" + str(row)].value,
                hh_wishes["E" + str(row)].value,
                hh_wishes["F" + str(row)].value,
                hh_wishes["G" + str(row)].value,
                hh_wishes["H" + str(row)].value,
                hh_wishes["I" + str(row)].value,
                hh_wishes["J" + str(row)].value,
                hh_wishes["K" + str(row)].value,
                hh_wishes["L" + str(row)].value,
                hh_wishes["M" + str(row)].value,
                hh_wishes["N" + str(row)].value,
                hh_wishes["O" + str(row)].value,
                hh_wishes["P" + str(row)].value
            )

    ws_flat_data = wb.worksheets[1]
    last_row_wohndaten = int(re.search(r'\d*$', ws_flat_data.dimensions).group(0))
    for row in range(2, last_row_wohndaten + 1):
        list_flats[ws_flat_data["A" + str(row)].value] = \
            Flat.Flat(
                ws_flat_data["A" + str(row)].value,
                ws_flat_data["B" + str(row)].value,
                ws_flat_data["C" + str(row)].value,
                ws_flat_data["D" + str(row)].value,
                ws_flat_data["E" + str(row)].value,
                ws_flat_data["F" + str(row)].value
            )

    config = wb.worksheets[2]
    first_row_gew = int(re.search(r'[0-9]{1,4}(?=:)', config.tables["gewichte_tab"].ref).group()) + 1
    first_col_gew = re.search(r'^[A-Z]{1,4}', config.tables["gewichte_tab"].ref).group()
    last_row_gew = int(re.search(r'[0-9]{1,4}$', config.tables["gewichte_tab"].ref).group())
    last_col_gew = re.search(r'(?<=:)[A-Z]*', config.tables["gewichte_tab"].ref).group()
    for row in range(first_row_gew, last_row_gew + 1):
        list_weights[config[first_col_gew + str(row)].value] = int(config[last_col_gew + str(row)].value)


def read_results(file, allocations):
    wb = load_workbook(file)

    ws_alloc = wb["Zuordnungen"]
    last_row = int(re.search(r'\d*$', ws_alloc.dimensions).group(0))
    for row in range(5, last_row + 1):
        allocations[ws_alloc["A" + str(row)].value] = \
            Allocation(
                ws_alloc["A" + str(row)].value,
                ws_alloc["B" + str(row)].value
            )
        if int(ws_alloc["A" + str(row)].value) <= 9000:
            allocations[ws_alloc["A" + str(row)].value].happy_numbers = \
                HappyNumbers(ws_alloc["C" + str(row)].value,
                             ws_alloc["D" + str(row)].value,
                             ws_alloc["E" + str(row)].value,
                             ws_alloc["F" + str(row)].value,
                             ws_alloc["G" + str(row)].value,
                             ws_alloc["H" + str(row)].value,
                             ws_alloc["I" + str(row)].value)
        else:
            allocations[ws_alloc["A" + str(row)].value].happy_numbers = \
                HappyNumbers(0, 0, 0, 0, 0, 0, 0)
