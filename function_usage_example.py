import h5py 
import numpy as np

import event_parser as EvtParser
import hit_parser as HitParser
import geom_dict_loader as DictLoader
import util

f = h5py.File('example_data/larnd-sim_output_mpr_mu100.h5', 'r')
tracks = f['tracks']
packets = f['packets']
assn = f['mc_packets_assn']

geom_dict = DictLoader.load_geom_dict("config_repo/dict_repo/multi_tile_layout-2.3.16.pkl")
run_config_path = "config_repo/module0.yaml"
run_config = util.get_run_config(run_config_path)

event_ids = np.unique(tracks['eventID'])
pckt_event_ids = EvtParser.packet_to_eventid(assn, tracks)
t0_grp = EvtParser.get_t0(packets)

for evt_id in event_ids:

    print("--------evt_id: ", evt_id)
    pckt_mask = pckt_event_ids == evt_id
    packets_ev = packets[pckt_mask]
    t0 = t0_grp[evt_id][0]
    x,y,z,dE = HitParser.hit_parser(t0, packets_ev, geom_dict, run_config)

    #print(">>x", x)
    #print(">>y", y)
    #print(">>z", z)
    #print(">>dE", dE)

    #track_mask = tracks['eventID'] == evt_id
    #print("PDG", tracks[track_mask]['pdgId'])
    #print("dEdx", tracks[track_mask]['dEdx'])
    #print("dEdx", tracks[track_mask])
    #if evt_id > 1:
    #    break
    

#x,y,z,dE = HitParser.hit_parser(packets_ev, geom_dict, run_config_path)
