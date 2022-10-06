import numpy as np
import get_vdrift as GetV
import event_parser as EvtParser
import util

def get_pixel_plane_position(packets_arr, geom_dict):
    
    x, y, z, direction = [], [], [], []
    for packet in packets_arr:
        xyz = geom_dict[packet['io_group'], packet['io_channel'], packet['chip_id'], packet['channel_id']]
        x.append(xyz[0])
        y.append(xyz[1])
        z.append(xyz[2])
        direction.append(xyz[3])
 
    return x, y, z, direction

def get_hit3D_position(evt_id, t0,  packets, packets_arr, geom_dict, run_config):

    x, y, z_anode, direction = get_pixel_plane_position(packets_arr, geom_dict)

    v_drift = GetV.v_drift(run_config, 1)
    
    t = packets_arr['timestamp'].astype(float)
    t_drift = t - t0

    z = z_anode + direction * t_drift * v_drift * run_config['response_sampling']

    return x, y, z
