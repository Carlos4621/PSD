from src.utils.ExponentialFunction import ExponentialFunction
from src.utils.Grapher import Grapher
from src.utils.SenoidalFunction import SinoidalFunction
from src.utils.SquareFunction import SquareFunction
from src.utils.TriangularFunction import TriangularFunction

class Tarea_1:

    # Los números mágicos son debido a parámetros de la tarea
    @staticmethod
    def iniciar():

        min_domain = -1
        max_domain = 6
        points = 1000
        graphic = Grapher(min_domain, max_domain, points)

        frecuency = 2

        exponential_function = ExponentialFunction(frecuency)
        senoidal_function = SinoidalFunction(frecuency)
        square_function = SquareFunction(frecuency)
        triangular_function = TriangularFunction(frecuency)

        time_sample = 0.05
        graphic.show_graph([exponential_function, senoidal_function, square_function, triangular_function], time_sample)
