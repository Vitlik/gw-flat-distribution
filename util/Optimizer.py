import copy

from util.Calculator import calc_happiness
from util.helper import swap_flats


def optimize_allocations(hh_wishes, flats, weights, allocations, swap_real_flats = True):
    max_happiness = calc_happiness(hh_wishes, flats, weights, allocations)
    best_allocation = copy.deepcopy(allocations)

    no_optimization_possible = False

    while not no_optimization_possible:
        current_allocations = copy.deepcopy(best_allocation)
        swap_happened = False
        for alloc_main in best_allocation:
            # print("Betrachte Haushalt: " + str(alloc_main))
            for alloc_sec in best_allocation:
                if alloc_main < 1000 and alloc_main < alloc_sec \
                        and flats[current_allocations[alloc_main].wg_id].flat_type == flats[current_allocations[alloc_sec].wg_id].flat_type \
                        and (swap_real_flats or (not swap_real_flats and not (alloc_main < 1000 and alloc_sec < 1000)
                                                 and (hh_wishes[alloc_main].wbs == flats[current_allocations[alloc_sec].wg_id].wbs))):
                    swap_flats(alloc_main, alloc_sec, current_allocations, flats)
                    new_happiness = calc_happiness(hh_wishes, flats, weights, current_allocations)
                    if new_happiness > max_happiness:
                        print(
                            "Bessere Zuordnung gefunden. Die Haushalte " + str(alloc_main) + " und " + str(alloc_sec)
                            + " tauschen ihre " + str(flats[current_allocations[alloc_main].wg_id].flat_type) + " ZiWg mit den IDs "
                            + str(best_allocation[alloc_main].wg_id) + " und "
                            + str(best_allocation[alloc_sec].wg_id) + ". Glück von " + str(round(max_happiness, 4))
                            + " auf " + str(round(new_happiness, 4)) + " erhöht.")
                        if swap_real_flats:
                            print("    " + hh_wishes[alloc_main].name + " (" + best_allocation[alloc_main].wg_id + ") wechselt mit "
                                  + hh_wishes[alloc_sec].name + " (" + best_allocation[alloc_sec].wg_id +")")
                        else:
                            print("    " + hh_wishes[alloc_main].name + " wechselt von " 
                                  + best_allocation[alloc_main].wg_id + " zu " + current_allocations[alloc_main].wg_id)
                        swap_happened = True
                        best_allocation = copy.deepcopy(current_allocations)
                        max_happiness = copy.deepcopy(new_happiness)
                        # save_allocation(best_allocation, "_tmp")  # secure progress
                        break
                    else:
                        current_allocations = copy.deepcopy(best_allocation)
            if swap_happened:
                break
        if not swap_happened:
            no_optimization_possible = True

    print("Optimum gefunden mit einem Glückswert von: " + str(max_happiness))
    return best_allocation
