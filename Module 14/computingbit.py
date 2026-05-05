'''
ComputingBit defines an API containing 3 methods that must be implemented by the Qubit subclass:
  1. probability_amplitudes
  2. validate_amplitudes
  3. experiment
'''

from abc import ABC, abstractmethod

class ComputingBit(ABC):
    @abstractmethod
    def probability_amplitudes(self):
        raise NotImplementedError("Did you implement the 'probability_amplitudes' method?")
  
    @abstractmethod
    def validate_amplitudes(self):
        raise NotImplementedError("Did you implement the 'validate_amplitudes' method?")

    @abstractmethod
    def experiment(self):
        raise NotImplementedError("Did you implement the 'experiment' method?")
