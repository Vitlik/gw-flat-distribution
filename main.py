import sys


class Household:

    def __init__(self, id_num, building_pref, building_weight, floor_pref, floor_weight, neighbour_pref,
                 neighbour_weight, small_flat_pref, small_flat_weight, animal_pref, animal_weight):
        self.id_num = id_num
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

    def __str__(self):
        return str(self.id_num) + ' is with ' \
        + str(self.building_pref) + ' building_pref | ' + str(self.building_weight) \
        + ' building_weight | ' + str(self.floor_pref) + ' floor_pref | ' + str(self.floor_weight) + ' floor_weight | ' \
        + str(self.neighbour_pref) + ' neighbour_pref | ' + str(self.neighbour_weight) + ' neighbour_weight | ' \
        + str(self.small_flat_pref) + ' small_flat_pref | ' + str(self.small_flat_weight) + ' small_flat_weight | ' \
        + str(self.animal_pref) + ' animal_pref | ' + str(self.animal_weight) + ' animal_weight'


if len(sys.argv) > 2:
    interests = sys.argv[1]
    master_data = sys.argv[2]
elif len(sys.argv) > 1:
    interests = sys.argv[1]
    master_data = "master_data_demo.xlsx"
else:
    interests = "interests_demo.xlsx"
    master_data = "master_data_demo.xlsx"

prengers = \
    Household(123,  # id_num
              "1", 6,  # building
              "3", 3,  # floor
              "45", 10,  # neighbour
              "False", 1,  # small_flat
              "close", 7)  # animal

str(prengers)
