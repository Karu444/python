import json, os
os.system("clear")

def print_car():
    car = r'''
                                                    ___________
                                          __..--""""           """"--..__
                                      _.-"""""""""""-----...      ______ `.
                                   .-"                      l ,-""    \ "-.`.
                                .-"                         ; ;        ;   \ ""--.._
                              .'                           : :         |    ;      .l
                        _.._.'                             ; ;  ___    |    ;    .' :
                       (  .'                              : :  :   ".  :..-'   .'    ;
                        )'                                | ;  ; __.'-"(     .'  .--.:
                ___...-'""""----....____          ______.-' :-/.'       \_.-'  .' .-.\
        __..--""                        """"""""""          /\"          ;    / .gs./\;
    _.-"                                                   /  ;          |   . d$P"Tb
 .-""-,                       ____                        /   |          :   ;:$$   $;
.'     ;                    ,""    ""--..__               /    :          |   $$$;   :$
/"-._  /                     ;       ____..-'    .-"""-.  /     :          ;  _$$$;   :$
:     ""--.._          ___....+---""""          .'  _._  \/      |         _:-" $$$;   :$
;                                              /  .d$$$b./       ;      .-".'   :$$$   $P
:            .----...____                      :  dP' `T$P        |   .-" .' _.gd$$$$b_d$'
;    __...---|    Karu    |----....____         | :$     $b        : .'   (.-"  `T$$$$$$P'
;  .';       '----...____;       /    "-.      ; $;     :$;_____..-"  .-"                  
: /  :                          /        \__..-':$       $$ ;-.    .-"                     
 Y    ;                        /          ;     $;       :$;|  `.-"                        
 :    :                       /           |     $$       $$;:.-"                           
 '$$$ggggp...____            /            :     :$;     :$$                                
  $$$$$$$$$$$$   """"----...:________....gggg$$$$$$     $$;                                
  'T$$$$$$$$P'                           T$$$$$$$$$b._.d$P                                 
    `T$$$$P'                              T$$$$$$$$$$$$$P                                   
                                           `T$$$$$$$$$P'                                   
    '''
    print(car)

def print_car_v2():
    car_v2 = '''
                                        ____

                             ______...-----\'_\'____\\.

             _____.....----==---\'\\|-----\'\'\'\'\'        \

            /--------\'\'\'\'\'\'  ____ |                   \

           /  __..--- | .-\'\'    \|\                   \\-___

          /| |       || |     __ | \           ____..-\'    `---._

         //  |       || |    [__]| |__...----\'\'\'\'                  `-.__

 _______//|  |       || |______\\\\| \\ == _____         ____..---\'\'\'\'   \

/_______/ |  `-------\'|         `\\  |==.     ``---.--\'   .-\\\\\\\\\\\\| )

|         | [-]       |[-]          | //          | [ ] (  )|||||||||_\'|

|         \\\\           |             |// .-------   \\_____`.----\'\'  \\ ()|

|    _____ \\\\          |         ___ |` /    ____\\\\_   |   (_) |__..-\'   |

\\\\   /     \\\\ \\  ____..-| -----\'\'\'\'\'    | /  .-\'      `-_|_               _|

|  /  _--\'-\\\\ \\         \\\\            | | /    ___     \\ |  ____:K_F:-\'\'/

| |  /---_    `-.______|__...------\'/ //  .-\'   `\\\\    \\|_/      __/_-/

 \\\\| / .-. \\\\   _ `--..__\\\\___...-----\' | |  |  .-.  |   | ____---\'/    |

   | /   \\\\ \\  \\`-_____....-----------\'_|  | (   ) |   |     `--\'    /

   | | ( )| |  |__\\\\________/__..-\'     \\\\  \\  `-\'  /   |-\\         /

   \\\\ \\    / |  |       \\_     _/        \\\\  `-.__.\'   /    `--.__.-\'

    \\ `--\' /  /          `---\'           \\\\        _/

     \\\\____/__/                             `------\'
    '''
    print(car_v2)

def menu_autos():
    os.system("clear")
    print("=" * 48)
    print("========== Bienvenido al AutoShopping ==========")
    print("================================================")
    print("1.                  Mostrar autos disponibles.")
    print("2.                  Agregar nuevo auto.")
    print("3.                  Buscar autos por marca.")
    print("4.                  Actualizar datos de auto.")
    print("5.                  Eliminar auto.")
    print("0.                  Salir.")
    print("=" * 48)
    print(" ")
    print("=" * 48)
    print(" ")
    print_car()
    print("=" * 48)

def opcion_autos_1():
    print("Has elegido la Opción 1.")
    print("Estos son nuestros autos disponibles: ")
    with open("AutoShopping.json", "r") as file:
        autos = json.load(file)  
        print("{:<3} {:<1} {:<12} {:<1} {:<15} {:<1} {:<10} {:<1} {:<30} {:<1}".format(" ", "|", "MARCA", "|", "MODELO", "|", "PRECIO", "|", "EQUIPAMIENTO", "|"))
        counter = 1
    for x in autos["autostore"]["autos"]:
        equipment = ""
        if isinstance(x["equipamiento"], list):
            equipment = ', '.join(x["equipamiento"])
        else:
            equipment = x["equipamiento"]
        print("{:<3} {:<1} {:<12} {:<1} {:<15} {:<1} {:<10} {:<1} {:<30} {:<1}".format(str(counter), "|", x["marca"], "|", x["modelo"], "|", x["precio"], "|", equipment.title(), "|"))
        counter += 1
    input()

def opcion_autos_2():
    os.system("clear")
    print_car_v2()
    print("Has elegido la Opción 2")
    print("Por favor llena los datos correspondientes para agregar un nuevo auto.")
    
    marca = input("Digite la marca del auto: ")
    linea = input("Digite la línea del auto: ")
    modelo = input("Digite el modelo del auto: ")
    precio = input("Digite el precio del auto: ")
    equipamiento = input("Digite el equipamiento del auto (separado por comas si hay múltiples elementos): ").split(',')
    
    nuevo_auto = {
        "marca": marca,
        "linea": linea,
        "modelo": modelo,
        "precio": precio,
        "equipamiento": equipamiento
    }
    
    with open("AutoShopping.json", "r+") as file:
        data = json.load(file)
        data["autostore"]["autos"].append(nuevo_auto)
        file.seek(0)
        json.dump(data, file, indent=4)
    
    print("Auto agregado con éxito.")
    input()

def opcion_autos_3():
    os.system("clear")
    print_car_v2()
    print("Has elegido la Opción 3")
    marca_elegida = input("Escribe la marca del auto para mostrar: ")
    with open("AutoShopping.json", "r") as file:
        autos = json.load(file)
        print("{:<3} {:<1} {:<12} {:<1} {:<15} {:<1} {:<10} {:<1} {:<30} {:<1}".format(" ", "|", "MARCA", "|", "MODELO", "|", "PRECIO", "|", "EQUIPAMIENTO", "|"))
        counter = 1
        for x in autos["autostore"]["autos"]:
            if x["marca"] == marca_elegida:
                equipment = ""
                if isinstance(x["equipamiento"], list):
                    equipment = ', '.join(x["equipamiento"])
                else:
                    equipment = x["equipamiento"]
                print("{:<3} {:<1} {:<12} {:<1} {:<15} {:<1} {:<10} {:<1} {:<30} {:<1}".format(str(counter), "|", x["marca"], "|", x["modelo"], "|", x["precio"], "|", equipment.title(), "|"))
                counter += 1
        input()

def opcion_autos_4():
    os.system("clear")
    print_car_v2()
    print("Has elegido la Opción 4")
    with open("AutoShopping.json", "r+") as file:
        data = json.load(file)
        print("Estos son nuestros autos disponibles: ")
        for idx, auto in enumerate(data["autostore"]["autos"]):
            print(f"{idx + 1}: {auto['marca']} - {auto['modelo']}")
        indice = int(input("Elije el índice del auto a actualizar: ")) - 1
        if 0 <= indice < len(data["autostore"]["autos"]):
            auto_actualizado = data["autostore"]["autos"][indice]
            print(f"Actualizando datos para {auto_actualizado['marca']} - {auto_actualizado['modelo']}")
            
            marca = input("Digite la marca del auto actualizado: ")
            linea = input("Digite la línea del auto actualizado: ")
            modelo = input("Digite el modelo del auto actualizado: ")
            precio = input("Digite el precio del auto actualizado: ")
            equipamiento = input("Digite el equipamiento actualizado (separado por comas si hay múltiples elementos): ").split(',')
            
            auto_actualizado["marca"] = marca
            auto_actualizado["linea"] = linea
            auto_actualizado["modelo"] = modelo
            auto_actualizado["precio"] = precio
            auto_actualizado["equipamiento"] = equipamiento
            
            data["autostore"]["autos"][indice] = auto_actualizado
            
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            
            print("Auto actualizado con éxito.")
            print_car_v2()
            input("")
        else:
            print("Índice inválido.")
            print_car_v2()
        input()

def opcion_autos_5():
    os.system("clear")
    print_car_v2()
    print("Has elegido la Opción 5")
    with open("AutoShopping.json", "r+") as file:
        data = json.load(file)
        print("Estos son nuestros autos disponibles: ")
        for idx, auto in enumerate(data["autostore"]["autos"]):
            print(f"{idx + 1}: {auto['marca']} - {auto['modelo']}")
        indice = int(input("Elije el índice del auto a eliminar: ")) - 1
        if 0 <= indice < len(data["autostore"]["autos"]):
            auto_eliminado = data["autostore"]["autos"].pop(indice)
            print(f"Eliminando {auto_eliminado['marca']} - {auto_eliminado['modelo']}")
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            print("Auto eliminado con éxito.")
            print_car()
        else:
            print("Índice inválido.")
            print_car_v2()
        input()

while True:
    menu_autos()
    opcion = input("Elige una opción (1-5): ")

    if opcion == '1':
        opcion_autos_1()
    elif opcion == '2':
        opcion_autos_2()
    elif opcion == '3':
        opcion_autos_3()
    elif opcion == '4':
        opcion_autos_4()
    elif opcion == '5':
        opcion_autos_5()
    elif opcion == '0':
        print("¡Hasta luego!")
        print_car_v2()
        break
    else:
        print("Opción inválida. Por favor, digite una opción válida.")
        print_car_v2()
        input()
        
