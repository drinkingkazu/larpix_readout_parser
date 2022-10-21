# LarpixParser
! Currently only works for single module!
This package provides simple function to parse LArPix readout position [mm], read out charge [thousand electrons(ke-)] and deposited energy [MeV].\
This package is also available on pypi: https://pypi.org/project/LarpixParser/. 
>```pip install LarpixParser```

## What do you need to prepare?
1. A LArPix geometry yaml file: \
    An example can be found in `config_repo/multi_tile_layout-2.3.16.yaml` for a module0 configuration. The geometry yaml files are produced using scripts in package `larpix/larpix-geometry` (https://github.com/larpix/larpix-geometry). It is also on PyPI: https://pypi.org/project/larpix-geometry/. Note that different runs of the same detector can lead to different geometry yaml file depending on the pixel channel routing set up before the run. Please see `larpix/larpix-geometry` for more details where the LArPix geometry yamls are stored on NERSC for example.
2. A configuration file: \
    An example can be found in `config_repo/module0.yaml`. It should store information about the LArPix charge calibration, run conditions (electric field, electron lifetime, etc.), coordinate shifts and detector physics parameters (LAr density, recombination model parameters, etc.). Note that `LarpixParser` assumes the units as shown in the example configuration file.
3. LArPix outputs:\
    `LarpixParser` consumes raw LArPix output. It "should" be agnoistic to whether the input is real data or simulation output, but this package has only been tested with simulation output. It does not produce "hit"-level data product. Users need to call it per instance. 
    
## An intermediate step:
Use `src/LarpixParser/geom_to_dict.py` to convert the LArPix geometry yaml to a dictionary and store it in a pickle file. The script can be run as a standalone one. The output pickle file will be stored in the same folder where the yaml file is, e.g `dict_repo/LARPIX_GEOM_NAME.pkl`. You may need to twist something if you don't have writing rights of the folder. Run the following command to execute this step. **You will only need to run this step once for a LArPix geometry yaml file.** The path to the pickle file is expected in LarpixParser.
>```python3 src/LarpixParser/geom_to_dict.py --geom_repo=PATH_TO_LARPIX_GEOMETRY_YAML --geom_name=NAME_LARPIX_GEOMETRY_YAML```

## Time to profit!
You can find an simple example here: `example/function_usage_example.py`, which is tuned for simulation input. Currently, it works if you feed in packets from a single event. It does not support feeding in the packets from multiple events at the moment, but YOU can fix it if you want:) Function `hit_parser_position` outputs x, y, z and the drift time with respect to the "t0" of the event; Function `hit_parser_charge` outputs x, y, z and dQ [ke-] which is the read out charge per channel (All the channels share the same calibration constants for now, and they are required in the configuration file. The calibration constants are used for converting the readout from [ADC] to [mV] and then to [ke-]); Function `hit_parser_energy` outputs x, y, z and dE [MeV] which meant to be the energy deposition corresponding to the read out charge at their origin. Therefore, the detector physics calibration (work function, recombination and electron attenuation) is folded in. One caveat is that dE/dx is assumed to be 2 MeV/cm for all in the recombination model which is definitely a simplification. `x` is along the drift axis; `y` is along the vertical axis; `z` is along the horizontal axis of the LArPix plane. The origin of the coordinate system depends on the detector (defined in the LArPix geometry yaml file).
