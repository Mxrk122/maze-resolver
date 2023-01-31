class Path(object):
    def __init__(self, states: list):
        self.states = states
    
    def end(self):
        #Devuelve el final de la lista
        return self.states[len(self.states) - 1]
    
    def extendFrom(self, arr: object):
        for element in arr.states:
            self.states.append(element)
    
    def addStep(self, step):
        self.states.append(step)

    def getStates(self):
        return self.states

    def __eq__(self, __other: object):
        if self.states == __other.states:
            return True
        else:
            return False
    
    def __str__(self) -> str:
        return str(self.states)