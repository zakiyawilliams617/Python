# Defines the Qubit class whic represents a quantum bit(qubit)
# A qubit can exist in a superposition of the |0> and |1> basis states
# represents a 2x1 Numpy column vector [alpha, beta]

import numpy
from computingbit import ComputingBit

class Qubit(ComputingBit):

    # Constructor: initializes the qubit state as a 2x1 NumPy column vector
    # alpha is the amplitude for the |0> basis state
    # beta is the amplitude for the |1> basis state
    # Calls validate_amplitude() to check that alpha^2 + beta^2 == 1
    def __init__(self, alpha, beta):
        self._state = numpy.array([[alpha], [beta]])
        self.validate_amplitudes()

    # Returns the squared amplitudes (probabilities) of measuring |0> and |1>
    # alpha^2 is the probability of measuring |0>
    # beta^2 is the probability of measuring |1>
    def probability_amplitudes(self):
        alpha = self._state[0][0]
        beta = self._state[1][0]
        return alpha ** 2, beta ** 2
    
    # Checks that the sum of squared amplitudes equals 1.
    # If not, prints "Invalid probabilty amplitudes(s)"
    # This enforces the quatume mechanics rule
    # that all probabilities must sum to 1
    def validate_amplitudes(self):
        alpha = self._state[0][0]
        beta = self._state[1][0]
        total = round(alpha ** 2 + beta ** 2, 10)
        if total != 1.0:
            print("Invalid probability amplitude(s).")

    # Simulates measuring the qubit 100 times using a binomial distribution
    # beta^2 is the probability of measuring |1> on each trial
    # Prints the percentage of 0's and 1's measured across all 100 trials
    def experiment(self):
        alpha_sq, beta_sq = self.probability_amplitudes()
        count_zero = 0
        count_one = 0
        i = 0
        while i < 100:
            # Sample from binomial: 1 = measured |1>, 0 = measured |0>
            sample = numpy.random.binomial(1, beta_sq)
            if sample == 0:
                count_zero = count_zero + 1
            else: 
                count_one = count_one + 1
            i = i + 1
        print("Percentage of 0's measured: " + str(count_zero / 100))
        print("Percentage of 1's measured: " + str(count_one / 100))

    # Returns the current 2x1 NumPy state vector of the qubit
    def get_state(self):
        return self._state 
    
    # Updates the qubit's state vector, used after applying a quantum gate
    def set_state(self, new_state):
        self._state = new_state

    # Returns a human readable string representation of the qubit state
    # Format: alpha|0> + beta |1>
    def __str__(self):
        alpha = self._state[0][0]
        beta = self._state[1][0]
        return str(alpha) + "|0> + " + str(beta) + "|1>"
        