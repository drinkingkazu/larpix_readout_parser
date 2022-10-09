import h5py 
import numpy as np

from LarpixParser import event_parser as EvtParser
from LarpixParser import hit_parser as HitParser
from LarpixParser import geom_dict_loader as DictLoader
from LarpixParser import util as util

f = h5py.File('../example_data/larnd-sim_output_mpr_mu100.h5', 'r')
tracks = f['tracks']
packets = f['packets']
assn = f['mc_packets_assn']

geom_dict = DictLoader.load_geom_dict("../config_repo/dict_repo/multi_tile_layout-2.3.16.pkl")
run_config_path = "../config_repo/module0.yaml"
run_config = util.get_run_config(run_config_path)

event_ids = np.unique(tracks['eventID'])
pckt_event_ids = EvtParser.packet_to_eventid(assn, tracks)
t0_grp = EvtParser.get_t0(packets)

for evt_id in event_ids:

    print("--------evt_id: ", evt_id)
    pckt_mask = pckt_event_ids == evt_id
    packets_ev = packets[pckt_mask]
    t0 = t0_grp[evt_id][0]
    
    ## x is the drift; y is the vertical direction; z is horizontal axis in pixel plane

    # if you want position and energy (derived from the readout)
    x,y,z,dE = HitParser.hit_parser_energy(t0, packets_ev, geom_dict, run_config)
    # if you want position and charge [ke-]
    x,y,z,dQ = HitParser.hit_parser_charge(t0, packets_ev, geom_dict, run_config)
    # if you just want the position info
    x,y,z,t_drift = HitParser.hit_parser_position(t0, packets_ev, geom_dict, run_config)


