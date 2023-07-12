contrasena = input("Ingresa una contraseña: ")

if len(contrasena) >= 8:

    tieneminuscula = False
    tienemayuscula = False
    tienenumero = False
    tieneespecial = False

    index = 0
    while index < len(contrasena):
        caracter = contrasena[index]
        if caracter.islower():
            tieneminuscula = True
        elif caracter.isupper():
            tienemayuscula = True
        elif caracter.isdigit():
            tienenumero = True
        elif caracter in "%^&!?¡¡/$#":
            tieneespecial = True
        
        index += 1

    if tieneminuscula and tienemayuscula and tienenumero and tieneespecial:
        print("Contraseña válida")
    else:
        print("Contraseña inválida")
else:
    print("Contraseña inválida")
