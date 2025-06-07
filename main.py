import sys
from src.Tarea1 import Tarea_1
from src.Tarea2 import Tarea_2
from src.Tarea3 import Tarea_3
from src.Tarea4 import Tarea_4

def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py arg")
        exit()

    match sys.argv[1]:
        case "tarea1":
            Tarea_1.iniciar()

        case "tarea2":
            if len(sys.argv) != 3:
                print("Usage: python main.py tarea2 amplitud")
                exit()
            Tarea_2.iniciar(float(sys.argv[2]))
            
        case "tarea3":
            if len(sys.argv) != 5:
                print("Usage: python main.py tarea3 amplitud frecuencia fase")
                exit() 
            Tarea_3.iniciar(float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))

        case "tarea4":
            if len(sys.argv) != 3:
                print("Usage: python main.py tarea4 resolution")
                exit()
            Tarea_4.iniciar(int(sys.argv[2]))

        case _:
            print("Invalid argument")

if __name__ == "__main__":
    main()
