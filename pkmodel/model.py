"""
A model class for solving PK calculatins given a Protocol data class.
"""
from abc import ABC, abstractmethod
from .protocol import Protocol
import scipy.integrate


class AbstractModel(ABC):
    """ An abstract class for PK models"""

    def __init__(self, protocol: Protocol):
        """ Constructs object using a Protocol object

        :param protocol: Protocol object with all necessary parameters for model creation
        :type protocol: Protocol
        """
        self.protocol = protocol

    @abstractmethod
    def __eq__(self, other_model) -> bool:
        return self.protocol == other_model.protocol

    @abstractmethod
    def solve_ode(self):
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs(t, y),
            t_span=[self.protocol.t_eval[0], self.protocol.t_eval[-1]],
            y0=self.protocol.y0, t_eval=self.protocol.t_eval
        )
        return sol


class TwoCompartmentModel(AbstractModel):

    def __init__(self, protocol: Protocol):
        """
        Constructs object using a Protocol object

        :param protocol: Protocol object with all necessary parameters for model creation
        :type protocol: Protocol
        """
        super().__init__(protocol)
        self.sol = self.solve_ode()

    def rhs(self, t, y):
        """ Right-hand side of ODE being solved for PK model

        :param t: Time variable
        :type t: float
        :param y: drug concentration in different compartments
        :type y: list[float]
        :return: LHS of ODE
        :rtype: list[float]
        """
        Q_p1 = self.protocol.Q_p1
        V_c = self.protocol.V_c
        V_p1 = self.protocol.V_p1
        CL = self.protocol.CL
        X = self.protocol.X

        q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = self.protocol.dose(t, X) - q_c / V_c * CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]

    def solve_ode(self):
        """ Solves the ODE using scipy.integrate libary

        :return: The solved ODE
        :rtype: list[float]
        """
        return super().solve_ode()

    def __eq__(self, other_model) -> bool:
        return super().__eq__(other_model)


class ThreeCompartmentModel(AbstractModel):

    def __init__(self, protocol: Protocol):
        """
        Constructs object using a Protocol object

        :param protocol: Protocol object with all necessary parameters for model creation
        :type protocol: Protocol
        """
        super().__init__(protocol)
        self.sol = self.solve_ode()

    def rhs(self, t, y):
        """
        Right-hand side of ODE being solved for PK model

        :param t: Time variable
        :type t: float
        :param y: drug concentration in different compartments
        :type y: list[float]
        :return: LHS of ODE
        :rtype
        """
        Q_p1 = self.protocol.Q_p1
        V_c = self.protocol.V_c
        V_p1 = self.protocol.V_p1
        CL = self.protocol.CL
        X = self.protocol.X
        k_a = self.protocol.k_a

        q_o, q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqo_dt = self.protocol.dose(t, X) - (k_a * q_o)
        dqc_dt = k_a * q_o - (q_c * CL) / V_c - transition
        dqp1_dt = transition
        return [dqo_dt, dqc_dt, dqp1_dt]

    def solve_ode(self):
        """ Solves the ODE using scipy.integrate libary

        :return: The solved ODE
        :rtype: list[float]
        """
        return super().solve_ode()

    def __eq__(self, other_model) -> bool:
        return super().__eq__(other_model)
