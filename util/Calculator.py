from objects.Allocation import Allocation
from objects.HappyNumbers import HappyNumbers


def init_distribution(hh_wishes, flats, allocations):
    print("Doing: init_distribution")
    allocated_flats = {}
    free_wg = 0
    for hh_id in hh_wishes:
        for flat_id in flats:
            if not allocated_flats.__contains__(flat_id) and hh_wishes[hh_id].flat_type == flats[flat_id].flat_type:
                free_wg = flats[flat_id].id
                break
        allocations[hh_wishes[hh_id].id] = Allocation(hh_wishes[hh_id].id, free_wg)
        allocations[hh_wishes[hh_id].id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0)
        allocated_flats[free_wg] = None
    for flat_id in flats:
        if not allocated_flats.__contains__(flat_id):
            allocations[9000 + flat_id] = Allocation(9000 + flat_id, free_wg)
            allocations[9000 + flat_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0)
            allocated_flats[free_wg] = None


def calc_distance(flat1, flat2):
    return abs(flat1.id - flat2.id)


def calc_happiness(hh_wishes, flats, weights, allocations):
    happiness = 0
    for alloc in allocations:
        if alloc <= 9000:
            hh = hh_wishes[alloc]
            flat = flats[allocations[alloc].wg_id]

            # building happiness
            if hh.building_pref == flat.building:
                allocations[alloc].happy_numbers.building_pref = 1 * (int(hh.building_weight) / 10) * weights["Gebäude"]

            # floor happiness
            max_floor = 4 if flat.building == "Punkt" else 3
            if hh.floor_pref == "Eher höher":
                floor_satisfaction = (flat.floor - 1) / (max_floor - 1)
            else:
                floor_satisfaction = (((flat.floor - 1) / (max_floor - 1)) - 1) * (-1)
            allocations[alloc].happy_numbers.floor_pref = floor_satisfaction * (int(hh.floor_weight) / 10) * weights[
                "Etage"]

            # close neighbor
            if not hh.neighbour_pref:  # neighbor set
                flat_neighbor = flats[allocations[hh.neighbour_pref].wg_id]
                if calc_distance(flat, flat_neighbor) < 3:
                    allocations[alloc].happy_numbers.neighbour_pref = 1 * (int(hh.neighbour_weight) / 10) * weights[
                        "Nachbar"]

            # small flat
            if hh.small_flat_pref == "Ja" and flat.small == "Ja":
                allocations[alloc].happy_numbers.small_flat_pref = 1 * (int(hh.small_flat_weight) / 10) * weights[
                    "kleine_wg"]

            # Haustier
            distance_to_next_animal = 999
            for neighbor in allocations:  # calculate closest animal flat
                if neighbor <= 9000 and neighbor != alloc and hh_wishes[neighbor].animal_pref == "Hund/Katze vorhanden":
                    flat_neighbor2 = flats[allocations[neighbor].wg_id]
                    dist = calc_distance(flat, flat_neighbor2)
                    if dist < distance_to_next_animal:
                        distance_to_next_animal = dist
            allocations[alloc].happy_numbers.distance_to_next_animal = distance_to_next_animal
            # rate happiness from distance
            distance_to_animal_happiness = 0
            if hh.animal_pref in ["Hund/Katze vorhanden", "Gerne in der Nähe"]:
                if distance_to_next_animal < 20:
                    distance_to_animal_happiness = 1
                if distance_to_next_animal < 40:
                    distance_to_animal_happiness = 0.5
            elif hh.animal_pref == "Gerne in der Nähe":
                if distance_to_next_animal > 20:
                    distance_to_animal_happiness = 0.5
                if distance_to_next_animal > 40:
                    distance_to_animal_happiness = 1
            elif hh.animal_pref == "Allergiker:in - bitte weit weg":
                if distance_to_next_animal > 20:
                    distance_to_animal_happiness = 0.5
                if distance_to_next_animal > 40:
                    distance_to_animal_happiness = 1
            # calculate weighted happiness
            allocations[alloc].happy_numbers.animal_pref = \
                distance_to_animal_happiness * (int(hh.animal_weight) / 10) * weights["Haustier"]

            # favorite flat
            if hh.specific_flat_pref == flat.id:
                allocations[alloc].happy_numbers.animal_pref = 1 * (int(hh.specific_flat_weight) / 10) * weights[
                    "konkrete_wg"]


    # calc overall happiness
    for alloc in allocations:
        happiness = happiness \
                    + allocations[alloc].happy_numbers.building_pref \
                    + allocations[alloc].happy_numbers.floor_pref \
                    + allocations[alloc].happy_numbers.neighbour_pref \
                    + allocations[alloc].happy_numbers.small_flat_pref \
                    + allocations[alloc].happy_numbers.animal_pref \
                    + allocations[alloc].happy_numbers.specific_flat_pref
    return happiness
