inventario = []

import json

def guardar_inventario(inventario):
    with open("inventario.json", "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)

def cargar_inventario():
    try:
        with open("inventario.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    
