# interfaz gráfica
from menu import iniciar_menu
from inventario import registrar_impresora
from inventario import mostrar_inventario
from inventario import editar_impresora
from inventario import eliminar_impresora
from inventario import buscar_impresora
from datos import inventario
from datos import cargar_inventario

inventario = cargar_inventario()

while True:
    iniciar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_impresora(inventario)
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
        editar_impresora(inventario)
    elif opcion == "4":
        eliminar_impresora(inventario)
    elif opcion == "5":
        buscar_impresora(inventario)
    elif opcion == "6":
        print("\n Hasta Luego")
        print("\n ")
        break
    else:
        print("\n ERROR: Opción inválida")
        print("\n ")
        break