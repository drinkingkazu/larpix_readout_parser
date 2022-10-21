import numpy as np

from LarpixParser import get_vdrift as GetV
from LarpixParser import event_parser as EvtParser
from LarpixParser import util

def get_pixel_plane_position(packets_arr, geom_dict, run_config):
    tpc_centers = run_config['tpc_offsets']
    
    x, y, z, direction = [], [], [], []
    for packet in packets_arr:
        io_group = packet['io_group']
        module_id = (io_group - 1)//4
        print("iogrp", io_group, "mid", module_id)
        io_group = io_group - module_id*4
        
        xyz = geom_dict[io_group, packet['io_channel'], packet['chip_id'], packet['channel_id']]
        x_offset = tpc_centers[module_id][0]*10
        z_offset = tpc_centers[module_id][2]*10
        y_offset = tpc_centers[module_id][1]*10
        
        x.append(xyz[0] + x_offset)
        y.append(xyz[1] + y_offset)
        z.append(xyz[2] + z_offset)
        direction.append(xyz[3])
 
    return x, y, z, direction

def get_t_drift(t0, packets_arr, run_config):

    t = packets_arr['timestamp'].astype(float)
    t_drift = t - t0 # ticks, 0.1us
    t_drift *= run_config['response_sampling']

    return t_drift

#def get_hit3D_position(t0,  packets, packets_arr, geom_dict, run_config):
#
#    x, y, z_anode, direction = get_pixel_plane_position(packets_arr, geom_dict)
#
#    v_drift = GetV.v_drift(run_config, 1)
#    
#    #t = packets_arr['timestamp'].astype(float)
#    t_drift = get_t_drift(t0, packets_arr, run_config)
#
#    z = z_anode + direction * t_drift * v_drift
#
#    return x, y, z

def get_hit3D_position_tdrift(t0,  packets, packets_arr, geom_dict, run_config):

    x, y, z_anode, direction = get_pixel_plane_position(packets_arr, geom_dict, run_config)

    v_drift = GetV.v_drift(run_config, 1)

    #t = packets_arr['timestamp'].astype(float)
    t_drift = get_t_drift(t0, packets_arr, run_config)

    z = z_anode + direction * t_drift * v_drift

    return x, y, z, t_drift
