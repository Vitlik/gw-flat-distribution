class HappyNumbers(object):
    punkt = 0
    winkel = 0
    riegel = 0
    eg = 0
    og1 = 0
    og2 = 0
    og3 = 0
    small_flat = 0
    wheelchair = 0
    neighbour = 0
    dog = 0
    distance_to_next_dog = 999
    cat = 0
    distance_to_next_cat = 999
    smoker = 0
    distance_to_next_smoker = 999
    specific_flat = 0

    sum = 0

    def __init__(self) -> None:
        super().__init__()

    def __init__(self,
                 punkt,
                 winkel,
                 riegel,
                 eg,
                 og1,
                 og2,
                 og3,
                 small_flat,
                 wheelchair,
                 neighbour,
                 dog,
                 cat,
                 smoker,
                 specific_flat):
        self.punkt = punkt
        self.winkel = winkel
        self.riegel = riegel
        self.eg = eg
        self.og1 = og1
        self.og2 = og2
        self.og3 = og3
        self.small_flat = small_flat
        self.wheelchair = wheelchair
        self.neighbour = neighbour
        self.dog = dog
        self.cat = cat
        self.smoker = smoker
        self.specific_flat = specific_flat
