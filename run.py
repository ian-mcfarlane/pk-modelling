import argparse
import pkmodel as pk
import csv
from pathlib import Path


def parse_args(argv=None):
    """ Parses command line arguments.

    :return: args
    :rtype: Namespace
    """
    parser = argparse.ArgumentParser(description="Plot PK models using 2 or 3 compartment models")
    parser.add_argument('-d', '--data_root', type=str, required=False, help="Path to location of csv file (default = './'",
                        default='./')
    parser.add_argument('-f', '--file_name', type=str, required=False, help="Filename for csv file containing model parameters",
                        default='example.csv')
    args = parser.parse_args(argv)

    return args


if __name__ == "__main__":
    args = parse_args()

    # Load csv files
    with open(Path(args.data_root + args.file_name)) as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        try:
            data = list(reader)
        except ValueError:
            raise ValueError("Strings in CSVs should be in double quotes.")

    # Create a Model object for each line in the csv file
    models = []
    for model_params in data:

        # create protocol
        protocol = pk.protocol.Protocol(*model_params)

        # Check if 2 or 3 component model
        if model_params[1] == 2:
            models.append(pk.model.TwoCompartmentModel(protocol))
        elif model_params[1] == 3:
            models.append(pk.model.ThreeCompartmentModel(protocol))

    # Generate graph
    solution = pk.solution.Solution(models)