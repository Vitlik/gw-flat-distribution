import sys
import pickle

from os.path import exists
from util.Calculator import calc_happiness
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
        file = "datasources/2022-07-21_results-survey2704_korrigiert_2022-07-26_23-12-33_263.0.xlsx"
        file2 = "datasources/WgDaten.xlsx"

    hh1 = 4
    hh2 = 59

    read_source(file, file2, list_hh_wishes, list_flats, list_weights)

    x = file.rfind("_")
    y = file.rfind(".xlsx")
    pickel_file = "datasources/allocations_" + file[x+1:y] + ".pkl"

    if exists(pickel_file):
        print("Previous allocation found. Loading existing allocation: " + pickel_file)
        with open(pickel_file, "rb") as inp:
            list_allocations = pickle.load(inp)
    else:
        raise Exception("No previous allocation found.")

    swap_flats(hh1, hh2, list_allocations)

    max_happiness = calc_happiness(list_hh_wishes, list_flats, list_weights, list_allocations)

    save_data_to_xlsx(file, list_hh_wishes, list_flats, list_allocations, max_happiness, "swapped_" + str(hh1) + "_" + str(hh2))
