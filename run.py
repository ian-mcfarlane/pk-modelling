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
    parser.add_argument('-f', '--file_name', type=str, required=False,
                        help="Filename for csv file containing model parameters", default='example.csv')
    parser.add_argument('-n', '--no_graph', action="store_true", help="Do not show the graph")
    args = parser.parse_args(argv)

    return args


def create_model(components, protocol):
    if components == 2:
        return pk.model.TwoCompartmentModel(protocol)
    elif components == 3:
        return pk.model.ThreeCompartmentModel(protocol)


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

        # Check if 2 or 3 component model and append to models list
        models.append(create_model(model_params[1], protocol))

    # Generate graph
    solution = pk.solution.Solution(models, no_graph=args.no_graph)
