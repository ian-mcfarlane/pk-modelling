import matplotlib.pylab as plt
import matplotlib.pyplot 
import numpy as np

class Solution:
    """This code will import the list models, which contains model objects
    created in model.py and graph the solution by calling the function graph.

    :param models: list[Model] contain models to be graphed.
    Each model will have attributes associated with it such as sol (solution)
    and protocol."""

    def __init__(self, models):
        self.models = models
        self.graph()

    def graph(self):
        """Function graph will use the for loop to go through the list of models.

        If the model used the two compartment models, it will plot two lines,
        which represents the quantity of drugs in the main compartment and the
        peripheral compartmentat all time points.

        If the model used the three compartment model, the plot contain extra
        information, and it will contain an extra line, which will represnt
        the quantity of drugs in the third comparment (e.g. subcutaneous
        scenario) at all time points.  """

        num_graphs = np.linspace(1, int(len(self.models)), int(len(self.models)))
        fig = matplotlib.pyplot.figure(figsize=(10.0,3.0))  

        for model in self.models:
            count = 0
            count = count +1

            if model.protocol.comps == 2:
                ax(count)=plt.subplot(2,2,count)
                ax(count).set_ylabel("drug mass [ng]")
                ax(count).set_xlabel("time [h]")
                plt.plot(model.sol.t, model.sol.y[0, :],
                        label=model.protocol.label + '- q_c')
                plt.plot(model.sol.t, model.sol.y[1, :],
                        label=model.protocol.label + '- q_p1')
                

            else:
                ax(count)=plt.subplot(2,2,count)
                ax(count).set_ylabel("drug mass [ng]")
                ax(count).set_xlabel("time [h]")
                plt.plot(model.sol.t, model.sol.y[0, :],
                        label=model.protocol.label + '- q_o')
                plt.plot(model.sol.t, model.sol.y[1, :],
                        label=model.protocol.label + '- q_c')
                plt.plot(model.sol.t, model.sol.y[2, :],
                        label=model.protocol.label + '- q_p1')
        
        plt.show()
        


        
