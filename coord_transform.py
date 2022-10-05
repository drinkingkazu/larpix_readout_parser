# shift y
# switch xz
def get_run_config_coord(run_config_path):
    '''
    '''
    run_config = {}

    with open(run_config_path) as infile:
        run_yaml = yaml.load(infile, Loader=yaml.FullLoader)

    # Note efield is expected to be in kV/mm to match with the unit treatment
    run_config['y_offset'] = run_yaml['tpc_offsets'][0][1]  
 
    print("run_config['y_offset']: ", run_config)
    return run_config

def switch_xz(x, y, z):
    return z, y, x

def shift_y(offset, x, y, z):
    return x, y - offset, z
