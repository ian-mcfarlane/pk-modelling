import matplotlib.pylab as plt


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

        for model in self.models:
            if model.protocol.comps == 2:
                plt.plot(model.sol.t, model.sol.y[0, :],
                         label="Two-compartment model" + '- q_c')
                plt.plot(model.sol.t, model.sol.y[1, :],
                         label="Two-compartment model" + '- q_p1')

            else:
                plt.plot(model.sol.t, model.sol.y[0, :],
                         label="Three-compartment model" + '- q_o')
                plt.plot(model.sol.t, model.sol.y[1, :],
                         label="Three-compartment model" + '- q_c')
                plt.plot(model.sol.t, model.sol.y[2, :],
                         label="Three-compartment model" + '- q_p1')

        plt.legend()
        plt.title("The change in drug quantity")
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()

