import pickle
import sys
from os.path import exists

from util.Calculator import init_distribution, calc_happiness
from util.Optimizer import optimize_allocations
from util.Reader import read_source
from util.Writer import save_data, save_allocation

list_hh_wishes = {}  # liste an Haushalten
list_flats = {}  # liste der Wohnungen
list_weights = {}  # Gewichte je Wunsch. Durch Belegungskommission festgelegt
list_allocations = {}  # Format: "Haushalts ID" : ["Wohnungs ID", HappyNumbers]


def main_method():
    global list_allocations
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "Haushaltsinteressen.xlsx"
    read_source(file, list_hh_wishes, list_flats, list_weights)
    pickel_file = "allocations.pkl"
    if exists(pickel_file):
        print("Previous allocation found. Loading existing allocation.")
        with open(pickel_file, "rb") as inp:
            list_allocations = pickle.load(inp)
    else:
        print("No previous allocation found. Initializing new allocation.")
        init_distribution(list_hh_wishes, list_flats, list_allocations)
    # max_happiness = calc_happiness(list_hh_wishes, list_flats, list_weights, list_allocations)
    # swap_flats(list_allocations[1].hh_id, list_allocations[2].hh_id, list_allocations)
    # new_happiness = calc_happiness(list_hh_wishes, list_flats, list_weights, list_allocations)
    list_allocations = optimize_allocations(list_hh_wishes, list_flats, list_weights, list_allocations)
    max_happiness = calc_happiness(list_hh_wishes, list_flats, list_weights, list_allocations)
    save_data(file, list_hh_wishes, list_flats, list_allocations, max_happiness, False)
    save_allocation(list_allocations, str(round(max_happiness, 4)))


if __name__ == '__main__':
    for i in range(10):
        main_method()
