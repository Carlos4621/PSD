import numpy as np
from src.utils.GraphFunction import GraphFunction

class TriangularFunction(GraphFunction):
    def calculate(self, time: float) -> float:
        period = 1.0 / self.frecuency
        time_module = time % period
    
        return (4 * self.frecuency) * np.abs(time_module - period/2) - 1