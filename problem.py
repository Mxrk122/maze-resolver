from abc import ABC, abstractmethod
class Problem(ABC):

    @abstractmethod
    def def_initial_state(self):
        pass

    @abstractmethod
    def actions(self, s):
        pass

    @abstractmethod
    def results(self, s, a):
        pass
    
    @abstractmethod
    def goalTest(self, s):
        pass

    @abstractmethod
    def stepCost(self, s, a, s_):
        pass

    @abstractmethod
    def pathCost(self, states):
        pass