import argparse
import pkmodel as pk


# def parse_args(argv=None):
#     parser = argparse.ArgumentParser(description='Train neural net on .types data.')
#     parser.add_argument('-d','--data_root',type=str,required=False,help="Root folder for relative paths in train/test files",default='/data/localhost/not-backed-up/turnbull/docks-train/')
#     parser.add_argument('-i','--frozen_iter',type=int,required=False,help="Number of iterations to run with all layers frozen",default=1000)
    

#     args = parser.parse_args(argv)
    
#     return args


protocol = pk.protocol.Protocol(2, 1, 1, 1, 1, 1, 1, k_a=1)
model = pk.model.ThreeCompartmentModel(protocol)

model.solution.graph()

