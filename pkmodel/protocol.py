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

    :method dose: takes parameters t, X and returns X or 0, depending on value
        of t. Represents a variable dose function over time.
    """

    def __init__(self, comps, Q_p1, V_c, V_p1, CL, X, dose_on,
                 dose_off=0, k_a=0):
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

        dose_preview = input('Preview dosing function? y/n: ')
        if dose_preview == 'y' or dose_preview == 'Y':
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
