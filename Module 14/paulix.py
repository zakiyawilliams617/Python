# Defines the PauliX class, which represents the Pauli X quantum gate
# The PauliX gate is the quantum equivalent fo a classical NOT gate
# It flips |0> to |1> and |1> to |0>
# Operator Matrix: [[0, 1]. [1, 0]]

import numpy
from qoperators import SingleQubitOperator
from qubit import Qubit

class PauliX(SingleQubitOperator):

    # Constructor: initializes the PauliX gate with its 2x2 operator matrix
    # Passes the matrix to the parent class SingleQubitOperator
    def __init__(self):
        matrix = numpy.array([[0, 1], [1, 0]])
        SingleQubitOperator.__init__(self, matrix)

    # Applies the PauliX operator matrix to the given qubit
    # Multiplies the 2x2 operator matrix by the qubit's 2x1 state vector
    # Returns a new Qubit object with the resulting state
    def operate(self, qubit):
        old_state = qubit.get_state()
        # Matrix vector multiplication: new_state = X * old_state
        new_state = numpy.dot(self._operator_matrix, old_state)
        new_alpha = new_state[0][0]
        new_beta = new_state[1][0]
        return Qubit(new_alpha, new_beta)