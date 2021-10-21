import matplotlib.pylab as plt
    
    """This code will import the object model and graph the solutions."""


class Solution:
    def __init__(self, models):
        self.models = models
        self.graph()

        """Looks at individual model created in model and prepares to plot the graph.
        """
    def graph(self):
        for model in models:
            if model.protocol.comps == 2:
                plt.plot(model.sol.t, model.sol.y[0, :], label="Two-compertment model" + '- q_c')
                plt.plot(model.sol.t, model.sol.y[1, :], label="Two-compertment model" + '- q_p1')
        
            else:
                plt.plot(model.sol.t, model.sol.y[0, :], label="Three-comparmtent model" + '- q_o')
                plt.plot(model.sol.t, model.sol.y[1, :], label="Three-comparmtent model" + '- q_c')
                plt.plot(model.sol.t, model.sol.y[2, :], label="Three-comparmtent model" + '- q_p1')
        
        """The graph will be plotted using the code below
        """
        plt.legend()
        plt.title("The change in drug quantity")
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()
    
    