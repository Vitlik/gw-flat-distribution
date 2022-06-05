def swap_flats(hh1, hh2, allocation):
    wg_id = allocation[hh1].wg_id
    allocation[hh1].wg_id = allocation[hh2].wg_id
    allocation[hh2].wg_id = wg_id
