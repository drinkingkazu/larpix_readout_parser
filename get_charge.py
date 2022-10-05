# ADC 
# mV
# ke-
# MeV (include work function, recombination and lifetime correction)

def get_run_config_charge(run_config_path):
    '''
    '''
    run_config = {}

    with open(run_config_path) as infile:
        run_yaml = yaml.load(infile, Loader=yaml.FullLoader)

    # Note efield is expected to be in kV/mm to match with the unit treatment
    run_config['GAIN'] = run_yaml['GAIN']  # mV/ke-
    run_config['V_CM'] = run_yaml['V_CM']  # mV
    run_config['V_REF'] = run_yaml['V_REF']  # mV
    run_config['V_PEDESTAL'] = run_yaml['V_PEDESTAL']  # mV
    run_config['ADC_COUNTS'] = run_yaml['ADC_COUNTS'] 


    return run_config

def get_charge_ADC(packets_arr):
    return packets_arr['dataword']

def get_charge_mV(packets_arr, run_config_path):
    run_config = get_run_config_charge(run_config_path)
    #run_config = GetV.get_run_config('/sdf/group/neutrino/cyifan/larpix_geometry_repo/2x2.yaml')
    packet_mV = packets_arr['dataword'] / run_config['ADC_COUNTS'] * (run_config['V_REF'] - run_config['V_CM']) + run_config['V_CM'] - run_config['V_PEDESTAL']

    return packet_mV

def get_charge_ke(packets_arr, run_config_path):
    packet_mV = get_charge_mV(packets_arr, run_config_path)
    packet_ke = packet_mV / run_config['GAIN']
    print("packet_ke ", packet_ke)
    return packet_ke
    
