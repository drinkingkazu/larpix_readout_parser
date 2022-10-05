import event_parser as EvtPaser
import get_raw_coord as GetCoord
import coord_transform as CoordTran
import get_charge as GetCharge

def hit_parser(packets, geom_dict, run_config_path):
    packets_arr = EvtPaser.get_data_packets(packets)

    # get 3D hit position, and flip x and z
    x, y, z = GetCoord.get_hit3D_position(packets_arr, geom_dict, run_config_path)

    # transform coordinate
    run_config = CoordTran.get_run_config_coord(run_config_path)    
    x, y, z = switch_xz(x, y, z)
    x, y, z = shift_y(run_config['y_offset'], x, y, z)

    dE = GetCharge.get_charge_MeV(packets_arr, run_config_path)

    return x, y, z, dE
