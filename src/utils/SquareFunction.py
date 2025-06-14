from src.utils.GraphFunction import GraphFunction

class SquareFunction(GraphFunction):
    def calculate(self, time: float):
        period = 1.0 / self.frecuency
        time_module = time % period

        return 1 if time_module < 0.5 * period else -1