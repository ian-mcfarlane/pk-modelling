"""
A model class for solving PK calculatins given a Protocol data class.
"""
from abc import ABC, abstractmethod
from solution import Solution
from protocol import Protocol
import scipy.integrate

class AbstractModel(ABC):
    """An abstract base (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, protocol: Protocol):
        pass

    @abstractmethod
    def solve_ode(self):
        pass

    @property
    @abstractmethod
    def get_solution(self) -> Solution:
        pass


class ThreeCompartmentModel(AbstractModel):

    def __init__(self, protocol: Protocol):
        self.protocol = protocol
        self.solution = self.solve_ode()

    def rhs(self, t, y):
        """[summary]

        :param t: [description]
        :type t: [type]
        :param y: [description]
        :type y: [type]
        :return: [description]
        :rtype: [type]
        """        
        Q_p1 = self.protocol.Q_p1
        V_c = self.protocol.V_c
        V_p1 = self.protocol.V_p1
        CL = self.protocol.CL
        X = self.protocol.X
        k_a = self.protocol.k_a

        q_o, q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqo_dt = self.protocol.dose(t,X) - (k_a*q_o)
        dqc_dt = k_a*q_o - (q_c*CL)/V_c - transition
        dqp1_dt = transition
        return [dqo_dt, dqc_dt, dqp1_dt]

    def solve_ode(self):
        """[summary]

        :return: [description]
        :rtype: [type]
        """        
        
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs(t, y),
            t_span=[self.protocol.t_eval[0], self.protocol.t_eval[-1]],
            y0=self.protocol.y0, t_eval=self.protocol.t_eval
        ) 
        return Solution(sol)
    
    @property
    def get_solution(self) -> Solution:
        """ Returns the Solution class of the solved PK model.

        :return: Solution class used to display result.
        :rtype: Solution
        """        
        return self.solution