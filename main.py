import sys
from src.Tarea1 import Tarea_1

def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py arg")
        exit()

    match sys.argv[1]:
        case "tarea1":
            Tarea_1.iniciar()

        case _:
            print("Invalid argument")

if __name__ == "__main__":
    main()
