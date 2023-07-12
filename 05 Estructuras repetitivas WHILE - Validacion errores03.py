def contar_vocales():
    frase = input("Ingresa una frase (presiona 'q' para terminar): ")
    contador = 0

    while frase.lower() != 'q':
        for letra in frase:
            if letra.lower() in 'aeiouáéíóú':
                contador += 1

        frase = input("Ingresa otra frase (presiona 'q' para terminar): ")

    print("Cantidad total de vocales encontradas:", contador)

contar_vocales()
