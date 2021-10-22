import matplotlib.pylab as plt
import datetime


class Solution:
    """This code will import the list models, which contains model objects
    created in model.py and graph the solution by calling the function graph.
    :param models: list[Model] contain models to be graphed.
    Each model will have attributes associated with it such as sol (solution)
    and protocol."""

    def __init__(self, models, no_graph=False):
        self.models = models
        self.no_graph = no_graph
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
            dose_type = self.get_dose_type(model)

            if model.protocol.comps == 2:
                model_type = ", IV"
                plt.plot(model.sol.t, model.sol.y[0, :],
                         label=model.protocol.label + model_type + ', ' + dose_type
                         + '- q_c')
                plt.plot(model.sol.t, model.sol.y[1, :],
                         label=model.protocol.label + model_type + ', ' + dose_type
                         + '- q_p1')

            elif model.protocol.comps == 3:
                model_type = ", SC"
                plt.plot(model.sol.t, model.sol.y[0, :],
                         label=model.protocol.label + model_type + ', ' + dose_type
                         + '- q_o')
                plt.plot(model.sol.t, model.sol.y[1, :],
                         label=model.protocol.label + model_type + ', ' + dose_type
                         + '- q_c')
                plt.plot(model.sol.t, model.sol.y[2, :],
                         label=model.protocol.label + model_type + ', ' + dose_type
                         + '- q_p1')

        plt.legend()
        plt.title("The change in drug quantity")
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        now = datetime.datetime.now()
        plt.savefig("Outputs/PK-Modelling-" + str(now.strftime("%Y%m%d_%H-%M-%S")) + ".png")
        if not self.no_graph:
            plt.show()

    def get_dose_type(self, model):
        if model.protocol.dose_on == 0:
            return "Instantaneous"

        elif model.protocol.dose_off == 0:
            return "Continuous"

        else:
            return "Intermittent"
