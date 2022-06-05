import sys

from util.Calculator import init_distribution
from util.Optimizer import optimize_allocations
from util.Reader import read_source
from util.Writer import save_data

list_hh_wishes = {}  # liste an Haushalten
list_flats = {}  # liste der Wohnungen
list_weights = {}  # Gewichte je Wunsch. Durch Belegungskommission festgelegt
list_allocations = {}  # Format: "Haushalts ID" : "Wohnungs ID"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "Haushaltsinteressen.xlsx"

    read_source(file, list_hh_wishes, list_flats, list_weights)

    init_distribution(list_hh_wishes, list_flats, list_allocations)

    max_happiness = optimize_allocations(list_hh_wishes, list_flats, list_weights, list_allocations)

    save_data(file, list_allocations, max_happiness)
