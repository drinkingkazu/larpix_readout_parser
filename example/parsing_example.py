import h5py 
import numpy as np

from LarpixParser import event_parser as EvtParser
from LarpixParser import hit_parser as HitParser
from LarpixParser import geom_dict_loader as DictLoader
from LarpixParser import util as util

'''
    If one wants to build the larpix layout dictionary on the fly instead of load from the prebuilt pkl file, uncomment ##**## and comment the geom_dict line
'''

##**##from LarpixParser import geom_to_dict as DictBuilder

f = h5py.File('../example_data/ndlar_ev20_larndsim.h5', 'r')
packets = f['packets'] # readout
tracks = f['tracks'] # Geant4 truth
assn = f['mc_packets_assn'] # G4-readout association

geom_dict = DictLoader.load_geom_dict("../config_repo/dict_repo/multi_tile_layout-3.0.40.pkl")
##**##geom_repo = '../config_repo'
##**##larpix_layout_name = 'multi_tile_layout-3.0.40'
##**##geom_dict = DictBuilder.larpix_layout_to_dict(geom_repo, larpix_layout_name, save_dict=False)

run_config_path = '../config_repo/ndlar-module.yaml'
run_config = util.get_run_config(run_config_path)

'''
    The following should be the read-out level information
    Since this package does not provide event parser, here in the example we use the truth information
'''
pckt_event_ids = EvtParser.packet_to_eventid(assn, tracks)
event_ids = np.unique(pckt_event_ids[pckt_event_ids != -1]) 
t0_grp = EvtParser.get_t0(packets)

for i_ev, evt_id in enumerate(event_ids):

    print("--------evt_id: ", evt_id)
    pckt_mask = pckt_event_ids == evt_id
    packets_ev = packets[pckt_mask]
    t0 = t0_grp[i_ev][0]
    
    ## x is the drift; y is the vertical direction; z is horizontal axis in pixel plane

    # if you want position and energy (derived from the readout)
    x,y,z,dE = HitParser.hit_parser_energy(t0, packets_ev, geom_dict, run_config)
    # if you want position and charge [ke-]
    x,y,z,dQ = HitParser.hit_parser_charge(t0, packets_ev, geom_dict, run_config)
    # if you just want the position info
    x,y,z,t_drift = HitParser.hit_parser_position(t0, packets_ev, geom_dict, run_config)


