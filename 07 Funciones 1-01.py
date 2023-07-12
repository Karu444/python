def menu():
    print("Bienvenido al menú")
    print("1. Contar palabras.")
    print("2. Calcular MCD de dos números.")
    print("3. Calcular IVA.")
    print("4. Salir.")
    print("vvvvv elige una opción según tu necesidad vvvvv")
    return int(input(" "))


def contar_palabras():
    frase = input("Digite la frase: ")
    palabras = frase.split()
    cantidad = len(palabras)
    print(f"Cantidad de palabras: {cantidad}")


def calcular_mcd():
    a = int(input("Escriba un número: "))
    b = int(input("Escriba un número menor al anterior: "))
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a


def calcular_total_factura():
    cantidad_sin_iva = float(input("Escriba la cantidad sin IVA: "))
    porcentaje_iva = float(input("Escriba el IVA: "))
    total = cantidad_sin_iva + (cantidad_sin_iva * porcentaje_iva / 100)
    print(f"Total de la factura: {total}")


opcion = menu()

if opcion == 1:
    contar_palabras()
elif opcion == 2:
    print("MCD de los dos números es:", calcular_mcd())
elif opcion == 3:
    calcular_total_factura()
elif opcion == 4:
    print("FIN DEL PROGRAMA")
    exit()