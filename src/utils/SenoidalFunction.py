import numpy as np
from src.utils.GraphFunction import GraphFunction

class SinoidalFunction(GraphFunction):
    def calculate(self, time: float):
        return self.amplitud * np.sin((2 * np.pi * self.frecuency * time) + self.fase)