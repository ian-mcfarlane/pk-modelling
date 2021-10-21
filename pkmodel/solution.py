import matplotlib.pylab as plt
from .protocol import Protocol


class Solution:
    def __init__(self, sol, protocol: Protocol):
        self.sol = sol
        self.protocol = protocol
        self.graph()

        
    def graph(self):
        
        if self.protocol.comps == 2:
            plt.plot(self.sol.t, self.sol.y[0, :], label="Two-compertment model" + '- q_c')
            plt.plot(self.sol.t, self.sol.y[1, :], label="Two-compertment model" + '- q_p1')
        
        else:
            plt.plot(self.sol.t, self.sol.y[0, :], label="Three-comparmtent model" + '- q_o')
            plt.plot(self.sol.t, self.sol.y[1, :], label="Three-comparmtent model" + '- q_c')
            plt.plot(self.sol.t, self.sol.y[2, :], label="Three-comparmtent model" + '- q_p1')

        plt.legend()
        plt.title("The change in drug quantity")
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()
    
    