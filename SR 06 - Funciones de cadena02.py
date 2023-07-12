letra1 = ""
letra2 = ""
round = 1
verificasion = 1
print("\n\tReduccion de caracteres")

while True:
    palabra = input("Ingrese una serie de caracteres: ")
    if palabra.strip().isalpha():
        break
    else:
        print("Ingrese solo letras")
nuevapalabra = palabra

while True:
    for i in nuevapalabra.lower():
        if round % 2 != 0:
            letra1 = i
        if round % 2 == 0:
            letra2 = i
        round += 1
        if letra1 == letra2:
            nuevapalabra = nuevapalabra.replace(i,"",2)
            letra1 = ""
            letra2 = ""
    round = 1
    if nuevapalabra == "":
        nuevapalabra = "Cadena Vacia"
        break
    if len(nuevapalabra) == verificasion:
        break
    verificasion += 1

print(f"\nLa cadena resultante de la reduccion es: {nuevapalabra.strip()}\n")