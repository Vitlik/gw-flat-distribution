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
        pickel_file = path + "/2022-11-19_allocations_5.pkl"
        xlsx        = path + "/2022-12-04_allocations_6_tmp.xlsx"
        wgDaten       = path + "/WgDaten.xlsx"

    read_source(xlsx, wgDaten, list_hh_wishes, list_flats, list_weights, True)

    if exists(pickel_file):
        print("Previous allocation found. Loading existing allocation: " + pickel_file)
        with open(pickel_file, "rb") as inp:
            list_allocations = pickle.load(inp)
    else:
        raise Exception("No previous allocation found.")

    old_allocation = copy.deepcopy(list_allocations)

    # Vorlage - Tausch
    hh1 = 86; hh2 = 2101
    swap_flats(hh1, hh2, list_allocations, list_flats)

    # Vorlage - Neuen Haushalt hinzufügen
    # list_allocations[216] = Allocation(216, "P.107")
    # list_allocations[216].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    # old_allocation[216] = Allocation(216, "P.107")
    # old_allocation[216].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    # del list_allocations[2207] # bisherige Wohnungszuordnung entfernen

    # Vorlage - Haushalt abgesprungen
    # Rohmann springt ab
    list_allocations[9012] = Allocation(9012, "W.012")
    old_allocation[9012] = Allocation(9012, "W.012")
    del list_allocations[116] # bisherige Wohnungszuordnung entfernen
    del old_allocation[116] # bisherige Wohnungszuordnung entfernen
    
    
    # Vorlage - Haushalt wechselt WBS Status - hier ist nichts zu tun, da die WBS Status nicht in der Zuordnung gespeichert werden
    # Stattdessen ist der WBS Status des Haushalts in der Excel "Haushaltsübersicht" zu ändern.
    # Schlattmann wechselt von frei zu WBS und Wohnung
    hh1 = 103; hh2 = 9012
    swap_flats(hh1, hh2, list_allocations, list_flats)

    
    # Neuberechnung
    max_happiness = calc_happiness(list_hh_wishes, list_flats, list_weights, list_allocations)
    list_allocations = check_unfulfilled_wishes(list_hh_wishes, list_flats, list_weights, list_allocations)

    # Berechnung Auswirkungen der Änderungen
    diff_allocations = compare_allocations(list_allocations, old_allocation)
    
    # Speichere Wohnungstausch
    try:
        save_data_to_xlsx(xlsx, list_hh_wishes, list_flats, list_allocations, list_weights, max_happiness, "tausch_" +
                    str(hh1) + "-" + str(hh2) + "_neu")
        save_data_to_xlsx(xlsx, list_hh_wishes, list_flats, diff_allocations, list_weights, max_happiness, "tausch_" +
                          str(hh1) + "-" + str(hh2) + "_diff")
    except NameError:
        save_data_to_xlsx(xlsx, list_hh_wishes, list_flats, list_allocations, list_weights, max_happiness, "neu")
        save_data_to_xlsx(xlsx, list_hh_wishes, list_flats, diff_allocations, list_weights, max_happiness, "neu_diff")
        

    # für anderes
    # save_data_to_xlsx(file, list_hh_wishes, list_flats, list_allocations, list_weights, max_happiness, "")

    # save_allocation(list_allocations, str(round(max_happiness, 4))+"_swapped", path)
