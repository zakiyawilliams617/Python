# Defines the Hadamard class, which represents the Hadamard quantum gate
# The Hadamard gate places a qubit into an equally weighted superposition
# of the |0> and |1> basis states.
# Operator matrix: (1/sqrt(2)) * [[1, 1], [1, -1]]

import numpy
from qoperators import SingleQubitOperator
from qubit import Qubit

class Hadamard(SingleQubitOperator):

    # Constructor: initializes the Hadamard gate with its 2x2 operator matrix
    # Passes the matrix to the parent class SingleQubitOperator
    def __init__(self):
        matrix = numpy.array([[1 / numpy.sqrt(2), 1 / numpy.sqrt(2)],
                              [1 / numpy.sqrt(2), -1 / numpy.sqrt(2)]])
        SingleQubitOperator.__init__(self, matrix)

    # Applies the Hadamard operator matrix to the given qubit.
    # Multiples the 2x2 operator matrix by the qubit's 2x1 state vector
    # returns a new qubit object with the resulting superposition state
    def operate(self, qubit):
        old_state = qubit.get_state()
        # Matrix vector multiplication: new_state = H * old_state
        new_state = numpy.dot(self._operator_matrix, old_state)
        new_alpha = new_state[0][0]
        new_beta = new_state[1][0]
        return Qubit(new_alpha, new_beta)