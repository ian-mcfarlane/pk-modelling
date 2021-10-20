"""
A model class for solving PK calculatins given a Protocol data class.
"""
from abc import ABC, abstractmethod
from solution import Solution
from protocol import Protocol


class AbstractModel(ABC):
    """An abstract base (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, protocol: Protocol):
        self.__protocol = protocol

    @abstractmethod
    def solve_ode(self):
        pass

    @property
    @abstractmethod
    def get_solution(self) -> Solution:
        pass
