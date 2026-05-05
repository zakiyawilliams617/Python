# Defines the abstract base class SingleQubitOperator
# all single qubit quantum gate classes (PauliX/Hadamard)
# inherit from this class and must implement the operate() method.

from abc import ABC, abstractmethod

class SingleQubitOperator(ABC):

    # Constructor: stores the 2x2 operator (gate) matrix as an instance variable
    # Subclasses call this via SingleQubitOperator.__init__(self, matrix).
    def __init__(self, operator_matrix):
        self._operator_matrix = operator_matrix

    # Abstract method that apples this gate's operator matrix to a qubit
    # Must be implemented by all subclasses
    # Accepts a Qubit object and returns a new Qubit with the updated state.
    @abstractmethod
    def operate(self, qubit):
        pass