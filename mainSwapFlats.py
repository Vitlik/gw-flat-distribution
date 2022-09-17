import copy
import sys
import pickle

from os.path import exists
from util.Calculator import calc_happiness, check_unfulfilled_wishes, compare_allocations
from util.Writer import save_data_to_xlsx, save_allocation
from util.helper import swap_flats
from util.Reader import read_source

list_hh_wishes = {}  # liste an Haushalten
list_flats = {}  # liste der Wohnungen
list_weights = {}  # Gewichte je Wunsch. Durch Belegungskommission festgelegt
list_allocations = {}  # Format: "Haushalts ID" : "Wohnungs ID"


if __name__ == '__main__':

    path = "D:/HomeOnD/NC/Projekte/gw-wohnvergabe-datasources"

    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = path + "/2022-08-19_allocations_2_nach_Tausch_Excel.xlsx"
        file2 = path + "/WgDaten.xlsx"

    read_source(file, file2, list_hh_wishes, list_flats, list_weights, True)

    last = file.rfind("_")
    lastlast = file[0:last].rfind("_")
    x = file[0:lastlast].rfind("_")
    y = file.rfind(".xlsx")
    pickel_file = path + "/2022-08-19_allocations_2_nach_Tausch.pkl"

    if exists(pickel_file):
        print("Previous allocation found. Loading existing allocation: " + pickel_file)
        with open(pickel_file, "rb") as inp:
            list_allocations = pickle.load(inp)
    else:
        raise Exception("No previous allocation found.")

    old_allocation = copy.deepcopy(list_allocations)

    # hh1 = 4; hh2 = 65  # Thorsten und Sabine
    # hh1 = 19; hh2 = 1109  # Detlev und freie Wohnung
    # hh1 = 36; hh2 = 63  # Jeanette und Kallmeyer, Ruth
    # hh1 = 36; hh2 = 88  # Jeanette und Tim Többe
    # hh1 = 61; hh2 = 94  # Linder, Liane und Penselin, Ulrike
    # hh1 = 43; hh2 = 3106  # Schätz, Gabriela und frei

    # Riegel
    hh1 = 28; hh2 = 17
    swap_flats(hh1, hh2, list_allocations, list_flats)  #

    hh1 = 17; hh2 = 1107
    swap_flats(hh1, hh2, list_allocations, list_flats)  #

    hh1 = 50; hh2 = 1211
    swap_flats(hh1, hh2, list_allocations, list_flats)  #

    hh1 = 92; hh2 = 1110  # Marianne Witt & frei
    swap_flats(hh1, hh2, list_allocations, list_flats)  #

    hh1 = 85; hh2 = 1110  # roth & frei
    swap_flats(hh1, hh2, list_allocations, list_flats)  #

    # Punkt
    hh1 = 202; hh2 = 2103  # drovs & frei
    swap_flats(hh1, hh2, list_allocations, list_flats)  #

    hh1 = 114; hh2 = 88
    swap_flats(hh1, hh2, list_allocations, list_flats)  #

    hh1 = 88; hh2 = 96
    swap_flats(hh1, hh2, list_allocations, list_flats)  #

    hh1 = 115; hh2 = 3101  # drovs & frei
    swap_flats(hh1, hh2, list_allocations, list_flats)  #

    max_happiness = calc_happiness(list_hh_wishes, list_flats, list_weights, list_allocations)

    list_allocations = check_unfulfilled_wishes(list_hh_wishes, list_flats, list_weights, list_allocations)

    diff_allocations = compare_allocations(list_allocations, old_allocation)

    save_data_to_xlsx(file, list_hh_wishes, list_flats, list_allocations, list_weights, max_happiness, "tausch_" +
                      str(hh1) + "-" + str(hh2) + "_neu")
    save_data_to_xlsx(file, list_hh_wishes, list_flats, diff_allocations, list_weights, max_happiness, "tausch_" +
                      str(hh1) + "-" + str(hh2) + "_diff")

    save_allocation(list_allocations, str(round(max_happiness, 4))+"_swapped", path)
