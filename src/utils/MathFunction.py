from abc import ABC, abstractmethod

class MathFunction(ABC):
    def __init__(self, frecuency : float):
        self._frecuency = frecuency

    @abstractmethod
    def calculate(self, time : float) -> float:
        """
        Evalúa el valor de time en la función dada

        Args:
            time: Valor del tiempo a evaluar

        Returns:
            Valor de la función en el tiempo dado
        """
        pass

    @property
    def frecuency(self):
        return self._frecuency

    @frecuency.setter
    def frecuency(self, nuevaFrecuencia: float):
        if (nuevaFrecuencia <= 0):
            raise ValueError("La frecuencia no debe ser menor o igual a 0")