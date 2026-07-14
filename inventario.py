from datos import guardar_inventario

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

    guardar_inventario(inventario)



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

def editar_impresora(inventario):
    print("\n ---- Editar impresora ----")
    id_busqueda = input("Impresora: ")

    for impresora in inventario:
        if impresora["id"] == id_busqueda:
            print("\n ---- Impresora ", impresora["id"],"seleccionada ----")
            nuevo_modelo = input("Modelo: ")
            nuevo_serie = input("Serie: ")
            nuevo_ip = input("IP: ")
            nuevo_area = input("Área: ")
            nuevo_estado = input("Estado: ")
            nuevo_contador = input("Contador: ")
            nuevo_fecha = input("Fecha de instalación: ")

            if nuevo_modelo:
                impresora["modelo"] = nuevo_modelo

            if nuevo_serie:
                impresora["serie"] = nuevo_serie
            
            if nuevo_ip:
                impresora["ip"] = nuevo_ip
            
            if nuevo_area:
                impresora["area"] = nuevo_area
            
            if nuevo_contador:
                impresora["contador"] = nuevo_contador

            if nuevo_estado:
                impresora["estado"] = nuevo_estado
            
            if nuevo_fecha:
                impresora["fecha_instalacion"] = nuevo_fecha
              
            print("\nImpresora editada")
            input("\nPresiona enter para regresar al menu")
            return
        # else:
    print("ID no econtrado")
    input("\nPresiona enter para regresar al menu")

def eliminar_impresora(inventario):
    print("\n ----Eliminar impresora----")
    imp_eliminar =  input("Impresora a eliminar: ")

    for impresora in inventario:
        if impresora["id"] == imp_eliminar:
            inventario.remove(impresora)
            print("Impresora ha sido eliminada correctamente")
            input("\nPresiona enter para regresar al menu")
            return
    print("\n ¡¡ ID no identificado !!")
    input("\nPresiona enter para regresar al menu")

def buscar_impresora(inventario):
    print("\n ---- Buscar Impresora ----")
    id_busqueda = input("Ingresa el ID de la impresora: ")
    for impresora in inventario:
        if impresora["id"] == id_busqueda:
            print("\n --- Impresora encontrada ---")
            print("id:", impresora["id"])
            print("Modelo:", impresora["modelo"])
            print("Serie:", impresora["serie"])
            print("IP asignada:", impresora["ip"])
            print("Área de ubicación:", impresora["area"])
            print("Estado actual:", impresora["estado"])
            print("Contador actual:", impresora["contador"])
            print("Fecha de instalación:", impresora["fecha_instalacion"])
            input("\nPresiona enter para regresar al menu")
            return
    print("\nID no encontrado")
    input("\nPresiona enter para regresar al menu")

