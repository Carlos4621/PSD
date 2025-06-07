from src.utils.Grapher import Grapher
from src.utils.SenoidalFunction import SinoidalFunction

class Tarea_2:

    @staticmethod
    def iniciar(frecuencia : float):

        min_domain = -1
        max_domain = 6
        points = 1000
        graphic = Grapher(min_domain, max_domain, points)

        senoidal_function = SinoidalFunction(frecuencia, nombre=f"f = {frecuencia} Hz, A = 1, fase = 0")

        time_sample = 0.05
        graphic.show_graph([senoidal_function], time_sample)