inventario = []

import json

# DUMPS() = crear datos JSON a partir de un diccionario de datos
# DUMP() = almacenar datos de un diccionario en un archivo JSON


# CONVETIR DATOS DE INVENTARIO A JSON:

def guardar_inventario(inventario):
    with open("inventario.json", "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)

# def cargar_inventario():
#     try:
#         with open("inventario.json", "r", encoding="utf-8") as archivo:
#             return json.load(archivo)
#     except FileNotFoundError:
#         return []
    
# PRUEBAS CON JSON
# De cadena JSON a diccionario de datos
# json_string = '{"nombre": "Ulises", "edad": "26", "activo": true}'
# datos_pyhton = json.loads(json_string)

# print(datos_pyhton["nombre"], "de edad: ", datos_pyhton['edad'])

# # De diccionario de datos a cadena JSON
# datos_pyhton2 = {"nombre": "Ulises", "edad": 26, "activo": True}
# json_string2 = json.dumps(datos_pyhton2, indent=4)

# print(json_string2)

# # Guardar diccionario de python en un archivo formato JSON
# with open("datos.json", "w") as archivo:
#     json.dump(datos_pyhton2, archivo, indent=4)

# # Lectura de un archivo JSON
# with open("datos.json", "r") as archivo:
#     datos = json.load(archivo)

# print(datos)
