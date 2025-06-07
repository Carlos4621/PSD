import numpy as np
import matplotlib.pyplot as plt

class Tarea_4:
    
    @staticmethod
    def iniciar(resolution : int):
        V_FS = 5.0
        levels = 2 ** resolution
        step_size = V_FS / (levels - 1)

        digital_input = np.arange(levels)
        analog_output = digital_input * step_size

        plt.figure(figsize=(8, 5))
        plt.step(digital_input, analog_output, where='post')
        plt.title('Salida')
        plt.xlabel('Entrada digital')
        plt.ylabel('Salida analógica (V)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()