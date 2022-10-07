import h5py 
import hit_paser as HitParser
import geom_dict_loader as DictLoader

f = h5py.File('/sdf/group/neutrino/cyifan/muon-sim/larndsim_output/f1_100/larnd-sim_100ev_1500us.h5', 'r')
pckts = f['packets']
print(pckts)
geom_dict = DictLoader.load_geom_dict("/sdf/group/neutrino/cyifan/larpix_geometry_repo/dict_repo/multi_tile_layout-2.2.16.pkl")
run_config_path = "/sdf/group/neutrino/cyifan/larpix_geometry_repo/module0.yaml"
x,y,z,dE = HitParser.hit_parser(packets, geom_dict, run_config_path)
