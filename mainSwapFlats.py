import copy
import sys
import pickle

from os.path import exists
from util.Calculator import calc_happiness, check_unfulfilled_wishes, compare_allocations
from util.Writer import save_data_to_xlsx
from util.helper import swap_flats
from util.Reader import read_source

list_hh_wishes = {}  # liste an Haushalten
list_flats = {}  # liste der Wohnungen
list_weights = {}  # Gewichte je Wunsch. Durch Belegungskommission festgelegt
list_allocations = {}  # Format: "Haushalts ID" : "Wohnungs ID"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "datasources/2022-08-18_results-survey2704(1)_korrigiert_2022-08-18_18-12-13_437.2062.xlsx"
        file2 = "datasources/WgDaten.xlsx"

    read_source(file, file2, list_hh_wishes, list_flats, list_weights, True)

    last = file.rfind("_")
    lastlast = file[0:last].rfind("_")
    x = file[0:lastlast].rfind("_")
    y = file.rfind(".xlsx")
    pickel_file = "datasources/allocations_" + file[x+1:y] + ".pkl"

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
    hh1 = 61; hh2 = 94  # Linder, Liane und Penselin, Ulrike

    swap_flats(hh1, hh2, list_allocations, list_flats)  #

    max_happiness = calc_happiness(list_hh_wishes, list_flats, list_weights, list_allocations)

    list_allocations = check_unfulfilled_wishes(list_hh_wishes, list_flats, list_weights, list_allocations)

    diff_allocations = compare_allocations(list_allocations, old_allocation)

    save_data_to_xlsx(file, list_hh_wishes, list_flats, list_allocations, list_weights, max_happiness, "tausch_" +
                      str(hh1) + "-" + str(hh2) + "_neu")
    save_data_to_xlsx(file, list_hh_wishes, list_flats, diff_allocations, list_weights, max_happiness, "tausch_" +
                      str(hh1) + "-" + str(hh2) + "_diff")
