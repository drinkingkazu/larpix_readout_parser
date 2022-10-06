# ADC 
# mV
# ke-
# MeV (include work function, recombination and lifetime correction)
import numpy as np
import units

def get_charge_ADC(packets_arr):
    return packets_arr['dataword']

def get_charge_mV(packets_arr, run_config):
    packet_mv = []
    packet_mV = packets_arr['dataword'] / run_config['ADC_COUNTS'] * (run_config['V_REF'] - run_config['V_CM']) + run_config['V_CM'] - run_config['V_PEDESTAL']
    return packet_mV

def get_charge_ke(packets_arr, run_config):
    packet_mV = get_charge_mV(packets_arr, run_config)
    packet_ke = packet_mV / run_config['GAIN']
    return packet_ke

def get_charge_MeV(packets_arr, run_config):
    ## work function, lifetime, recombination
    packet_MeV = get_charge_ke(packets_arr, run_config) * 1000 / 0.7 * 23.6 * units.eV / units.MeV
    return packet_MeV    
