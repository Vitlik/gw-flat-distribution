class Flat(object):
    id = None
    flat_type = None
    building = None
    floor = None
    qm = None
    small = None
    wbs = None
    wheelchair_suitable = None
    distribution = None

    def __init__(self, id, flat_type, building, floor, qm, small, wbs, wheelchair_suitable, distribution):
        self.id = id
        self.flat_type = flat_type
        self.building = building
        self.floor = floor
        self.qm = qm
        self.small = small
        self.wbs = wbs
        self.wheelchair_suitable = wheelchair_suitable
        self.distribution = distribution

    def __str__(self):
        return str(self.id) + ' is with' \
               + ' | flat_type: ' + str(self.flat_type) \
               + ' | building: ' + str(self.building) \
               + ' | floor: ' + str(self.floor) \
               + ' | qm: ' + str(self.qm) \
               + ' | small: ' + str(self.small) \
               + ' | wbs: ' + str(self.wbs) \
               + ' | wheelchair_suitable: ' + str(self.wheelchair_suitable) \
               + ' | distribution: ' + str(self.distribution)
