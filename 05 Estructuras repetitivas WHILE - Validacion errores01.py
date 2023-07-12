import random

puntuacion_maxima = 0
jugador_maximo = ""

print("¡Bienvenido a Adivina el Número!")
print("Estoy pensando en un número entre 1 y 100. ¡Adivina cuál es!")

while True:
    jugador = input("Ingresa tu nombre: ")
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    while not adivinado:
        intento = int(input("Introduce tu suposición: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            adivinado = True

    print(f"¡Felicidades, {jugador}! Adivinaste el número en {intentos} intentos.")

    if intentos > puntuacion_maxima:
        puntuacion_maxima = intentos
        jugador_maximo = jugador

    continuar = input("¿Quieres jugar de nuevo? (s/n): ")
    if continuar.lower() != "s":
        break

print(f"\nLa mayor puntuación fue de {puntuacion_maxima} intentos, lograda por {jugador_maximo}. ¡Felicidades!")
        
