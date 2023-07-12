cadena = "abcedeefghijkmnlopqrstuvwxyz"
cadenareducida = ''
letraanterior = ''

for letra in cadena:
    if letra != letraanterior:
        cadenareducida += letra
    letraanterior = letra

if len(cadenareducida) > 0 and cadenareducida[-1] == letraanterior:
    cadenareducida = ''

print(cadenareducida)
