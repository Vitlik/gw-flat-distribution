class HappyNumbers(object):
    building_pref = 0
    floor_pref = 0
    neighbour_pref = 0
    small_flat_pref = 0
    animal_pref = 0
    distance_to_next_animal = 999
    specific_flat_pref = 0

    def __init__(self) -> None:
        super().__init__()

    def __init__(self,
                 building_pref,
                 floor_pref,
                 neighbour_pref,
                 small_flat_pref,
                 animal_pref,
                 specific_flat_pref):
        self.building_pref = building_pref
        self.floor_pref = floor_pref
        self.neighbour_pref = neighbour_pref
        self.small_flat_pref = small_flat_pref
        self.animal_pref = animal_pref
        self.specific_flat_pref = specific_flat_pref
