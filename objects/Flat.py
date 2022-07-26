class Flat(object):
    id = None
    flat_type = None
    building = None
    floor = None
    qm = None
    small = None
    wheelchair_suitable = None
    distribution = None

    def __init__(self, id, flat_type, building, floor, qm, small, wheelchair_suitable, distribution):
        self.id = id
        self.flat_type = flat_type
        self.building = building
        self.floor = floor
        self.qm = qm
        self.small = small
        self.wheelchair_suitable = wheelchair_suitable
        self.distribution = distribution

    def __str__(self):
        return str(self.id) + ' is with' \
               + ' | flat_type: ' + str(self.flat_type) \
               + ' | building: ' + str(self.building) \
               + ' | floor: ' + str(self.floor) \
               + ' | small: ' + str(self.small) \
               + ' | wheelchair_suitable: ' + str(self.wheelchair_suitable)
