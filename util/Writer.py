import pickle
from datetime import datetime

from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter


def save_data(file, hh_wishes, flats, allocations, max_happiness):
    wb = load_workbook(file)

    ws = wb.create_sheet("Zuordnungen")
    wb.active = wb["Zuordnungen"]

    ws.append(["Maximales Glück:"])
    ws.append([round(max_happiness, 4)])
    ws.append([""])

    ws["A2"].alignment = Alignment(horizontal='center')
    ws["A2"].fill = PatternFill("solid", start_color="92D050")

    ws.append(["HaushaltsID", "WohnungsID",
               "Geb_Glück", "Etage_Glück", "Nachbar_Glück", "kleiWg_Glück", "Wg_Glück", "TierNähe_Glück", "Summe", "_",
               "Geb_Wunsch", "Geb_tatsächlich", "Etage_Wunsch", "Etage_tatsächlich", "Nachbar_Wunsch",
               "kleiWg_Wunsch", "kleiWg_tatsächlich", "Wg_Wunsch", "TierNähe_Wunsch", "Tier Distanz" ])

    counter = 4
    for alloc in allocations:
        if alloc <= 9000:
            ws.append(
                [allocations[alloc].hh_id, allocations[alloc].wg_id,
                 # building wish
                 allocations[alloc].happy_numbers.building_pref,
                 # floor wish
                 round(allocations[alloc].happy_numbers.floor_pref, 4),
                 # neighbour wish
                 allocations[alloc].happy_numbers.neighbour_pref,
                 # small flat wisch
                 allocations[alloc].happy_numbers.small_flat_pref,
                 # specific flat wisch
                 allocations[alloc].happy_numbers.specific_flat_pref,
                 # animal pref
                 allocations[alloc].happy_numbers.animal_pref,
                 # sum column
                 allocations[alloc].happy_numbers.building_pref + round(allocations[alloc].happy_numbers.floor_pref, 4)
                 + allocations[alloc].happy_numbers.neighbour_pref + allocations[alloc].happy_numbers.small_flat_pref
                 + allocations[alloc].happy_numbers.animal_pref,
                 "",
                 # actual prefs
                 hh_wishes[allocations[alloc].hh_id].building_pref,
                 flats[allocations[alloc].wg_id].building,
                 hh_wishes[allocations[alloc].hh_id].floor_pref,
                 flats[allocations[alloc].wg_id].floor,
                 hh_wishes[allocations[alloc].hh_id].neighbour_pref,
                 hh_wishes[allocations[alloc].hh_id].small_flat_pref,
                 flats[allocations[alloc].wg_id].small,
                 hh_wishes[allocations[alloc].hh_id].specific_flat_pref,
                 hh_wishes[allocations[alloc].hh_id].animal_pref,
                 allocations[alloc].happy_numbers.distance_to_next_animal,
                 ])
        else:
            ws.append([allocations[alloc].hh_id, allocations[alloc].wg_id])
        counter += 1

    tab = Table(displayName="Allocations", ref="A4:T" + str(counter))

    # Add a default style with striped rows and banded columns
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False,
                           showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style

    ws.add_table(tab)

    for cell in ws['J5:J' + str(counter)]:
        cell[0].fill = PatternFill("solid", start_color="D9D9D9")

    for i in range(1, 10):  # ,1 to start at 1
        ws.column_dimensions[get_column_letter(i)].width = 14

    new_file_name = file.replace(".xlsx", "") + "_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".xlsx"
    wb.save(new_file_name)

    print("File saved: " + new_file_name)

    with open("allocations.pkl", "wb") as out:
        pickle.dump(allocations, out, pickle.HIGHEST_PROTOCOL)
