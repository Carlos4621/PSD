import numpy as np
from src.utils.MathFunction import MathFunction

class SinoidalFunction(MathFunction):
    def calculate(self, time: float):
        return np.sin(2 * np.pi * self.frecuency * time)