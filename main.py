import copy
import pickle

from os.path import exists
from datetime import datetime
from util.Calculator import init_distribution, calc_happiness, check_unfulfilled_wishes
from util.Optimizer import optimize_allocations
from util.Reader import read_source
from util.Writer import save_data_to_xlsx, save_allocation
from multiprocessing import Pool


def main_method(id):
    list_hh_wishes = {}  # liste an Haushalten
    list_flats = {}  # liste der Wohnungen
    list_weights = {}  # Gewichte je Wunsch. Durch Belegungskommission festgelegt
    list_allocations = {}  # Format: "Haushalts ID" : ["Wohnungs ID", HappyNumbers]

    path = "D:/HomeOnD/NC/Projekte/gw-wohnvergabe-datasources"

    file = path + "/2022-11-19_allocations_5.xlsx"
    file2 = path + "/WgDaten.xlsx"

    read_source(file, file2, list_hh_wishes, list_flats, list_weights)

    pickel_file = path + "/2022-11-19_allocations_5.pkl"
    if exists(pickel_file):
        print("Previous allocation found. Loading existing allocation: " + pickel_file)
        with open(pickel_file, "rb") as inp:
            list_allocations = pickle.load(inp)
    else:
        print("No previous allocation found. Initializing new allocation.")
        init_distribution(list_hh_wishes, list_flats, list_allocations)
        # save_allocation(list_allocations, "init")

    swap_real_flats = False

    list_allocations = optimize_allocations(list_hh_wishes, list_flats, list_weights, list_allocations, swap_real_flats)

    max_happiness = calc_happiness(list_hh_wishes, list_flats, list_weights, list_allocations)

    list_allocations = check_unfulfilled_wishes(list_hh_wishes, list_flats, list_weights, list_allocations)

    # save_allocation(list_allocations, str(round(max_happiness, 4)), path)
    save_data_to_xlsx(file, list_hh_wishes, list_flats, list_allocations, list_weights, max_happiness, "opt")


if __name__ == '__main__':
    full_start = datetime.now()
    print("Start: " + str(full_start))
    # for i in range(20):
    with Pool(10) as p:
        p.map(main_method, range(0, 1))

    print("--------------------------------------")
    print("Ende: " + str(datetime.now()))
    full_diff = datetime.now() - full_start
    print(str(full_diff.seconds / 60) + " mins")
