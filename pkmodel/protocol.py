#
# Protocol class
#

import numpy as np
import matplotlib.pyplot as plt


class Protocol:
    """A Pharmokinetic (PK) protocol

    Contains all parameters needed to run 2- or 3-compartment models, and dose
        function.

    :param comps: int number indicating which model (2- or 3-compartment) to be
        used
    :param Q_p1: float transition rate between central component and
        peripheral component
    :param V_c: float volume of central component
    :param V_p1: float volume of peripheral component
    :param CL: float elimination rate for drug in central component
    :param X: float amount of drug administered
    :param dose_on: int number of time units (thousandths of an hour)
        for which drug is administered at a time (dose_on = 0 -> single dose
        at time 0)
        If dose_off = 0, dose_on can be 0 (instantaneous dose) or 1
        (continuous dose)
    :optional param dose_off: int number of time units (thousandths of an hour)
        for which drug is not administered at a time
        (default value 0 -> drug is continuously administered,
        unless dose_on = 0 which overrides this)
    :optional param k_a: float for three-component model only absorption rate
        for subcutaneous dosing
    :optional param graph_preview: bool to trigger graph preview of dosing
        function (default value False -> preview not shown)

    :method dose: takes parameters t, X and returns X or 0, depending on value
        of t. Represents a variable dose function over time.
    """

    def __init__(self, comps: int, Q_p1: float, V_c: float, V_p1: float,
                 CL: float, X: float, dose_on: int, dose_off: int = 0,
                 k_a: float = 0, graph_preview: bool = False):
        self.comps = comps
        self.Q_p1 = Q_p1
        self.V_c = V_c
        self.V_p1 = V_p1
        self.CL = CL
        self.X = X
        self.dose_on = dose_on
        self.dose_off = dose_off
        self.k_a = k_a
        self.eval_subdiv = 1000
        self.t_eval = np.linspace(0, 1, self.eval_subdiv)
        self.y0 = np.array([0.0, 0.0])
        self.graph_preview = graph_preview

        assert comps == 2 or comps == 3, "Number of components must be 2 or 3"
        assert Q_p1 >= 0, "Compartment transition rate must be non-negative"
        assert V_c > 0 and V_p1 > 0, "Volume of compartments must be positive"
        assert CL >= 0, "Clearance rate must be non-negative"
        assert X > 0, "Dose administered must be positive"
        assert dose_on >= 0, "dose_on must be non-negative"
        assert dose_off >= 0, "dose_off must be non-negative"
        assert k_a >= 0, "Subcutaneous absorption rate must be non-negative"

        if self.graph_preview:
            plt.figure
            axs = plt.axes()
            axs.plot(self.t_eval, self.dose(self.t_eval, self.X))
            axs.set_ylabel('Dose (ng)')
            axs.set_xlabel('Time (hr)')
            axs.set_title('Dose administered over time')
            plt.show()

    def dose(self, t, X):
        """Dose function to be evaluated at all times t in [0,1] when solving ODEs

        Args:
            t (float): time value, between 0 and 1
            X (float): magnitude of dosage applied at all relevant times

        Returns:
            float: amount of drug administered at time t
        """
        if self.dose_on == 0:
            return X * (t == 0)
        else:
            return X * ((self.eval_subdiv - 1) * t % (self.dose_on
                        + self.dose_off) < self.dose_on)

    def __eq__(self, other_prot):
        if self.comps != other_prot.comps:
            return False
        elif self.Q_p1 != other_prot.Q_p1:
            return False
        elif self.V_c != other_prot.V_c:
            return False
        elif self.V_p1 != other_prot.V_p1:
            return False
        elif self.X != other_prot.X:
            return False
        elif self.dose_on != other_prot.dose_on:
            return False
        elif self.dose_off != other_prot. dose_off:
            return False
        elif self.k_a != other_prot.k_a:
            return False

        return True
