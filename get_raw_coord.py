# load a run config file with efield
# run, event, hit?
# hit shape
# event parser?

import numpy as np
import get_vdrift as GetV
import event_parser as EvtPaser

def get_data_packets(packets):
    mask = packets['packet_type'] == 0
    packets_arr = packets.data[mask]
    return packets_arr

def get_pixel_plane_position(packets_arr, geom_dict):

    xyz = geom_dict[packets_arr['io_group'], packets_arr['io_channel'], packets_arr['chip_id'], packets_arr['channel_id']]
    x = xyz[:, 0]
    y = xyz[:, 1]
    z = xyz[:, 2]
    direction = yz[:, 3]
    return x, y, z, direction

def get_hit3D_position(packets_arr, geom_dict, run_config_path):

    xyz = geom_dict[packets_arr['io_group'], packets_arr['io_channel'], packets_arr['chip_id'], packets_arr['channel_id']]
    x = xyz[:, 0]
    y = xyz[:, 1]

    z_anode = xyz[:, 2]

    run_config = GetV.get_run_config_vdrift(run_config_path)
    #run_config = GetV.get_run_config_vdrift('/sdf/group/neutrino/cyifan/larpix_geometry_repo/2x2.yaml')
    v_drift = GetV.v_drift(run_config, 1)

    t0_grp = EvtParser.get_t0(packets_arr).astype(float)
    t0 = t0_grp[packets_arr['io_group']-1]
    t = packets_arr['timestamp'].astype(float)
    t_drift = t - t0
    
    z = z_anode + direction * t_drift * v_drift

    return x, y, z


