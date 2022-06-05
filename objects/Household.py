class Household(object):

    id = None
    flat_type = None
    building_pref = None
    building_weight = None
    floor_pref = None
    floor_weight = None
    neighbour_pref = None
    neighbour_weight = None
    small_flat_pref = None
    small_flat_weight = None
    animal_pref = None
    animal_weight = None
    specific_flat_pref = None
    specific_flat_weight = None
    wheelchair_suitable = None

    def __init__(self, id,
                 wohn_art,
                 building_pref, building_weight,
                 floor_pref, floor_weight,
                 neighbour_pref, neighbour_weight,
                 small_flat_pref, small_flat_weight,
                 animal_pref, animal_weight,
                 specific_flat_pref, specific_flat_weight,
                 wheelchair_suitable):
        self.id = id
        self.flat_type = wohn_art
        self.building_pref = building_pref
        self.building_weight = building_weight
        self.floor_pref = floor_pref
        self.floor_weight = floor_weight
        self.neighbour_pref = neighbour_pref
        self.neighbour_weight = neighbour_weight
        self.small_flat_pref = small_flat_pref
        self.small_flat_weight = small_flat_weight
        self.animal_pref = animal_pref
        self.animal_weight = animal_weight
        self.specific_flat_pref = specific_flat_pref
        self.specific_flat_weight = specific_flat_weight
        self.wheelchair_suitable = wheelchair_suitable

    def __str__(self):
        return str(self.id) + ' is with' \
               + ' | flat_type: ' + str(self.flat_type) \
               + ' | building_pref: ' + str(self.building_pref) + ' | building_weight: ' + str(self.building_weight) \
               + ' | floor_pref: ' + str(self.floor_pref) + ' | floor_weight: ' + str(self.floor_weight) \
               + ' | neighbour_pref: ' + str(self.neighbour_pref) + ' | neighbour_weight: ' + str(self.neighbour_weight) \
               + ' | small_flat_pref: ' + str(self.small_flat_pref) + ' | small_flat_weight: ' + str(self.small_flat_weight) \
               + ' | animal_pref: ' + str(self.animal_pref) + ' | animal_weight: ' + str(self.animal_weight) \
               + ' | specific_flat_pref: ' + str(self.specific_flat_pref) + ' | specific_flat_weight: ' \
               + str(self.specific_flat_weight) \
               + ' | wheelchair_suitable: ' + str(self.wheelchair_suitable)
