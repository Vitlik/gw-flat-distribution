import pickle
import sys
from os.path import exists
from datetime import datetime
from util.Calculator import init_distribution, calc_happiness
from util.Optimizer import optimize_allocations
from util.Reader import read_source
from util.Writer import save_data_to_xlsx, save_allocation

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

    pickel_file = "allocations_100.5333.pkl"
    if exists(pickel_file):
        print("Previous allocation found. Loading existing allocation: " + pickel_file)
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
    save_allocation(list_allocations, str(round(max_happiness, 4)))
    # save_data_to_xlsx(file, list_hh_wishes, list_flats, list_allocations, max_happiness, False)


if __name__ == '__main__':
    full_start = datetime.now()
    for i in range(1):
        start = datetime.now()
        main_method()
        diff = datetime.now() - start
        print(str(diff.seconds / 60) + " mins")
        print("--------------------------------------")
        list_hh_wishes = {}
        list_flats = {}
        list_weights = {}
        list_allocations = {}
    full_diff = datetime.now() - full_start
    print("--------------------------------------")
    print(str(full_diff.seconds / 60) + " mins")
