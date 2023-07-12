def buscar_palabra_clave():
    while True:
        oracion = input("Ingresa una oración (o escribe 'salir' para terminar el programa): ")
        if oracion.lower() == "salir":
            print("Programa finalizado.")
            break
        
        palabra_clave = input("Ingresa una palabra clave: ")
        
        if palabra_clave.lower() in oracion.lower():
            print("¡La palabra clave se encontró en la oración!")
            break
        else:
            print("La palabra clave no se encontró en la oración. Intenta nuevamente.")

buscar_palabra_clave()

