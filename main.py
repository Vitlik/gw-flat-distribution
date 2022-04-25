import sys


class Person:
    def __init__(self, id_num, animal_pref, animal_weight):
        self.id_num = id_num
        self.animal_pref = animal_pref
        self.animal_weight = animal_weight


if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = "demo.xlsx"

print("Ende.")
