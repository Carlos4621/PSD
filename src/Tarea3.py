from src.utils.Grapher import Grapher
from src.utils.SenoidalFunction import SinoidalFunction

class Tarea_3:

    @staticmethod
    def iniciar(amplitud : float, frecuencia : float, fase : float):
        
        min_domain = -1
        max_domain = 6
        points = 1000
        graphic = Grapher(min_domain, max_domain, points)

        senoidal_function = SinoidalFunction(frecuencia, amplitud, fase, f"f = {frecuencia} Hz, A = {amplitud}, fase = {fase}")
        sample_senoidal_function = SinoidalFunction(1, 1)

        time_sample = 0.05
        graphic.show_graph([senoidal_function], time_sample, [sample_senoidal_function])