import numpy as np
from src.utils.MathFunction import MathFunction

class ExponentialFunction(MathFunction):
    def calculate(self, time: float) -> float:
        return np.e**(-2 * time) * (0 if time < 0 else 1)