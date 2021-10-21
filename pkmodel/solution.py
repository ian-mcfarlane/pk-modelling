import matplotlib.pylab as plt
import numpy as np
from protocol import Protocol #CHECK WITH OLLIE

class Solution:

    def __init__(self, sol,protocol:Protocol): #CHECK WITH OLLIE
        self.sol = sol
        graph()
        
    def graph (self):
        
        if self.no_of_compartment== 2:
            plt.plot(sol.t, sol.y[0, :], label=model['name'] + '- q_c')
            plt.plot(sol.t, sol.y[1, :], label=model['name'] + '- q_p1')
        
        else:
            plt.plot(sol.t, sol.y[0, :], label=model['name'] + '- q_o')
            plt.plot(sol.t, sol.y[1, :], label=model['name'] + '- q_c')
            plt.plot(sol.t, sol.y[2, :], label=model['name'] + '- q_p1')

        

        plt.legend()
        plt.title("The change in drug quantity")
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()
    
    