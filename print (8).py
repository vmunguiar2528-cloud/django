import random
import getpass

def jugar():
    print("Jugador 1: elige un número secreto.")
    print("Jugador 2: intenta adivinarlo.")
    print("El número secreto se ocultará al escribirlo.")

    while True:
        try:
            numero_secreto = int(getpass.getpass("Jugador 1, escribe un número entre 1 y 100: "))
            if 1 <= numero_secreto <= 100:
                break
            print("El número debe estar entre 1 y 100.")
        except ValueError:
            print("Debes ingresar un número válido.")

    print("\nAhora le toca a Jugador 2.")
    input("Presiona Enter para empezar...")

    intentos = 0
    max_intentos = 6

    while intentos < max_intentos:
        try:
            intento = int(input("Jugador 2, ingresa tu número: "))
        except ValueError:
            print("Debes ingresar un número válido.")
            continue

        intentos += 1

        if intento == numero_secreto:
            print(f"¡Correcto! Jugador 2 adivinó el número {numero_secreto} en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("El número secreto es más alto.")
        else:
            print("El número secreto es más bajo.")
    else:
        print(f"¡Se acabaron los intentos! El número secreto era {numero_secreto}.")

    respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if respuesta == "s":
        jugar()
    else:
        print("¡Gracias por jugar!")

jugar()
numero_secreto = random.randint(1, 50)
intentos = 0
max_intentos = 6 


def jugar():
    print("Jugador 1: introduce un número secreto.")
    print("Jugador 2: intenta adivinarlo.")
    print("El número secreto no se mostrará en la terminal.")

    while True:
        try:
            numero_secreto = int(getpass.getpass("Jugador 1, escribe un número entre 1 y 100: "))
            if 1 <= numero_secreto <= 100:
                break
            else:
                print("El número debe estar entre 1 y 100.")
        except ValueError:
            print("Debes ingresar un número válido.")

    print("\nAhora le toca a Jugador 2. ¡No mires la pantalla del Jugador 1!")
    input("Presiona Enter cuando estés listo para empezar...")

    intentos = 0
    max_intentos = 6

    while intentos < max_intentos:
        try:
            intento = int(input("Jugador 2, ingresa tu número: "))           
            import getpass
            
            def jugar():
                print("Jugador 1: elige un número secreto.")
                print("Jugador 2: intenta adivinarlo.")
                print("El número secreto se ocultará al escribirlo.")
            
                while True:
                    try:
                        numero_secreto = int(getpass.getpass("Jugador 1, escribe un número entre 1 y 100: "))
                        if 1 <= numero_secreto <= 100:
                            break
                        else:
                            print("El número debe estar entre 1 y 100.")
                    except ValueError:
                        print("Debes ingresar un número válido.")
            
                print("\nAhora le toca a Jugador 2.")
                input("Presiona Enter para empezar...")
            
                intentos = 0
                max_intentos = 6
            
                while intentos < max_intentos:
                    try:
                        intento = int(input("Jugador 2, ingresa tu número: "))
                    except ValueError:
                        print("Debes ingresar un número válido.")
                        continue
            
                    intentos += 1
            
                    if intento == numero_secreto:
                        print(f"¡Correcto! Jugador 2 adivinó el número {numero_secreto} en {intentos} intentos.")
                        break
                    elif intento < numero_secreto:
                        print("El número secreto es más alto.")
                    else:
                        print("El número secreto es más bajo.")
                else:
                    print(f"¡Se acabaron los intentos! El número secreto era {numero_secreto}.")
            
                respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
                if respuesta == "s":
                    jugar()
                else:
                    print("¡Gracias por jugar!")
            
            jugar()
        except ValueError:
            print("Debes ingresar un número válido.")
            continue

        intentos += 1

        if intento == numero_secreto:
            print(f"¡Correcto! Jugador 2 adivinó el número {numero_secreto} en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("El número secreto es más alto.")
        else:
            print("El número secreto es más bajo.")
    else:
        print(f"¡Se acabaron los intentos! El número secreto era {numero_secreto}.")

    respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if respuesta == "s":
        jugar()
    else:
        print("¡Gracias por jugar!")

jugar()
import random

def jugar():
    print("Jugador 1: introduce un número secreto.")
    print("Jugador 2: intenta adivinarlo.")

    while True:
        try:
            numero_secreto = int(input("Jugador 1, escribe un número entre 1 y 100: "))
            if 1 <= numero_secreto <= 100:
                break
            else:
                print("El número debe estar entre 1 y 100.")
        except ValueError:
            print("Debes ingresar un número válido.")

    print("\nAhora le toca a Jugador 2. ¡No mires la pantalla del Jugador 1!")
    input("Presiona Enter cuando estés listo para empezar...")

    intentos = 0
    max_intentos = 6

    while intentos < max_intentos:
        try:
            intento = int(input("Jugador 2, ingresa tu número: "))
        except ValueError:
            print("Debes ingresar un número válido.")
            continue

        intentos += 1

        if intento == numero_secreto:
            print(f"¡Correcto! Jugador 2 adivinó el número {numero_secreto} en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("El número secreto es más alto.")
        else:
            print("El número secreto es más bajo.")

        if intentos == max_intentos:
            print(f"¡Se acabaron los intentos! El número secreto era {numero_secreto}.")

    respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if respuesta == "s":
        jugar()
    else:
        print("¡Gracias por jugar!")

jugar()
print("Bienvenido a Adivina el número!")
print("Tienes 6 intentos para adivinar un número entre 1 y 50.")

while intentos < max_intentos:
    try:
        apuesta = int(input("Ingresa tu número: "))
    except ValueError:
        print("Debes ingresar un número válido.")
        continue

    intentos += 1

    if apuesta == numero_secreto:
        print(f"¡Correcto! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        break
    elif apuesta < numero_secreto:
        print("El número es más alto.")
    else:
        print("El número es más bajo.")

    if intentos == max_intentos:
        print(f"¡Se acabaron los intentos! El número secreto era {numero_secreto}.")