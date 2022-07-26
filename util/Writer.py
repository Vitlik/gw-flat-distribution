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
        ws = wb.create_sheet("Zuordnungen_" + swapping)
        wb.active = wb["Zuordnungen_" + swapping]

    ws.append(["Maximales Glück:"])
    ws.append([round(max_happiness, 4)])
    ws.append([""])

    ws["A2"].alignment = Alignment(horizontal='center')
    ws["A2"].fill = PatternFill("solid", start_color="92D050")

    ws.append(["HaushaltsID", "WohnungsID", "Größe", "Summe",
               "Punkt_Glück", "Winkel_Glück", "Riegel_Glück", "EG_Glück", "OG1_Glück", "OG2_Glück", "OG3_Glück",
               "kleiWg_Glück", "Rolli_Glück", "Nachbar_Glück", "HundNähe_Glück", "KatzenNähe_Glück", "RaucherNähe_Glück",
               "Wg_Glück"])

    counter = 4
    for alloc in allocations:
        if alloc < 1000:
            ws.append(
                [allocations[alloc].hh_id, allocations[alloc].wg_id, flats[allocations[alloc].wg_id].flat_type,
                 # sum column
                 allocations[alloc].happy_numbers.sum,
                 # building wish
                 allocations[alloc].happy_numbers.punkt,
                 allocations[alloc].happy_numbers.winkel,
                 allocations[alloc].happy_numbers.riegel,
                 # floor wish
                 allocations[alloc].happy_numbers.eg,
                 allocations[alloc].happy_numbers.og1,
                 allocations[alloc].happy_numbers.og2,
                 allocations[alloc].happy_numbers.og3,
                 # small flat wisch
                 allocations[alloc].happy_numbers.small_flat,
                 # wheelchair wisch
                 allocations[alloc].happy_numbers.wheelchair,
                 # neighbour wish
                 allocations[alloc].happy_numbers.neighbour,
                 # animal wish
                 allocations[alloc].happy_numbers.dog,
                 allocations[alloc].happy_numbers.cat,
                 # smoker wisch
                 allocations[alloc].happy_numbers.smoker,
                 # specific flat wisch
                 allocations[alloc].happy_numbers.specific_flat
                 # "",
                 # actual prefs
                 # hh_wishes[allocations[alloc].hh_id].building_pref,
                 # hh_wishes[allocations[alloc].hh_id].building_weight,
                 # flats[allocations[alloc].wg_id].building,
                 # hh_wishes[allocations[alloc].hh_id].floor_pref,
                 # hh_wishes[allocations[alloc].hh_id].floor_weight,
                 # flats[allocations[alloc].wg_id].floor,
                 # hh_wishes[allocations[alloc].hh_id].neighbour_pref,
                 # hh_wishes[allocations[alloc].hh_id].neighbour_weight,
                 # hh_wishes[allocations[alloc].hh_id].small_flat_pref,
                 # hh_wishes[allocations[alloc].hh_id].small_flat_weight,
                 # flats[allocations[alloc].wg_id].small,
                 # hh_wishes[allocations[alloc].hh_id].animal_pref,
                 # hh_wishes[allocations[alloc].hh_id].animal_weight,
                 # allocations[alloc].happy_numbers.distance_to_next_animal,
                 # hh_wishes[allocations[alloc].hh_id].specific_flat_pref,
                 # hh_wishes[allocations[alloc].hh_id].specific_flat_weight,
                 # hh_wishes[allocations[alloc].hh_id].wheelchair_suitable,
                 # hh_wishes[allocations[alloc].hh_id].wheelchair_suitable_weight
                 ])
        else:
            ws.append([allocations[alloc].hh_id, allocations[alloc].wg_id])
        counter += 1

    # Formatiere Daten als Tabelle
    if not swapping:
        tab = Table(displayName="Allocations", ref="A4:" + get_column_letter(18) + str(counter))
    else:
        tab = Table(displayName="Allocations_neu", ref="A4:" + get_column_letter(18) + str(counter))

    # Lege Tabellen Stil fest (striped rows and banded columns)
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False,
                           showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style

    # füge neues Datenblatt zur Datei hinzu
    ws.add_table(tab)

    # Färbe Spalte grau
    # for cell in ws['K5:K' + str(counter)]:
    #     cell[0].fill = PatternFill("solid", start_color="D9D9D9")
    # ws.column_dimensions["K"].width = 3

    # lege Spaltenbreite pauschal fest
    for i in range(1, 17):  # ,1 to start at 1
        ws.column_dimensions[get_column_letter(i)].width = 10

    # lege Dateinamen fest
    if not swapping:
        new_file_name = file.replace(".xlsx", "") + "_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") \
                        + "_" + str(round(max_happiness, 4)) + ".xlsx"
    else:
        new_file_name = file.replace(".xlsx", "") + "_" + swapping + ".xlsx"

    wb.save(new_file_name)
    print("File saved: " + new_file_name)


def save_allocation(allocations, suffix):
    with open("datasources/allocations_" + suffix + ".pkl", "wb") as out:
        pickle.dump(allocations, out, pickle.HIGHEST_PROTOCOL)
