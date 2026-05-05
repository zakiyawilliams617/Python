# main.py
# entry point for the Quantum Computation Simulation 
# reads qubit states and operator sequences from qubits.txt
# applies quantum gates (X and H) to each qubit
# and prints the initial state, final state, and experiment results 

from qubit import Qubit
from paulix import PauliX
from hadamard import Hadamard

def main():
    # open and read all lines from tne input file
    file = open("qubits.txt", "r")
    lines = file.readlines()
    file.close()


    # Process each line in the input file 
    for line in lines:
        # Split the lines in to parts, alpha, beta, and operator sequence
        parts = line.strip().split()
        alpha = float(parts[0])
        beta = float(parts[1])
        operators = parts[2:]

        # Validate that all operators in this line are either X or H
        valid_operators = True
        for op in operators:
            if op != "X" and op != "H":
                valid_operators = False

        # If any invalid operator is found, print error and skip to next line 
        if not valid_operators:
            print("Initial state: " + str(alpha) + "|0> + " + str(beta) + "|1>")
            print("Invalid operator.")
            print()
            continue 

        # Create a Qubi object with the given alpha and beta values
        qubit = Qubit(alpha, beta)

        # Print the initial state of the qubit before applying any gates 
        print("Initial state: " + str(qubit))

        # Apply each operator in sequence to the qubit
        for op in operators:
            if op == "X":
                gate = PauliX()   # PauliX (quantum not) gate
            else:
                gate = Hadamard()   # Hadamard (superposition) gate
            # operate() returns a new Qubit with the update stat
            qubit = gate.operate(qubit)

        # Print the final state after all gates have been applied
        print("Final state: " + str(qubit))

        # Run the probablistic experiment (100 measurements) and print results 
        qubit.experiment()
        print()

# Only call main() when this script is run directly 
if __name__ == "__main__":
    main()