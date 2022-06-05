from objects.HappyNumbers import HappyNumbers


class Allocation:
    hh_id = 0
    wg_id = 0
    happy_numbers = None

    def __init__(self, hh_id, wg_id, happy_numbers):
        self.hh_id = hh_id
        self.wg_id = wg_id
        self.happy_numbers = happy_numbers

    def __init__(self, hh_id, wg_id):
        self.hh_id = hh_id
        self.wg_id = wg_id
