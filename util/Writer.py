import pickle
from datetime import datetime

from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter


def save_data_to_xlsx(file, hh_wishes, flats, allocations, max_happiness, swapping):
    wb = load_workbook(file)

    if not swapping:
        ws = wb.create_sheet("Zuordnungen")
        wb.active = wb["Zuordnungen"]
    else:
        ws = wb.create_sheet("Zuordnungen_neu")
        wb.active = wb["Zuordnungen_neu"]

    ws.append(["Maximales Glück:"])
    ws.append([round(max_happiness, 4)])
    ws.append([""])

    ws["A2"].alignment = Alignment(horizontal='center')
    ws["A2"].fill = PatternFill("solid", start_color="92D050")

    ws.append(["HaushaltsID", "WohnungsID",
               "Geb_Glück", "Etage_Glück", "Nachbar_Glück", "kleiWg_Glück", "TierNähe_Glück", "Wg_Glück", "Rolli_Glück",
               "Summe", "_",
               "Geb_Wunsch", "Geb_Gewicht", "Geb_tatsächlich", "Etage_Wunsch", "Etage_Gewicht", "Etage_tatsächlich",
               "Nachbar_Wunsch", "Nachbar_Gewicht", "kleiWg_Wunsch", "kleiWg_Gewicht", "kleiWg_tatsächlich",
               "TierNähe_Wunsch", "TierNähe_Gewicht", "Tier Distanz", "Wg_Wunsch", "Wg_Gewicht",
               "Rolli_Wunsch", "Rolli_Gewicht", ])

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
                 # animal pref
                 allocations[alloc].happy_numbers.animal_pref,
                 # specific flat wisch
                 allocations[alloc].happy_numbers.specific_flat_pref,
                 # wheelchair wisch
                 allocations[alloc].happy_numbers.wheelchair_pref,
                 # sum column
                 allocations[alloc].happy_numbers.building_pref + round(allocations[alloc].happy_numbers.floor_pref, 4)
                 + allocations[alloc].happy_numbers.neighbour_pref + allocations[alloc].happy_numbers.small_flat_pref
                 + allocations[alloc].happy_numbers.animal_pref + allocations[alloc].happy_numbers.specific_flat_pref
                 + allocations[alloc].happy_numbers.wheelchair_pref,
                 "",
                 # actual prefs
                 hh_wishes[allocations[alloc].hh_id].building_pref,
                 hh_wishes[allocations[alloc].hh_id].building_weight,
                 flats[allocations[alloc].wg_id].building,
                 hh_wishes[allocations[alloc].hh_id].floor_pref,
                 hh_wishes[allocations[alloc].hh_id].floor_weight,
                 flats[allocations[alloc].wg_id].floor,
                 hh_wishes[allocations[alloc].hh_id].neighbour_pref,
                 hh_wishes[allocations[alloc].hh_id].neighbour_weight,
                 hh_wishes[allocations[alloc].hh_id].small_flat_pref,
                 hh_wishes[allocations[alloc].hh_id].small_flat_weight,
                 flats[allocations[alloc].wg_id].small,
                 hh_wishes[allocations[alloc].hh_id].animal_pref,
                 hh_wishes[allocations[alloc].hh_id].animal_weight,
                 allocations[alloc].happy_numbers.distance_to_next_animal,
                 hh_wishes[allocations[alloc].hh_id].specific_flat_pref,
                 hh_wishes[allocations[alloc].hh_id].specific_flat_weight,
                 hh_wishes[allocations[alloc].hh_id].wheelchair_suitable,
                 hh_wishes[allocations[alloc].hh_id].wheelchair_suitable_weight
                 ])
        else:
            ws.append([allocations[alloc].hh_id, allocations[alloc].wg_id])
        counter += 1

    if not swapping:
        tab = Table(displayName="Allocations", ref="A4:" + get_column_letter(29) + str(counter))
    else:
        tab = Table(displayName="Allocations_neu", ref="A4:" + get_column_letter(29) + str(counter))

    # Add a default style with striped rows and banded columns
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False,
                           showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style

    ws.add_table(tab)

    for cell in ws['K5:K' + str(counter)]:
        cell[0].fill = PatternFill("solid", start_color="D9D9D9")
    ws.column_dimensions["K"].width = 3

    for i in range(1, 10):  # ,1 to start at 1
        ws.column_dimensions[get_column_letter(i)].width = 14

    if not swapping:
        new_file_name = file.replace(".xlsx", "") + "_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") \
                        + "_" + str(round(max_happiness, 4)) + ".xlsx"
    else:
        new_file_name = file.replace(".xlsx", "") + "_neu.xlsx"

    wb.save(new_file_name)

    print("File saved: " + new_file_name)


def save_allocation(allocations, suffix):
    with open("allocations_" + suffix + ".pkl", "wb") as out:
        pickle.dump(allocations, out, pickle.HIGHEST_PROTOCOL)
