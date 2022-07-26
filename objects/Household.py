from typing import Type


class Household(object):

    id = None
    name = None
    flat_type = None

    punkt = None
    punkt_weight = None
    winkel = None
    winkel_weight = None
    riegel = None
    riegel_weight = None

    eg = None
    eg_weight = None
    og1 = None
    og1_weight = None
    og2 = None
    og2_weight = None
    og3 = None
    og3_weight = None

    small_flat = None

    wheelchair_suitable = None
    wheelchair_suitable_weight = None

    neighbour = None
    neighbour_id = None
    neighbour_weight = None

    dog = None
    dog_close = None
    dog_close_weight = None
    dog_allergy = None
    cat = None
    cat_close = None
    cat_close_weight = None
    cat_allergy = None

    smoker = None
    smoker_aversion_weight = None

    specific_flat_wish = None
    specific_flat1 = None
    specific_flat2 = None
    specific_flat3 = None

    def __init__(self,
                 param_id,
                 name,
                 flat_type,
                 punkt, punkt_weight,
                 winkel, winkel_weight,
                 riegel, riegel_weight,
                 eg, eg_weight,
                 og1, og1_weight,
                 og2, og2_weight,
                 og3, og3_weight,
                 small_flat,
                 wheelchair_suitable, wheelchair_suitable_weight,
                 neighbour, neighbour_id, neighbour_weight,
                 dog, dog_close, dog_close_weight, dog_allergy,
                 cat, cat_close, cat_close_weight, cat_allergy,
                 smoker, smoker_aversion_weight,
                 specific_flat_wish, specific_flat1, specific_flat2, specific_flat3):
        self.id = param_id
        self.name = name
        self.flat_type = flat_type
        self.punkt = punkt
        self.punkt_weight = punkt_weight
        self.winkel = winkel
        self.winkel_weight = winkel_weight
        self.riegel = riegel
        self.riegel_weight = riegel_weight
        self.eg = eg
        self.eg_weight = eg_weight
        self.og1 = og1
        self.og1_weight = og1_weight
        self.og2 = og2
        self.og2_weight = og2_weight
        self.og3 = og3
        self.og3_weight = og3_weight
        self.small_flat = small_flat
        self.wheelchair_suitable = wheelchair_suitable
        self.wheelchair_suitable_weight = wheelchair_suitable_weight
        self.neighbour = neighbour
        self.neighbour_id = neighbour_id
        self.neighbour_weight = neighbour_weight
        self.dog = dog
        self.dog_close = dog_close
        self.dog_close_weight = dog_close_weight
        self.dog_allergy = dog_allergy
        self.cat = cat
        self.cat_close = cat_close
        self.cat_close_weight = cat_close_weight
        self.cat_allergy = cat_allergy
        self.smoker = smoker
        self.smoker_aversion_weight = smoker_aversion_weight
        self.specific_flat_wish = specific_flat_wish
        self.specific_flat1 = specific_flat1
        self.specific_flat2 = specific_flat2
        self.specific_flat3 = specific_flat3

    # def __str__(self):
    #     return str(self.id) + ' is with' \
    #            + ' | flat_type: ' + str(self.flat_type) \
    #            + ' | building_pref: ' + str(self.building_pref) + ' | building_weight: ' + str(self.building_weight) \
    #            + ' | floor_pref: ' + str(self.floor_pref) + ' | floor_weight: ' + str(self.floor_weight) \
    #            + ' | neighbour_pref: ' + str(self.neighbour_pref) + ' | neighbour_weight: ' + str(self.neighbour_weight) \
    #            + ' | small_flat_pref: ' + str(self.small_flat_pref) + ' | small_flat_weight: ' + str(self.small_flat_weight) \
    #            + ' | animal_pref: ' + str(self.animal_pref) + ' | animal_weight: ' + str(self.animal_weight) \
    #            + ' | specific_flat_pref: ' + str(self.specific_flat_pref) + ' | specific_flat_weight: ' \
    #            + str(self.specific_flat_weight) \
    #            + ' | wheelchair_suitable: ' + str(self.wheelchair_suitable) \
    #            + ' | wheelchair_suitable_weight: ' + str(self.wheelchair_suitable_weight)
