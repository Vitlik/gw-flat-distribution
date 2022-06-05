from util.Calculator import calc_happiness
from util.helper import swap_flats


def optimize_allocations(hh_wishes, flats, weights, allocations):
    max_happiness = calc_happiness(hh_wishes, flats, weights, allocations)

    no_optimization_possible = False

    while not no_optimization_possible:
        current_allocations = dict(allocations)
        swap_happened = False
        for alloc_main in current_allocations:
            print("Betrachte Haushalt: " + str(alloc_main))
            for alloc_sec in current_allocations:
                if alloc_main <= 9000 and alloc_main < alloc_sec and flats[current_allocations[alloc_main].wg_id].flat_type == \
                        flats[current_allocations[alloc_sec].wg_id].flat_type:
                    swap_flats(alloc_main, alloc_sec, current_allocations)
                    new_happiness = calc_happiness(hh_wishes, flats, weights, current_allocations)
                    if new_happiness > max_happiness:
                        print(
                            "Bessere Zuordnung gefunden. Die Haushalte " + str(alloc_main) + " und " + str(alloc_sec)
                            + " tauschen ihre " + flats[current_allocations[alloc_main].wg_id].flat_type + " "
                            + str(current_allocations[alloc_main].wg_id) + " und "
                            + str(current_allocations[alloc_sec].wg_id) + ". Glück von " + str(round(max_happiness, 4))
                            + " auf " + str(round(new_happiness, 4)) + " erhöht.")
                        swap_happened = True
                        allocations = dict(current_allocations)
                        max_happiness = new_happiness
                        break
                    else:
                        current_allocations = dict(allocations)
            if swap_happened:
                break
        if not swap_happened:
            no_optimization_possible = True
    return max_happiness
