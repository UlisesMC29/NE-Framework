
def registrar_impresora(inventario):
    print("\n ---- Registrar impresora ----")

    id_impresora = input("Identificador: ")
    modelo = input("Modelo: ")
    no_serie = input("Serie: ")
    ip = input("IP Asignada: ")
    area = input("Área de ubicación: ")
    estado = input("Estado actual: ")
    contador = input("Contador actual: ")
    fecha_instalacion = input("Fecha de instalación: ")

    impresora = {
        "id": id_impresora,
        "modelo": modelo,
        "serie": no_serie,
        "ip": ip,
        "area": area,
        "estado": estado,
        "contador": contador,
        "fecha_instalacion": fecha_instalacion 
    }

    inventario.append(impresora)

    print("\nImpresora registrada")

    input("\nPresiona Enter para regresar al menú...")

def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("\n!!! No hay impresoras registradas")
    else:       
        print("\n ---- Inventario ----")
        for impresora in inventario:
            print("\n -- Impresora --" )
            print("id:", impresora["id"])
            print("Modelo:", impresora["modelo"])
            print("Serie:", impresora["serie"])
            print("IP asignada:", impresora["ip"])
            print("Área de ubicación:", impresora["area"])
            print("Estado actual:", impresora["estado"])
            print("Contador actual:", impresora["contador"])
            print("Fecha de instalación:", impresora["fecha_instalacion"])
           
    input("\nPresiona enter para regresar al menu")
