import sys

from util.Calculator import calc_happiness
from util.Writer import save_data_to_xlsx
from util.helper import swap_flats
from util.Reader import read_source
from util.Reader import read_results

list_hh_wishes = {}  # liste an Haushalten
list_flats = {}  # liste der Wohnungen
list_weights = {}  # Gewichte je Wunsch. Durch Belegungskommission festgelegt
list_allocations = {}  # Format: "Haushalts ID" : "Wohnungs ID"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "Haushaltsinteressen_2022-06-06_22-45-45_98.5667.xlsx"

    hh1 = 1
    hh2 = 2

    read_source(file, list_hh_wishes, list_flats, list_weights)

    read_results(file, list_allocations)

    swap_flats(hh1, hh2, list_allocations)

    max_happiness = calc_happiness(list_hh_wishes, list_flats, list_weights, list_allocations)

    save_data_to_xlsx(file, list_hh_wishes, list_flats, list_allocations, max_happiness, True)
