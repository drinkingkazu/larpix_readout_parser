from LarpixParser import get_raw_coord as GetCoord
from LarpixParser import coord_transform as CoordTran
from LarpixParser import get_charge as GetCharge
from LarpixParser import util

def hit_parser(t0, packets, geom_dict, run_config):
    packets_arr = util.get_data_packets(packets)

    # get 3D hit position, and flip x and z
    x, y, z, t_drift_arr = GetCoord.get_hit3D_position_tdrift(t0, packets, packets_arr, geom_dict, run_config)

    # transform coordinate
    x, y, z = CoordTran.switch_xz(x, y, z)
    #x, y, z = CoordTran.shift_y(run_config['y_offset'], x, y, z)

    
    dE = GetCharge.get_charge_MeV(packets_arr, t_drift_arr, run_config)

    return x, y, z, dE
