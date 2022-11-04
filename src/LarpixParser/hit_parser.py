from LarpixParser import get_raw_coord as GetCoord
from LarpixParser import coord_transform as CoordTran
from LarpixParser import get_charge as GetCharge
from LarpixParser import util

def hit_parser_position(t0, packets, geom_dict, run_config, switch_xz=True):

    packets_arr = util.get_data_packets(packets)

    # get 3D hit position, and flip x and z
    x, y, z, t_drift_arr = GetCoord.get_hit3D_position_tdrift(t0, packets, packets_arr, geom_dict, run_config)

    # transform coordinate
    if switch_xz:
        x, y, z = CoordTran.switch_xz(x, y, z)

    return x, y, z, t_drift_arr

def hit_parser_charge(t0, packets, geom_dict, run_config, switch_xz=True):
    
    packets_arr = util.get_data_packets(packets)

    x, y, z, t_drift_arr = hit_parser_position(t0, packets, geom_dict, run_config, switch_xz)

    dQ = GetCharge.get_calo_ke(packets_arr, run_config)

    return x, y, z, dQ

def hit_parser_energy(t0, packets, geom_dict, run_config, switch_xz=True):

    packets_arr = util.get_data_packets(packets)

    x, y, z, t_drift_arr = hit_parser_position(t0, packets, geom_dict, run_config, switch_xz)

    dE = GetCharge.get_calo_MeV(packets_arr, t_drift_arr, run_config)

    return x, y, z, dE
