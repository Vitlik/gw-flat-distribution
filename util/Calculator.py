import copy
from random import randrange

from objects.Allocation import Allocation
from objects.HappyNumbers import HappyNumbers


def init_distribution(hh_wishes, flats, allocations):
    flat1 = []
    flat2 = []
    flat3 = []
    flat4 = []
    flat5 = []
    flat3k = []

    for flat_id in flats:
        if flats[flat_id].distribution == "Programm":
            if flats[flat_id].flat_type == 1.5:
                flat1.append(flat_id)
            elif flats[flat_id].flat_type == 2.5:
                flat2.append(flat_id)
            elif flats[flat_id].flat_type == 3.5:
                flat3.append(flat_id)
            elif flats[flat_id].flat_type == 4.5:
                flat4.append(flat_id)
            elif flats[flat_id].flat_type == 5.5:
                flat5.append(flat_id)
            elif flats[flat_id].flat_type == "3,5k":
                flat3k.append(flat_id)

    for hh_id in hh_wishes:
        if hh_wishes[hh_id].flat_type == 1.5:
            num = randrange(0, len(flat1))
            allocations[hh_id] = Allocation(hh_id, flat1[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flat1.remove(flat1[num])
        elif hh_wishes[hh_id].flat_type == 2.5:
            num = randrange(0, len(flat2))
            allocations[hh_id] = Allocation(hh_id, flat2[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flat2.remove(flat2[num])
        elif hh_wishes[hh_id].flat_type == 3.5:
            num = randrange(0, len(flat3))
            allocations[hh_id] = Allocation(hh_id, flat3[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flat3.remove(flat3[num])
        elif hh_wishes[hh_id].flat_type == 4.5:
            num = randrange(0, len(flat4))
            allocations[hh_id] = Allocation(hh_id, flat4[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flat4.remove(flat4[num])
        elif hh_wishes[hh_id].flat_type == 5.5:
            num = randrange(0, len(flat5))
            allocations[hh_id] = Allocation(hh_id, flat5[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flat5.remove(flat5[num])
        elif hh_wishes[hh_id].flat_type == "3,5k":
            num = randrange(0, len(flat3k))
            allocations[hh_id] = Allocation(hh_id, flat3k[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flat3k.remove(flat3k[num])

    # fülle restliche Wohnungen mit Dummy Haushalten
    for flat_id2 in flat1 + flat2 + flat3 + flat4 + flat5 + flat3k:
        if flat_id2[:1] == "R":
            numeric_wg_id = 1000
        elif flat_id2[:1] == "P":
            numeric_wg_id = 2000
        elif flat_id2[:1] == "W":
            numeric_wg_id = 3000

        numeric_wg_id += int(flat_id2[2:5])

        allocations[numeric_wg_id] = Allocation(numeric_wg_id, flat_id2)
        allocations[numeric_wg_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


def calc_distance(flat1, flat2):
    dic = {}
    if flat1.id[:1] != flat2.id[:1]:  # wenn in einem anderen Gebäude, dann maximale Distanz
        dic["floor_diff"] = 999
        dic["flat_diff"] = 999
    else:
        dic["floor_diff"] = int(flat1.id[2:3]) - int(flat2.id[2:3])
        dic["flat_diff"] = int(flat1.id[3:5]) - int(flat2.id[3:5])
    return dic

# Weight from 1 (indifferent) to 5 (very important)
def norm_weight(weight):
    return (weight - 1) / 4


def calc_happiness(hh_wishes, flats, weights, allocations):
    for alloc in allocations:
        if alloc < 1000:
            hh = hh_wishes[alloc]
            flat = flats[allocations[alloc].wg_id]

            # Punkt happiness
            if hh.punkt is not None and hh.punkt_weight is not None and \
                    norm_weight(hh.punkt_weight) > 0 and \
                    ((hh.punkt == 1 and flat.building == "Punkt") or (hh.punkt == 0 and flat.building != "Punkt")):
                allocations[alloc].happy_numbers.punkt = norm_weight(hh.punkt_weight) * weights["Gebäude"]
            else:
                allocations[alloc].happy_numbers.punkt = 0

            # Winkel happiness
            if hh.winkel is not None and hh.winkel_weight is not None and \
                    norm_weight(hh.winkel_weight) > 0 and \
                    ((hh.winkel == 1 and flat.building == 'Winkel') or (hh.winkel == 0 and flat.building != 'Winkel')):
                allocations[alloc].happy_numbers.winkel = norm_weight(hh.winkel_weight) * weights["Gebäude"]
            else:
                allocations[alloc].happy_numbers.winkel = 0

            # Riegel happiness
            if hh.riegel is not None and hh.riegel_weight is not None and \
                    norm_weight(hh.riegel_weight) > 0 and \
                    ((hh.riegel == 1 and flat.building == 'Riegel') or (hh.riegel == 0 and flat.building != 'Riegel')):
                allocations[alloc].happy_numbers.riegel = norm_weight(hh.riegel_weight) * weights["Gebäude"]
            else:
                allocations[alloc].happy_numbers.riegel = 0

            # eg happiness
            if hh.eg is not None and hh.eg_weight is not None and \
                    norm_weight(hh.eg_weight) > 0 and \
                    ((hh.eg == 1 and flat.floor == 'EG') or (hh.eg == 0 and flat.floor != 'EG')):
                allocations[alloc].happy_numbers.eg = norm_weight(hh.eg_weight) * weights["Etage"]
            else:
                allocations[alloc].happy_numbers.eg = 0

            # og1 happiness
            if hh.og1 is not None and hh.og1_weight is not None and \
                    norm_weight(hh.og1_weight) > 0 and \
                    ((hh.og1 == 1 and flat.floor == 'OG1') or (hh.og1 == 0 and flat.floor != 'OG1')):
                allocations[alloc].happy_numbers.og1 = norm_weight(hh.og1_weight) * weights["Etage"]
            else:
                allocations[alloc].happy_numbers.og1 = 0

            # og2 happiness
            if hh.og2 is not None and hh.og2_weight is not None and \
                    norm_weight(hh.og2_weight) > 0 and \
                    ((hh.og2 == 1 and flat.floor == 'OG2') or (hh.og2 == 0 and flat.floor != 'OG2')):
                allocations[alloc].happy_numbers.og2 = norm_weight(hh.og2_weight) * weights["Etage"]
            else:
                allocations[alloc].happy_numbers.og2 = 0

            # og3 happiness
            if hh.og3 is not None and hh.og3_weight is not None and \
                    norm_weight(hh.og3_weight) > 0 and \
                    ((hh.og3 == 1 and flat.floor == 'OG3') or (hh.og3 == 0 and flat.floor != 'OG3')):
                allocations[alloc].happy_numbers.og3 = norm_weight(hh.og3_weight) * weights["Etage"]
            else:
                allocations[alloc].happy_numbers.og3 = 0

            # small_flat happiness
            if hh.small_flat is not None and norm_weight(hh.small_flat) > 0 and \
                    flat.small == 'Ja':
                allocations[alloc].happy_numbers.small_flat = norm_weight(hh.small_flat) * weights["kleine_wg"]
            else:
                allocations[alloc].happy_numbers.small_flat = 0

            # wheelchair_suitable happiness
            if hh.wheelchair_suitable is not None and hh.wheelchair_suitable_weight is not None and \
                    norm_weight(hh.wheelchair_suitable_weight) > 0 and \
                    (hh.wheelchair_suitable == 1 and flat.wheelchair_suitable == 'OG3'):
                allocations[alloc].happy_numbers.wheelchair = norm_weight(hh.wheelchair_suitable_weight) * weights["rollitauglich"]
            else:
                allocations[alloc].happy_numbers.wheelchair = 0

            # neighbour happiness
            if hh.neighbour is not None and hh.neighbour_weight is not None and hh.neighbour_id is not None and \
                    hh.neighbour == 1 and norm_weight(hh.neighbour_weight) > 0:

                if hh.neighbour_id in allocations:
                    dic = calc_distance(flat, flats[allocations[hh.neighbour_id].wg_id])
                else:
                    raise Exception("Wunschnachbar mit ID " + str(hh.neighbour_id) + " von Haushalt \"" + hh.name +
                                    "\" nicht in der Haushaltsliste gefunden. Bitte hinzufügen.")
                neighbor_happiness_factor = 0
                if abs(dic["floor_diff"]) == 0 and abs(dic["flat_diff"]) <= 1:
                    neighbor_happiness_factor = 1
                elif abs(dic["floor_diff"]) == 0 and abs(dic["flat_diff"]) == 2:
                    neighbor_happiness_factor = 0.9
                elif abs(dic["floor_diff"]) == 0 and abs(dic["flat_diff"]) == 3:
                    neighbor_happiness_factor = 0.8

                elif abs(dic["floor_diff"]) == 1 and abs(dic["flat_diff"]) <= 1:
                    neighbor_happiness_factor = 0.15
                elif abs(dic["floor_diff"]) == 1 and abs(dic["flat_diff"]) == 2:
                    neighbor_happiness_factor = 0.1

                allocations[alloc].happy_numbers.neighbour = neighbor_happiness_factor * norm_weight(hh.neighbour_weight) * weights["Nachbar"]
            else:
                allocations[alloc].happy_numbers.neighbour = 0

            # Hund
            distance_to_next_dog = 999
            for neighbor in allocations:  # finde nächste Hundewohnung
                if neighbor < 1000 and neighbor != alloc and hh_wishes[neighbor].dog == 1:
                    flat_neighbor2 = flats[allocations[neighbor].wg_id]
                    dic = calc_distance(flat, flat_neighbor2)
                    if dic["floor_diff"] == 0 and abs(dic["flat_diff"]) < distance_to_next_dog:
                        distance_to_next_dog = abs(dic["flat_diff"])
            allocations[alloc].happy_numbers.distance_to_next_dog = distance_to_next_dog
            # rate happiness from distance
            dog_happiness_factor = 0
            if hh.dog == 0 and (hh.dog_close_weight is None or norm_weight(hh.dog_close_weight) == 0):
                allocations[alloc].happy_numbers.dog = 0
            elif hh.dog == 1 or (hh.dog == 0 and hh.dog_close == 1):
                if distance_to_next_dog == 1:
                    dog_happiness_factor = 1
                elif distance_to_next_dog == 2:
                    dog_happiness_factor = 0.9
                elif distance_to_next_dog == 3:
                    dog_happiness_factor = 0.7
                elif distance_to_next_dog == 4:
                    dog_happiness_factor = 0.5
                elif distance_to_next_dog == 5:
                    dog_happiness_factor = 0.3
                elif distance_to_next_dog == 6:
                    dog_happiness_factor = 0.1
                else:
                    dog_happiness_factor = 0
                # calculate weighted happiness
                if hh.dog == 1:
                    allocations[alloc].happy_numbers.dog = dog_happiness_factor * weights["Hund"]
                else:
                    allocations[alloc].happy_numbers.dog = \
                        dog_happiness_factor * norm_weight(hh.dog_close_weight) * weights["Hund"] * \
                        (1 + weights["Hundeallergie"] * hh.dog_allergy)  # durch die Multiplikation mit hh.dog_allergy hat der Eintrag nur bei Allergie einen Effekt
            elif hh.dog == 0 and hh.dog_close == 0:
                if distance_to_next_dog == 1:
                    dog_happiness_factor = 0
                elif distance_to_next_dog == 2:
                    dog_happiness_factor = 0.1
                elif distance_to_next_dog == 3:
                    dog_happiness_factor = 0.3
                elif distance_to_next_dog == 4:
                    dog_happiness_factor = 0.5
                elif distance_to_next_dog == 5:
                    dog_happiness_factor = 0.7
                elif distance_to_next_dog == 6:
                    dog_happiness_factor = 0.9
                else:
                    dog_happiness_factor = 1
                # calculate weighted happiness
                allocations[alloc].happy_numbers.dog = \
                    dog_happiness_factor * norm_weight(hh.dog_close_weight) * weights["Hund"] * \
                    (1 + weights[
                        "Hundeallergie"] * hh.dog_allergy)  # durch die Multiplikation mit hh.dog_allergy hat der Eintrag nur bei Allergie einen Effekt

            # Katze
            distance_to_next_cat = 999
            for neighbor in allocations:  # finde nächste Katzenwohnung
                if neighbor < 1000 and neighbor != alloc and hh_wishes[neighbor].cat == 1:
                    flat_neighbor2 = flats[allocations[neighbor].wg_id]
                    dic = calc_distance(flat, flat_neighbor2)
                    if dic["floor_diff"] == 0 and abs(dic["flat_diff"]) < distance_to_next_cat:
                        distance_to_next_cat = abs(dic["flat_diff"])
            allocations[alloc].happy_numbers.distance_to_next_cat = distance_to_next_cat
            # rate happiness from distance
            cat_happiness_factor = 0
            if hh.cat == 0 and (hh.cat_close_weight is None or norm_weight(hh.cat_close_weight) == 0):
                allocations[alloc].happy_numbers.cat = 0
            elif hh.cat == 1 or (hh.cat == 0 and hh.cat_close == 1):
                if distance_to_next_cat == 1:
                    cat_happiness_factor = 1
                elif distance_to_next_cat == 2:
                    cat_happiness_factor = 0.9
                elif distance_to_next_cat == 3:
                    cat_happiness_factor = 0.7
                elif distance_to_next_cat == 4:
                    cat_happiness_factor = 0.5
                elif distance_to_next_cat == 5:
                    cat_happiness_factor = 0.3
                elif distance_to_next_cat == 6:
                    cat_happiness_factor = 0.1
                else:
                    cat_happiness_factor = 0
                # calculate weighted happiness
                if hh.cat == 1:
                    allocations[alloc].happy_numbers.cat = cat_happiness_factor * weights["Katze"]
                else:
                    allocations[alloc].happy_numbers.cat = \
                        cat_happiness_factor * norm_weight(hh.cat_close_weight) * weights["Katze"] * \
                        (1 + weights[
                            "Katzenallergie"] * hh.cat_allergy)  # durch die Multiplikation mit hh.cat_allergy hat der Eintrag nur bei Allergie einen Effekt
            elif hh.cat == 0 and hh.cat_close == 0:
                if distance_to_next_cat == 1:
                    cat_happiness_factor = 0
                elif distance_to_next_cat == 2:
                    cat_happiness_factor = 0.1
                elif distance_to_next_cat == 3:
                    cat_happiness_factor = 0.3
                elif distance_to_next_cat == 4:
                    cat_happiness_factor = 0.5
                elif distance_to_next_cat == 5:
                    cat_happiness_factor = 0.7
                elif distance_to_next_cat == 6:
                    cat_happiness_factor = 0.9
                else:
                    cat_happiness_factor = 1
                # calculate weighted happiness
                allocations[alloc].happy_numbers.cat = \
                    cat_happiness_factor * norm_weight(hh.cat_close_weight) * weights["Katze"] * \
                    (1 + weights[
                        "Katzenallergie"] * hh.cat_allergy)  # durch die Multiplikation mit hh.cat_allergy hat der Eintrag nur bei Allergie einen Effekt

            # smoker happiness
            if hh.smoker is not None and (hh.smoker == 1 or (hh.smoker == 0 and norm_weight(hh.smoker_aversion_weight) > 0)):
                distance_to_next_smoker = 999
                for neighbor in allocations:  # finde nächste Raucherwohnung
                    if neighbor < 1000 and neighbor != alloc and hh_wishes[neighbor].smoker == 1:
                        flat_neighbor2 = flats[allocations[neighbor].wg_id]
                        dic = calc_distance(flat, flat_neighbor2)
                        if dic["floor_diff"] == 0 and abs(dic["flat_diff"]) < distance_to_next_smoker:
                            distance_to_next_smoker = abs(dic["flat_diff"])
                        elif dic["floor_diff"] > 0 and abs(dic["flat_diff"]) <= 5:  # Raucher wohnt unter mir
                            distance_to_next_smoker = 2
                        elif dic["floor_diff"] > 0 and abs(dic["flat_diff"]) <= 10:  # Raucher wohnt unter mir, aber mehr horizontal versetzt
                            distance_to_next_smoker = 5
                allocations[alloc].happy_numbers.distance_to_next_smoker = distance_to_next_smoker
                # rate happiness from distance
                smoker_happiness_factor = 0
                if hh.smoker == 0 and (hh.smoker_aversion_weight is None or norm_weight(hh.smoker_aversion_weight) == 0):
                    allocations[alloc].happy_numbers.smoker = 0
                elif hh.smoker == 1:
                    if distance_to_next_smoker == 1:
                        smoker_happiness_factor = 2
                    elif distance_to_next_smoker == 2:
                        smoker_happiness_factor = 1
                    elif distance_to_next_smoker <= 4:
                        smoker_happiness_factor = 0.6
                    elif distance_to_next_smoker <= 6:
                        smoker_happiness_factor = 0.3
                    elif distance_to_next_smoker <= 8:
                        smoker_happiness_factor = 0.1
                    else:
                        smoker_happiness_factor = 0

                    # calculate weighted happiness
                    allocations[alloc].happy_numbers.smoker = \
                        smoker_happiness_factor * weights["Raucher"]

                elif hh.cat == 0:
                    if distance_to_next_smoker == 1:
                        smoker_happiness_factor = 0
                    elif distance_to_next_smoker == 2:
                        smoker_happiness_factor = 0.2
                    elif distance_to_next_smoker <= 4:
                        smoker_happiness_factor = 0.5
                    elif distance_to_next_smoker <= 6:
                        smoker_happiness_factor = 0.9
                    else:
                        smoker_happiness_factor = 1

                    # calculate weighted happiness
                    allocations[alloc].happy_numbers.smoker = \
                        smoker_happiness_factor * norm_weight(hh.smoker_aversion_weight) * weights["Raucher"]
            else:
                allocations[alloc].happy_numbers.smoker = 0

            # Wunschwohnung
            if hh.specific_flat_wish is not None and hh.specific_flat_wish == 1:
                if hh.specific_flat1 == flat.id:
                    allocations[alloc].happy_numbers.specific_flat = weights["konkrete_wg1"]
                elif hh.specific_flat2 == flat.id:
                    allocations[alloc].happy_numbers.specific_flat = weights["konkrete_wg2"]
                elif hh.specific_flat3 == flat.id:
                    allocations[alloc].happy_numbers.specific_flat = weights["konkrete_wg3"]
                else:
                    allocations[alloc].happy_numbers.specific_flat = 0
            else:
                allocations[alloc].happy_numbers.specific_flat = 0

            allocations[alloc].happy_numbers.sum = \
                allocations[alloc].happy_numbers.punkt + \
                allocations[alloc].happy_numbers.winkel + \
                allocations[alloc].happy_numbers.riegel + \
                allocations[alloc].happy_numbers.eg + \
                allocations[alloc].happy_numbers.og1 + \
                allocations[alloc].happy_numbers.og2 + \
                allocations[alloc].happy_numbers.og3 + \
                allocations[alloc].happy_numbers.small_flat + \
                allocations[alloc].happy_numbers.wheelchair + \
                allocations[alloc].happy_numbers.neighbour + \
                allocations[alloc].happy_numbers.dog + \
                allocations[alloc].happy_numbers.cat + \
                allocations[alloc].happy_numbers.smoker + \
                allocations[alloc].happy_numbers.specific_flat

    # calc overall happiness
    happiness = 0
    for alloc in allocations:
        if alloc < 1000:
            happiness = happiness \
                        + allocations[alloc].happy_numbers.punkt \
                        + allocations[alloc].happy_numbers.winkel \
                        + allocations[alloc].happy_numbers.riegel \
                        + allocations[alloc].happy_numbers.eg \
                        + allocations[alloc].happy_numbers.og1 \
                        + allocations[alloc].happy_numbers.og2 \
                        + allocations[alloc].happy_numbers.og3 \
                        + allocations[alloc].happy_numbers.small_flat \
                        + allocations[alloc].happy_numbers.wheelchair \
                        + allocations[alloc].happy_numbers.neighbour \
                        + allocations[alloc].happy_numbers.dog \
                        + allocations[alloc].happy_numbers.cat \
                        + allocations[alloc].happy_numbers.smoker \
                        + allocations[alloc].happy_numbers.specific_flat
    return happiness
