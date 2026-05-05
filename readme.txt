Name: Zakiya Williams

Module Info: Module  Assignment 14: Final Exam Programming Assignment: Quantum Computing Simulator Due on 05/05/2026

Approach:
The overall design required simulation of quantum bits(qubits) using OOP (object oriented programming). I had to model quibits as vectors and quantum gates as matrices, then use matrix multiplication to apply gates to qubits.

I built two inheritance chains the Computingbit (provided) abstract class extended by the qubit class and a custom SingleQubitOperator abstract class was extended by the PauliX and Hadamard gate classes.

The Qubit stores its state as a 2x1 numpy column vector that has alpha and beta, the probability amplitudes. Alpha squared represents the probablity of measuring a |0> and beta squared represents the probabliity of measuring a |1>. The validate_amplitudes() method enforces the quantum mechanics rule that these two probabilities must always sume to 1. The experiment() method simulates measuring the qubit 100 times using numpy.random.binomial, where beta squared serves as the probability of measuring a |1> on each trial, this is why the percentages vary a little between runs.

Each gate class stores a 2x2 numpy operator matrix. The PauliX gate uses the matrix [[0,1][1.0]], this flips |0> to |1> and vice versa. It is the quantim equivalent of a not gate. The Hadamard gate places a quit into an equally weighted superposition of both basis states. I produced a new state to return a new qubit object by calling numpy.() to multiply the gate matrix by the qubit's state vector.

The main.py file ties everything together by reading qubits.txt line by line, validating that all operators either X or H, creating a qubit from the alpha and beta values, applying each gate in sequence and printing the initial state, final state and experiment results for each qubit. 

Known bugs: n/a
Citations: n/a

