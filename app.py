# interfaz gráfica
from menu import iniciar_menu
from inventario import registrar_impresora
from inventario import mostrar_inventario
from datos import inventario

while True:
    iniciar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_impresora(inventario)
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
        print("\n Hasta Luego")
        print("\n ")
        break
    else:
        print("\n ERROR: Opción inválida")
        print("\n ")
        break