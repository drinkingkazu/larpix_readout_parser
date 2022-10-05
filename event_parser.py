# external trigger
# self trigger

def get_data_packets(packets):
    mask = packets['packet_type'] == 0
    packets_arr = packets.data[mask]
    return packets_arr

def get_t0(packets_arr):
    pckts_t0 = pckts[pckts['packet_type'] == 7]
    n_grps = len(np.unique(pckts_t0['io_group']))
    print("pckts_t0['timestamp']: ", pckts_t0['timestamp'])
    print("pckts_t0['timestamp'].reshape(-1, n_grps): ", pckts_t0['timestamp'].reshape(-1, n_grps))
    return pckts_t0['timestamp'].reshape(-1, n_grps)
