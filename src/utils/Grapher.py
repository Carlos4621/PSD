import matplotlib.pyplot as plt
import numpy as np
from src.utils.GraphFunction import GraphFunction

class Grapher:
    def __init__(self, min_domain : int, max_domain: int, points : int):
        self.max_domain = max_domain
        self.min_domain = min_domain
        self._points = points

    def show_graph(self, functions : list[GraphFunction], time_sample : float, sample_functions : list[GraphFunction] = [],
                    x_label_title : str = "Tiempo[s]", y_label_title : str = "Amplitud"):

        figures, axes = plt.subplots(len(functions), 1, sharex=True, squeeze=False) # type: ignore
        values_to_evaluate_continous = np.linspace(self.min_domain, self.max_domain, self.points)

        values_to_evaluate_discrete = np.arange(self.min_domain, self.max_domain, time_sample)
        
        for i in range(len(functions)):
            vectorized_function = np.vectorize(functions[i].calculate)

            calculated_continous_values = vectorized_function(values_to_evaluate_continous)
            calculated_discrete_values = vectorized_function(values_to_evaluate_discrete)

            axes[i, 0].set_xlabel(x_label_title)
            axes[i, 0].set_ylabel(y_label_title)
            axes[i, 0].set_title(functions[i].nombre)
            axes[i, 0].plot(values_to_evaluate_continous, calculated_continous_values)
            axes[i, 0].stem(values_to_evaluate_discrete, calculated_discrete_values)
            axes[i, 0].grid(True)

            if i < len(sample_functions):
                vectorized_sample_function = np.vectorize(sample_functions[i].calculate)
                calculated_sample_values = vectorized_sample_function(values_to_evaluate_continous)
                axes[i, 0].plot(values_to_evaluate_continous, calculated_sample_values, color="red")

        plt.tight_layout()
        plt.show() # type: ignore

    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self, new_points : int):
        if new_points <= 0:
            raise ValueError("Points can't be minor or equal to 0")
        
        self._points = new_points