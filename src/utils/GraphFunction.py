from abc import ABC, abstractmethod

# Clase para representar una función graficable con Grapher
class GraphFunction(ABC):
    def __init__(self, frecuency : float, amplitud : float = 1, fase : float = 0, nombre : str = ""):
        self._frecuency = frecuency
        self._amplitud = amplitud
        self._fase = fase
        self.nombre = nombre

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
    def frecuency(self, nueva_frecuencia : float):
        if (nueva_frecuencia <= 0):
            raise ValueError("La frecuencia no debe ser menor o igual a 0")
        self._frecuency = nueva_frecuencia
        
    @property
    def amplitud(self):
        return self._amplitud
    
    @amplitud.setter
    def amplitud(self, nueva_amplitud : float):
        if (nueva_amplitud <= 0):
            raise ValueError("La amplitud no debe ser menor o igual a 0")
        self._amplitud = nueva_amplitud

    @property
    def fase(self):
        return self._fase
    
    @fase.setter
    def fase(self, nueva_fase : float):
        if (nueva_fase <= 0):
            raise ValueError("La fase no debe ser menor a 0")
        self._fase = nueva_fase