import numpy as np
from src.utils.MathFunction import MathFunction

class TriangularFunction(MathFunction):
    def calculate(self, time: float) -> float:
        period = 1.0 / self.frecuency
        time_module = time % period
    
        return (4 * self.frecuency) * np.abs(time_module - period/2) - 1