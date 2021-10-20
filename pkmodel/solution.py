import matplotlib.pylab as plt
import numpy as np
import protocol as Protocol #

Class Solution: 


    def __init__(self, sol,protocol:Protocol):
        self.sol = sol
        graph()
        

    def graph (self):
        
        if self.type_of_compartment== 2:
            plt.plot(sol.t, sol.y[0, :], label=model['name'] + '- q_c')
            plt.plot(sol.t, .solution.y[1, :], label=model['name'] + '- q_p1')
        
        else type_of_compartment.self == 3:
            plt.plot(sol.t, sol.y[0, :], label=model['name'] + '- q_o)
            plt.plot(sol.t, sol.y[1, :], label=model['name'] + '- q_c')
            plt.plot(sol.t, sol.y[2, :], label=model['name'] + '- q_p1')

        

        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()
    
    