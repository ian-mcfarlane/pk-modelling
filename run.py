import argparse
import pkmodel as pk
import csv
from pathlib import Path
import sys
import numpy as np


def parse_args(argv=None):
    """ Parses command line arugments.

    :return: args
    :rtype: Namespace
    """    
    parser = argparse.ArgumentParser(description="Plot PK models using 2 or 3 compartment models")
    parser.add_argument('-d', '--data_root', type=str, required=False, help="Path to location of csv file (default = './'",
                        default='./')
    parser.add_argument('-f', '--file_name', type=str, required=False, help="Filename for csv file containing model parameters",
                        default='test.csv')
    args = parser.parse_args(argv)
    
    return args

if __name__ == "__main__":
    args = parse_args()

    # Load csv files
    with open(Path(args.data_root + args.file_name)) as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        data = list(reader)
    
    # Create a Model object for each line in the csv file
    models = []
    for model_params in data:

        # create protocol
        print(model_params)
        protocol = pk.protocol.Protocol(*model_params)

        # Check if 2 or 3 component model
        if model_params[0] == 2:
            models.append(pk.model.TwoCompartmentModel(protocol))
        elif model_params[0] == 3:
            models.append(pk.model.ThreeCompartmentModel(protocol))

        else:
            raise ValueError("Component number must be either 2 or 3.")
        
    # Generate graph
    solution = pk.solution.Solution(models)


        

        

