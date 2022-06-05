import copy


def swap_flats(hh1, hh2, allocation):
    wg_id = copy.deepcopy(allocation[hh1].wg_id)
    # print("allocation[hh1].wg_id : " + str(allocation[hh1].wg_id))
    allocation[hh1].wg_id = copy.deepcopy(allocation[hh2].wg_id)
    # print("allocation[hh1].wg_id : " + str(allocation[hh1].wg_id))
    # print("allocation[hh2].wg_id : " + str(allocation[hh2].wg_id))
    allocation[hh2].wg_id = copy.deepcopy(wg_id)
    # print("allocation[hh2].wg_id : " + str(allocation[hh2].wg_id))
