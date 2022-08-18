import copy


def swap_flats(hh1, hh2, allocation, list_flats):
    if list_flats[allocation[hh1].wg_id].flat_type != list_flats[allocation[hh2].wg_id].flat_type:
        raise Exception("Es können nur Haushalte mit gleichem Wohnungstyp getauscht werden.")
    wg_id = copy.deepcopy(allocation[hh1].wg_id)
    allocation[hh1].wg_id = copy.deepcopy(allocation[hh2].wg_id)
    allocation[hh2].wg_id = copy.deepcopy(wg_id)
