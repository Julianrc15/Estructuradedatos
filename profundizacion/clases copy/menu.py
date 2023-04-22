from profundizacion.biblioteca import *

def menu():
    print("\nMenú de opciones:")
    print("1. Registrar nuevo libro")
    print("2. Actualizar libro")
    print("3. Eliminar libro")
    print("4. Buscar libro")
    print("5. Ordenar libros")
    print("0. Salir")

    opcion = input("\nIngrese una opción: ")

    return opcion

biblioteca = Biblioteca()

while True:
    opcion = menu()

    if opcion == "1":
        codigo = input("Ingrese el código del libro: ")
        nombre = input("Ingrese el nombre del libro: ")
        autor = input("Ingrese el autor del libro: ")
        materia = input("Ingrese la materia del libro: ")
        num_paginas = int(input("Ingrese el número de páginas del libro: "))

        biblioteca.registrar_libro(codigo, nombre, autor, materia, num_paginas)

    elif opcion == "2":
        codigo = input("Ingrese el código del libro a actualizar: ")
        nombre = input("Ingrese el nuevo nombre del libro: ")
        autor = input("Ingrese el nuevo autor del libro: ")
        materia = input("Ingrese la nueva materia del libro: ")
        num_paginas = int(input("Ingrese el nuevo número de páginas del libro: "))

        biblioteca.actualizar_libro(codigo, nombre, autor, materia, num_paginas)

    elif opcion == "3":
        codigo = input("Ingrese el código del libro a eliminar: ")

        biblioteca.eliminar_libro(codigo)

    elif opcion == "4":
        codigo = input("Ingrese el código del libro a buscar: ")

        libro = biblioteca.buscar_libro_secuencial(codigo)
        if libro is None:
            print("Libro no encontrado.")
        else:
            print(f"Código: {libro[0]}, Nombre: {libro[1]}, Autor: {libro[2]}, Materia: {libro[3]}, Páginas: {libro[4]}")

    elif opcion == "5":
        print("\nMétodos de ordenamiento:")
        print("1. Por autor")
        print("2. Por código con el método burbuja")
        print("0. Volver al menú principal")

        opcion_ordenamiento = input("\nIngrese una opción: ")

        if opcion_ordenamiento == "1":
            biblioteca.ordenar_por_autor()
        elif opcion_ordenamiento == "2":
            biblioteca.ordenar_por_codigo_burbuja()

    elif opcion == "0":
        break

    else:
        print("Opción inválida. Intente de nuevo.")

