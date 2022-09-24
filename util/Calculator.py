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
    flatClW2 = []
    flatClR = []
    flatClAus = []

    for flat_id in flats:
        if flats[flat_id].distribution == "Programm":
            if flats[flat_id].flat_type == "1,5":
                flat1.append(flat_id)
            elif flats[flat_id].flat_type == "2,5":
                flat2.append(flat_id)
            elif flats[flat_id].flat_type == "3,5":
                flat3.append(flat_id)
            elif flats[flat_id].flat_type == "4,5":
                flat4.append(flat_id)
            elif flats[flat_id].flat_type == "5,5":
                flat5.append(flat_id)
            elif flats[flat_id].flat_type == "3,5k":
                flat3k.append(flat_id)
        elif flats[flat_id].distribution == "direkt":
            if flats[flat_id].flat_type == "ClusterW2":
                flatClW2.append(flat_id)
            if flats[flat_id].flat_type == "ClusterR":
                flatClR.append(flat_id)
            if flats[flat_id].flat_type == "ClusterAus":
                flatClAus.append(flat_id)

    for hh_id in hh_wishes:
        if hh_wishes[hh_id].flat_type == "1,5":
            num = randrange(0, len(flat1))
            allocations[hh_id] = Allocation(hh_id, flat1[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flat1.remove(flat1[num])
        elif hh_wishes[hh_id].flat_type == "2,5":
            num = randrange(0, len(flat2))
            allocations[hh_id] = Allocation(hh_id, flat2[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flat2.remove(flat2[num])
        elif hh_wishes[hh_id].flat_type == "3,5":
            num = randrange(0, len(flat3))
            allocations[hh_id] = Allocation(hh_id, flat3[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flat3.remove(flat3[num])
        elif hh_wishes[hh_id].flat_type == "4,5":
            num = randrange(0, len(flat4))
            allocations[hh_id] = Allocation(hh_id, flat4[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flat4.remove(flat4[num])
        elif hh_wishes[hh_id].flat_type == "5,5":
            num = randrange(0, len(flat5))
            allocations[hh_id] = Allocation(hh_id, flat5[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flat5.remove(flat5[num])
        elif hh_wishes[hh_id].flat_type == "3,5k":
            num = randrange(0, len(flat3k))
            allocations[hh_id] = Allocation(hh_id, flat3k[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flat3k.remove(flat3k[num])
        elif hh_wishes[hh_id].flat_type == "ClusterW2":
            num = randrange(0, len(flatClW2))
            allocations[hh_id] = Allocation(hh_id, flatClW2[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flatClW2.remove(flatClW2[num])
        elif hh_wishes[hh_id].flat_type == "ClusterR":
            num = randrange(0, len(flatClR))
            allocations[hh_id] = Allocation(hh_id, flatClR[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flatClR.remove(flatClR[num])
        elif hh_wishes[hh_id].flat_type == "ClusterAus":
            num = randrange(0, len(flatClAus))
            allocations[hh_id] = Allocation(hh_id, flatClAus[num])
            allocations[hh_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            flatClAus.remove(flatClAus[num])

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
        allocations[numeric_wg_id].happy_numbers = HappyNumbers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


def calc_distance(flat1, flat2):
    dic = {}
    if flat1.id[:1] != flat2.id[:1]:  # wenn in einem anderen Gebäude, dann maximale Distanz
        dic["floor_diff"] = 999
        dic["flat_diff"] = 999
    else:
        if flat1.id[:1] != "P":
            dic["floor_diff"] = int(flat1.id[2:3]) - int(flat2.id[2:3])
            dic["flat_diff"] = int(flat1.id[3:5]) - int(flat2.id[3:5])
        else:  # im Punkt liegen sich Wohnungen gegenüber. Dadurch sind z.B. P.201 und P.211 direkte Nachbarn
            dic["floor_diff"] = int(flat1.id[2:3]) - int(flat2.id[2:3])
            wg1 = int(flat1.id[3:5])
            wg2 = int(flat2.id[3:5])
            if (wg1 <= 6 and wg2 <= 6) or (wg1 >= 7 and wg2 >= 7):
                dic["flat_diff"] = int(flat1.id[3:5]) - int(flat2.id[3:5])
            elif (wg1 <= 3 and wg2 >= 9) or (wg2 <= 3 and wg1 >= 9) or \
                    (4 <= wg1 <= 6 and 7 <= wg2 <= 9) or (4 <= wg2 <= 6 and 7 <= wg1 <= 9):
                dic["flat_diff"] = 2
            else:
                dic["flat_diff"] = 4
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
                allocations[alloc].happy_numbers.punkt = norm_weight(hh.punkt_weight) * weights["Punkt"]
            else:
                allocations[alloc].happy_numbers.punkt = 0

            # Winkel happiness
            if hh.winkel is not None and hh.winkel_weight is not None and \
                    norm_weight(hh.winkel_weight) > 0 and \
                    ((hh.winkel == 1 and flat.building == 'Winkel') or (hh.winkel == 0 and flat.building != 'Winkel')):
                allocations[alloc].happy_numbers.winkel = norm_weight(hh.winkel_weight) * weights["Winkel"]
            else:
                allocations[alloc].happy_numbers.winkel = 0

            # Riegel happiness
            if hh.riegel is not None and hh.riegel_weight is not None and \
                    norm_weight(hh.riegel_weight) > 0 and \
                    ((hh.riegel == 1 and flat.building == 'Riegel') or (hh.riegel == 0 and flat.building != 'Riegel')):
                allocations[alloc].happy_numbers.riegel = norm_weight(hh.riegel_weight) * weights["Riegel"]
            else:
                allocations[alloc].happy_numbers.riegel = 0

            # eg happiness
            if hh.eg is not None and hh.eg_weight is not None and \
                    norm_weight(hh.eg_weight) > 0 and \
                    ((hh.eg == 1 and flat.floor == 'EG') or (hh.eg == 0 and flat.floor != 'EG')):
                allocations[alloc].happy_numbers.eg = norm_weight(hh.eg_weight) * weights["EG"]
            else:
                allocations[alloc].happy_numbers.eg = 0

            # og1 happiness
            if hh.og1 is not None and hh.og1_weight is not None and \
                    norm_weight(hh.og1_weight) > 0 and \
                    ((hh.og1 == 1 and flat.floor == 'OG1') or (hh.og1 == 0 and flat.floor != 'OG1')):
                allocations[alloc].happy_numbers.og1 = norm_weight(hh.og1_weight) * weights["1OG"]
            else:
                allocations[alloc].happy_numbers.og1 = 0

            # og2 happiness
            if hh.og2 is not None and hh.og2_weight is not None and \
                    norm_weight(hh.og2_weight) > 0 and \
                    ((hh.og2 == 1 and flat.floor == 'OG2') or (hh.og2 == 0 and flat.floor != 'OG2')):
                allocations[alloc].happy_numbers.og2 = norm_weight(hh.og2_weight) * weights["2OG"]
            else:
                allocations[alloc].happy_numbers.og2 = 0

            # og3 happiness
            if hh.og3 is not None and hh.og3_weight is not None and \
                    norm_weight(hh.og3_weight) > 0 and \
                    ((hh.og3 == 1 and flat.floor == 'OG3') or (hh.og3 == 0 and flat.floor != 'OG3')):
                allocations[alloc].happy_numbers.og3 = norm_weight(hh.og3_weight) * weights["3OG"]
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
                allocations[alloc].happy_numbers.wheelchair = norm_weight(hh.wheelchair_suitable_weight) * weights[
                    "rollitauglich"]
            else:
                allocations[alloc].happy_numbers.wheelchair = 0

            # neighbour happiness
            if hh.neighbour is not None and hh.neighbour_weight is not None and hh.neighbour_id is not None and \
                    hh.neighbour == 1 and norm_weight(hh.neighbour_weight) > 0:

                if hh.neighbour_id in allocations:
                    dic = calc_distance(flat, flats[allocations[hh.neighbour_id].wg_id])
                else:
                    raise Exception("Wunschnachbar mit ID " + str(hh.neighbour_id) + " von Haushalt " + str(hh.id) +
                                    " \"" + hh.name + "\" nicht in der Haushaltsliste gefunden. Bitte hinzufügen.")
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

                allocations[alloc].happy_numbers.neighbour = neighbor_happiness_factor * norm_weight(
                    hh.neighbour_weight) * weights["Nachbar"]
            else:
                allocations[alloc].happy_numbers.neighbour = 0

            # Hund
            distance_to_next_dog = 999
            next_dog_flat = ""
            for neighbor in allocations:  # finde nächste Hundewohnung
                if neighbor < 1000 and neighbor != alloc and hh_wishes[neighbor].dog == 1:
                    flat_neighbor2 = flats[allocations[neighbor].wg_id]
                    if next_dog_flat == "":
                        next_dog_flat = str(flat_neighbor2.id)
                    dic = calc_distance(flat, flat_neighbor2)
                    if dic["floor_diff"] == 0 and abs(dic["flat_diff"]) < distance_to_next_dog:
                        distance_to_next_dog = abs(dic["flat_diff"])
                        next_dog_flat = str(flat_neighbor2.id)
            allocations[alloc].happy_numbers.distance_to_next_dog = distance_to_next_dog
            allocations[alloc].happy_numbers.next_dog_flat = next_dog_flat
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
                        (1 + weights[
                            "Hundeallergie"] * hh.dog_allergy)  # durch die Multiplikation mit hh.dog_allergy hat der Eintrag nur bei Allergie einen Effekt
            elif hh.dog == 0 and hh.dog_close == 0:
                if distance_to_next_dog == 1:
                    dog_happiness_factor = 0
                elif distance_to_next_dog == 2:
                    dog_happiness_factor = 0.075
                elif distance_to_next_dog == 3:
                    dog_happiness_factor = 0.15
                elif distance_to_next_dog == 4:
                    dog_happiness_factor = 0.4
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
            next_cat_flat = ""
            for neighbor in allocations:  # finde nächste Katzenwohnung
                if neighbor < 1000 and neighbor != alloc and hh_wishes[neighbor].cat == 1:
                    flat_neighbor2 = flats[allocations[neighbor].wg_id]
                    if next_cat_flat == "":
                        next_cat_flat = str(flat_neighbor2.id)
                    dic = calc_distance(flat, flat_neighbor2)
                    if dic["floor_diff"] == 0 and abs(dic["flat_diff"]) < distance_to_next_cat:
                        distance_to_next_cat = abs(dic["flat_diff"])
                        next_cat_flat = str(flat_neighbor2.id)
            allocations[alloc].happy_numbers.distance_to_next_cat = distance_to_next_cat
            allocations[alloc].happy_numbers.next_cat_flat = next_cat_flat
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
            if hh.smoker is not None and (
                    hh.smoker == 1 or (hh.smoker == 0 and norm_weight(hh.smoker_aversion_weight) > 0)):
                distance_to_next_smoker = 999
                next_smoker_flat = ""
                for neighbor in allocations:  # finde nächste Raucherwohnung
                    if neighbor < 1000 and neighbor != alloc and hh_wishes[neighbor].smoker == 1:
                        flat_neighbor2 = flats[allocations[neighbor].wg_id]
                        dic = calc_distance(flat, flat_neighbor2)
                        if dic["floor_diff"] == 0 and abs(dic["flat_diff"]) < distance_to_next_smoker:
                            distance_to_next_smoker = abs(dic["flat_diff"])
                            next_smoker_flat = str(flat_neighbor2.id)
                        elif dic["floor_diff"] > 0 and abs(dic["flat_diff"]) <= 2:  # Raucher wohnt unter mir
                            distance_to_next_smoker = 1
                            next_smoker_flat = str(flat_neighbor2.id)
                        elif dic["floor_diff"] > 0 and abs(
                                dic["flat_diff"]) <= 4:  # Raucher wohnt unter mir, aber etwas weiter
                            distance_to_next_smoker = 2
                            next_smoker_flat = str(flat_neighbor2.id)
                        elif dic["floor_diff"] > 0 and abs(
                                dic["flat_diff"]) <= 10:  # Raucher wohnt unter mir, aber noch etwas weiter
                            distance_to_next_smoker = 3
                            next_smoker_flat = str(flat_neighbor2.id)
                allocations[alloc].happy_numbers.distance_to_next_smoker = distance_to_next_smoker
                allocations[alloc].happy_numbers.next_smoker_flat = next_smoker_flat
                # rate happiness from distance
                smoker_happiness_factor = 0
                if hh.smoker == 0 and (
                        hh.smoker_aversion_weight is None or norm_weight(hh.smoker_aversion_weight) == 0):
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

                else:  # not smoker and not indifferent to smokers
                    if distance_to_next_smoker == 1:
                        smoker_happiness_factor = 0
                    elif distance_to_next_smoker == 2:
                        smoker_happiness_factor = 0.1
                    elif distance_to_next_smoker <= 3:
                        smoker_happiness_factor = 0.3
                    elif distance_to_next_smoker <= 4:
                        smoker_happiness_factor = 0.5
                    elif distance_to_next_smoker <= 5:
                        smoker_happiness_factor = 0.7
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

            # initiale WBS Verteilung erfüllt
            if hh.wbs == flat.wbs:
                allocations[alloc].happy_numbers.wbs = weights["WBS-AB"]
            else:
                allocations[alloc].happy_numbers.wbs = 0

            # Engagement-Multiplikator
            eng_mult = 1 + hh.engagement * (weights["EngagementMultiplikator"] - 1)
            allocations[alloc].happy_numbers.punkt = allocations[alloc].happy_numbers.punkt * eng_mult
            allocations[alloc].happy_numbers.winkel = allocations[alloc].happy_numbers.winkel * eng_mult
            allocations[alloc].happy_numbers.riegel = allocations[alloc].happy_numbers.riegel * eng_mult
            allocations[alloc].happy_numbers.eg = allocations[alloc].happy_numbers.eg * eng_mult
            allocations[alloc].happy_numbers.og1 = allocations[alloc].happy_numbers.og1 * eng_mult
            allocations[alloc].happy_numbers.og2 = allocations[alloc].happy_numbers.og2 * eng_mult
            allocations[alloc].happy_numbers.og3 = allocations[alloc].happy_numbers.og3 * eng_mult
            allocations[alloc].happy_numbers.small_flat = allocations[alloc].happy_numbers.small_flat * eng_mult
            allocations[alloc].happy_numbers.wheelchair = allocations[alloc].happy_numbers.wheelchair * eng_mult
            allocations[alloc].happy_numbers.neighbour = allocations[alloc].happy_numbers.neighbour * eng_mult
            allocations[alloc].happy_numbers.dog = allocations[alloc].happy_numbers.dog * eng_mult
            allocations[alloc].happy_numbers.cat = allocations[alloc].happy_numbers.cat * eng_mult
            allocations[alloc].happy_numbers.smoker = allocations[alloc].happy_numbers.smoker * eng_mult
            allocations[alloc].happy_numbers.specific_flat = allocations[alloc].happy_numbers.specific_flat * eng_mult
            # kein wbs, da es nicht im persönlichen Interesse des Haushaltes, sondern des Grünen Weilers ist.

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
                allocations[alloc].happy_numbers.specific_flat + \
                allocations[alloc].happy_numbers.wbs

    # calc overall happiness
    happiness = 0
    for alloc in allocations:
        if alloc < 1000:
            happiness = happiness + allocations[alloc].happy_numbers.sum

    return happiness


def add_unfulfilled_wish(text, allocations, alloc_id):
    if allocations[alloc_id].happy_numbers.unfulfilled_wish1 == "" or allocations[
        alloc_id].happy_numbers.unfulfilled_wish1 == text:
        allocations[alloc_id].happy_numbers.unfulfilled_wish1 = text
    elif allocations[alloc_id].happy_numbers.unfulfilled_wish2 == "" or allocations[
        alloc_id].happy_numbers.unfulfilled_wish2 == text:
        allocations[alloc_id].happy_numbers.unfulfilled_wish2 = text
    elif allocations[alloc_id].happy_numbers.unfulfilled_wish3 == "" or allocations[
        alloc_id].happy_numbers.unfulfilled_wish3 == text:
        allocations[alloc_id].happy_numbers.unfulfilled_wish3 = text
    elif allocations[alloc_id].happy_numbers.unfulfilled_wish4 == "" or allocations[
        alloc_id].happy_numbers.unfulfilled_wish4 == text:
        allocations[alloc_id].happy_numbers.unfulfilled_wish4 = text
    elif allocations[alloc_id].happy_numbers.unfulfilled_wish5 == "" or allocations[
        alloc_id].happy_numbers.unfulfilled_wish5 == text:
        allocations[alloc_id].happy_numbers.unfulfilled_wish5 = text


def check_unfulfilled_wishes(hh_wishes, flats, weights, allocations):
    local_allocations = copy.deepcopy(allocations)

    for alloc in local_allocations:
        if alloc < 1000:
            hh = hh_wishes[alloc]
            flat = flats[local_allocations[alloc].wg_id]

            local_allocations[alloc].happy_numbers.unfulfilled_wish1 = ""
            local_allocations[alloc].happy_numbers.unfulfilled_wish2 = ""
            local_allocations[alloc].happy_numbers.unfulfilled_wish3 = ""
            local_allocations[alloc].happy_numbers.unfulfilled_wish4 = ""
            local_allocations[alloc].happy_numbers.unfulfilled_wish5 = ""
            local_allocations[alloc].happy_numbers.wbs_change = ""

            # Nicht einen Gebäude-Wunsch erfüllt
            # mind. ein bestimmtes Gebäude ist wichtig (4 oder 5)
            # keines der wichtigen Gebäudewünsche wurde erfüllt
            if ((hh.punkt_weight is not None and norm_weight(hh.punkt_weight) > 0.5) or \
                (hh.riegel_weight is not None and norm_weight(hh.riegel_weight) > 0.5) or \
                (hh.winkel_weight is not None and norm_weight(hh.winkel_weight) > 0.5)) \
                    and (local_allocations[alloc].happy_numbers.punkt / weights["Punkt"] +
                         local_allocations[alloc].happy_numbers.winkel / weights["Winkel"] +
                         local_allocations[alloc].happy_numbers.riegel / weights["Riegel"] < 0.5):
                add_unfulfilled_wish("Gebäudewunsch verletzt", local_allocations, alloc)

            # Nicht einen Etagen-Wunsch erfüllt
            # mind. eine bestimmte Etage ist wichtig (4 oder 5)
            # keines der wichtigen Etagenwünsche wurde erfüllt
            if ((hh.eg_weight is not None and norm_weight(hh.eg_weight) > 0.5) or \
                (hh.og1_weight is not None and norm_weight(hh.og1_weight) > 0.5) or \
                (hh.og2_weight is not None and norm_weight(hh.og2_weight) > 0.5) or \
                (hh.og3_weight is not None and norm_weight(hh.og3_weight) > 0.5)) \
                    and (local_allocations[alloc].happy_numbers.eg / weights["EG"] +
                         local_allocations[alloc].happy_numbers.og1 / weights["1OG"] +
                         local_allocations[alloc].happy_numbers.og2 / weights["2OG"] +
                         local_allocations[alloc].happy_numbers.og3 / weights["3OG"] < 0.5):
                add_unfulfilled_wish("Etagenwunsch verletzt", local_allocations, alloc)

            # kleine Wohnung wichtig und nicht erfüllt (4 oder 5)
            if (hh.small_flat is not None and norm_weight(hh.small_flat) > 0.5) and (
                    local_allocations[alloc].happy_numbers.small_flat / weights["kleine_wg"] < 0.5):
                add_unfulfilled_wish("kl. Wg Wunsch verletzt", local_allocations, alloc)

            # rolli-tauglich wichtig und nicht erfüllt (4 oder 5)
            if (hh.wheelchair_suitable_weight is not None and norm_weight(hh.wheelchair_suitable_weight) > 0.5) \
                    and (local_allocations[alloc].happy_numbers.wheelchair / weights["rollitauglich"] < 0.5):
                add_unfulfilled_wish("Rolli Wunsch verletzt", local_allocations, alloc)

            # Nachbar wichtig und nicht erfüllt (4 oder 5)
            if (hh.neighbour_weight is not None and norm_weight(hh.neighbour_weight) > 0.5) \
                    and (local_allocations[alloc].happy_numbers.neighbour / weights["Nachbar"] < 0.5):
                add_unfulfilled_wish("Nachbarwunsch verletzt. NachbarID: " + str(hh.neighbour_id), local_allocations,
                                     alloc)

            # Hundedistanz wichtig und nicht erfüllt (4 oder 5)
            if (hh.dog_close_weight is not None and norm_weight(hh.dog_close_weight) > 0.5) \
                    and (local_allocations[alloc].happy_numbers.dog / weights["Hund"] < 0.5):
                if hh.dog_close is not None and hh.dog_close == 1:
                    close_vs_distant = "nähe"
                else:
                    close_vs_distant = "distanz"
                add_unfulfilled_wish("Hunde" + close_vs_distant + "wunsch verletzt -> Nächster Hund in " +
                                     local_allocations[alloc].happy_numbers.next_dog_flat, local_allocations, alloc)

            # Katzendistanz wichtig und nicht erfüllt (4 oder 5)
            if (hh.cat_close_weight is not None and norm_weight(hh.cat_close_weight) > 0.5) \
                    and (local_allocations[alloc].happy_numbers.cat / weights["Katze"] < 0.5):
                if hh.cat_close is not None and hh.cat_close == 1:
                    close_vs_distant = "nähe"
                else:
                    close_vs_distant = "distanz"
                add_unfulfilled_wish("Katzen" + close_vs_distant + "wunsch verletzt -> Nächste Katze in " +
                                     local_allocations[alloc].happy_numbers.next_cat_flat, local_allocations, alloc)

            # Raucherdistanz wichtig und nicht erfüllt (4 oder 5)
            if (hh.smoker_aversion_weight is not None and norm_weight(hh.smoker_aversion_weight) > 0.5) and \
                    ((local_allocations[alloc].happy_numbers.smoker / weights["Raucher"]) < 0.5):
                add_unfulfilled_wish("Raucherdistanzwunsch verletzt -> Nächster Raucher in " +
                                     local_allocations[alloc].happy_numbers.next_smoker_flat, local_allocations, alloc)

            # Wunschwohnung und keine Wunschwohnung bekommen
            if (hh.specific_flat_wish is not None and hh.specific_flat_wish == 1) \
                    and (local_allocations[alloc].happy_numbers.specific_flat < 0.5):
                add_unfulfilled_wish("Wunschwohnung verletzt. WunschWg: " + str(hh.specific_flat1) + ", "
                                     + str(hh.specific_flat2) + ", " + str(hh.specific_flat3), local_allocations, alloc)

            # WBS
            if hh.wbs != flat.wbs:
                local_allocations[alloc].happy_numbers.wbs_change = "Wohnung " + str(local_allocations[alloc].wg_id) + \
                                                                    " war eine WBS " + str(flat.wbs) + " Wohnung und muss " + \
                                                                    "eine WBS " + str(hh.wbs) + " Wohnung werden."

    return local_allocations


def compare_allocations(new_allocation, old_allocation):
    diff_allocation = copy.deepcopy(new_allocation)

    for alloc in new_allocation:
        if alloc < 1000:
            diff_allocation[alloc].happy_numbers.punkt = new_allocation[alloc].happy_numbers.punkt - \
                                                         old_allocation[alloc].happy_numbers.punkt
            diff_allocation[alloc].happy_numbers.winkel = new_allocation[alloc].happy_numbers.winkel - \
                                                          old_allocation[alloc].happy_numbers.winkel
            diff_allocation[alloc].happy_numbers.riegel = new_allocation[alloc].happy_numbers.riegel - \
                                                          old_allocation[alloc].happy_numbers.riegel
            diff_allocation[alloc].happy_numbers.eg = new_allocation[alloc].happy_numbers.eg - \
                                                      old_allocation[alloc].happy_numbers.eg
            diff_allocation[alloc].happy_numbers.og1 = new_allocation[alloc].happy_numbers.og1 - \
                                                       old_allocation[alloc].happy_numbers.og1
            diff_allocation[alloc].happy_numbers.og2 = new_allocation[alloc].happy_numbers.og2 - \
                                                       old_allocation[alloc].happy_numbers.og2
            diff_allocation[alloc].happy_numbers.og3 = new_allocation[alloc].happy_numbers.og3 - \
                                                       old_allocation[alloc].happy_numbers.og3
            diff_allocation[alloc].happy_numbers.small_flat = new_allocation[alloc].happy_numbers.small_flat - \
                                                              old_allocation[alloc].happy_numbers.small_flat
            diff_allocation[alloc].happy_numbers.wheelchair = new_allocation[alloc].happy_numbers.wheelchair - \
                                                              old_allocation[alloc].happy_numbers.wheelchair
            diff_allocation[alloc].happy_numbers.neighbour = new_allocation[alloc].happy_numbers.neighbour - \
                                                             old_allocation[alloc].happy_numbers.neighbour
            diff_allocation[alloc].happy_numbers.dog = new_allocation[alloc].happy_numbers.dog - \
                                                       old_allocation[alloc].happy_numbers.dog
            diff_allocation[alloc].happy_numbers.cat = new_allocation[alloc].happy_numbers.cat - \
                                                       old_allocation[alloc].happy_numbers.cat
            diff_allocation[alloc].happy_numbers.smoker = new_allocation[alloc].happy_numbers.smoker - \
                                                          old_allocation[alloc].happy_numbers.smoker
            diff_allocation[alloc].happy_numbers.specific_flat = new_allocation[alloc].happy_numbers.specific_flat - \
                                                                 old_allocation[alloc].happy_numbers.specific_flat
            diff_allocation[alloc].happy_numbers.wbs = new_allocation[alloc].happy_numbers.wbs - \
                                                       old_allocation[alloc].happy_numbers.wbs

            diff_allocation[alloc].happy_numbers.sum = \
                diff_allocation[alloc].happy_numbers.punkt + \
                diff_allocation[alloc].happy_numbers.winkel + \
                diff_allocation[alloc].happy_numbers.riegel + \
                diff_allocation[alloc].happy_numbers.eg + \
                diff_allocation[alloc].happy_numbers.og1 + \
                diff_allocation[alloc].happy_numbers.og2 + \
                diff_allocation[alloc].happy_numbers.og3 + \
                diff_allocation[alloc].happy_numbers.small_flat + \
                diff_allocation[alloc].happy_numbers.wheelchair + \
                diff_allocation[alloc].happy_numbers.neighbour + \
                diff_allocation[alloc].happy_numbers.dog + \
                diff_allocation[alloc].happy_numbers.cat + \
                diff_allocation[alloc].happy_numbers.smoker + \
                diff_allocation[alloc].happy_numbers.specific_flat + \
                diff_allocation[alloc].happy_numbers.wbs

    return diff_allocation
