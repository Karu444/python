import json
with open ("vendedores.txt", "r") as file:
    lineas = file.readlines()

lineas = lines[1:]
vendedores = []

for linea in lineas:
    datos = linea.strip().split(", ")
    apellido = datos[0]
    identificacion = datos[1]
    ventas = [int(venta) for venta in datos[2:]]

    vendedor = {
        "apellido" : apellido,
        "id" : identificacion,
        "ventas" : ventas
    }

    vendedores.append(vendedor)

data = {
    "vendedores" : vendedores
}

with open("vendedores.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("*** .EL ARCHIVO FUE CREADO EXITOSAMENTE. ***")