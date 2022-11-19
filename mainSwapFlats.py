import copy
import sys
import pickle

from os.path import exists

from objects.Allocation import Allocation
from objects.HappyNumbers import HappyNumbers
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
        file = path + "/2022-09-25_allocations_4_Update_Excel.xlsx"
        file2 = path + "/WgDaten.xlsx"

    read_source(file, file2, list_hh_wishes, list_flats, list_weights, True)

    last = file.rfind("_")
    lastlast = file[0:last].rfind("_")
    x = file[0:lastlast].rfind("_")
    y = file.rfind(".xlsx")
    pickel_file = path + "/2022-09-25_allocations_4_Update.pkl"

    if exists(pickel_file):
        print("Previous allocation found. Loading existing allocation: " + pickel_file)
        with open(pickel_file, "rb") as inp:
            list_allocations = pickle.load(inp)
    else:
        raise Exception("No previous allocation found.")

    old_allocation = copy.deepcopy(list_allocations)

    ## Haushalte tauschen
    ## Fendel W.202 frei -> W.212 WBS A
    list_hh_wishes[90].wbs = "A" # Wohnungstypwechsel
    hh1 = 90; hh2 = 3212
    swap_flats(hh1, hh2, list_allocations, list_flats)
    ## Martina Fux P.102 WBS A -> P.101 WBS A
    hh1 = 86; hh2 = 2101
    swap_flats(hh1, hh2, list_allocations, list_flats)

    ## Neuen Haushalt hinzufügen
    # list_allocations[209] = Allocation(209, "W.209")
    # list_allocations[209].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    # del list_allocations[3209]  # bisherige Wohnungszuordnung entfernen
    
    ## Haushalt löschen
    # Haushalt Lehmann springt ab
    list_allocations[9204] = Allocation(9204, "P.103")
    list_allocations[9204].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    del list_allocations[204]
    del list_hh_wishes[204]
    # Haushalt Sendal springt ab
    list_allocations[9044] = Allocation(9044, "W.213")
    list_allocations[9044].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    del list_allocations[44]
    del list_hh_wishes[44]

    max_happiness = calc_happiness(list_hh_wishes, list_flats, list_weights, list_allocations)

    list_allocations = check_unfulfilled_wishes(list_hh_wishes, list_flats, list_weights, list_allocations)

    # für Tausch
    # diff_allocations = compare_allocations(list_allocations, old_allocation)
    save_data_to_xlsx(file, list_hh_wishes, list_flats, list_allocations, list_weights, max_happiness, "tausch_" +
                      str(hh1) + "-" + str(hh2) + "_neu")
    # save_data_to_xlsx(file, list_hh_wishes, list_flats, diff_allocations, list_weights, max_happiness, "tausch_" +
                    #   str(hh1) + "-" + str(hh2) + "_diff")

    # für anderes
    # save_data_to_xlsx(file, list_hh_wishes, list_flats, list_allocations, list_weights, max_happiness, "")

    save_allocation(list_allocations, str(round(max_happiness, 4))+"_swapped", path)
