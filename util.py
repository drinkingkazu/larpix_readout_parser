import yaml
import units

def get_data_packets(packets):

    mask = packets['packet_type'] == 0
    packets_arr = packets[mask]

    return packets_arr

def get_run_config(run_config_path):

    run_config = {}

    with open(run_config_path) as infile:
        run_yaml = yaml.load(infile, Loader=yaml.FullLoader)

    run_config['y_offset'] = run_yaml['tpc_offsets'][0][1] * units.cm

    run_config['GAIN'] = run_yaml['GAIN']  # mV/ke-
    run_config['V_CM'] = run_yaml['V_CM']  # mV
    run_config['V_REF'] = run_yaml['V_REF']  # mV
    run_config['V_PEDESTAL'] = run_yaml['V_PEDESTAL']  # mV
    run_config['ADC_COUNTS'] = run_yaml['ADC_COUNTS']

    run_config['efield'] = run_yaml['e_field'] / (units.kV / units.cm) # kV/cm # the input should be in kV/mm
    run_config['temp'] = run_yaml['temperature'] / (units.K) #K

    run_config['response_sampling'] = run_yaml['response_sampling'] #us

    return run_config
