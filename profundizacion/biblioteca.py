class Biblioteca:
    def __init__(self):
        self.arreglo = [ ["L001", "El nombre del viento", "Patrick Rothfuss", "Fantasía", 662],
            ["L002", "Los pilares de la tierra", "Ken Follett", "Histórica", 1076],
            ["L003", "Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 471],
            ["L004", "El señor de los anillos", "J.R.R. Tolkien", "Fantasía", 1216],
            ["L005", "1984", "George Orwell", "Ciencia ficción", 328],
            ["L006", "Crónica de una muerte anunciada", "Gabriel García Márquez", "Realismo mágico", 120],
            ["L007", "La isla del tesoro", "Robert Louis Stevenson", "Aventuras", 304],
            ["L008", "Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 1088],
            ["L009", "El retrato de Dorian Gray", "Oscar Wilde", "Drama", 284],
            ["L010", "Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", 223],
            ["L011", "La sombra del viento", "Carlos Ruiz Zafón", "Misterio", 553],
            ["L012", "La ladrona de libros", "Markus Zusak", "Drama", 480],
            ["L013", "El código Da Vinci", "Dan Brown", "Misterio", 595],
            ["L014", "Fahrenheit 451", "Ray Bradbury", "Ciencia ficción", 192],
            ["L015", "Las aventuras de Tom Sawyer", "Mark Twain", "Aventuras", 224]]

    def registrar_libro(self, codigo, nombre, autor, materia, num_paginas):
        self.arreglo.append([codigo, nombre, autor, materia, num_paginas])
        print("Libro registrado exitosamente.")

    
    def actualizar_libro(self, codigo, nombre, autor, materia, num_paginas):
        for libro in self.arreglo:
            if libro[0] == codigo:
                libro[1] = nombre
                libro[2] = autor
                libro[3] = materia
                libro[4] = num_paginas
                print("Libro actualizado exitosamente.")
                return
        print("Libro no encontrado.")

    def eliminar_libro(self, codigo):
        for libro in self.arreglo:
            if libro[0] == codigo:
                self.arreglo.remove(libro)
                print("Libro eliminado exitosamente.")
                return
        print("Libro no encontrado.")

    def buscar_libro_secuencial(self, codigo):
        for libro in self.arreglo:
            if libro[0] == codigo:
                return libro
        return None

    def buscar_libro_binario(self, codigo):
        arreglo_ordenado = sorted(self.arreglo, key=lambda libro: libro[0])
        inicio = 0
        fin = len(arreglo_ordenado) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2

            if arreglo_ordenado[medio][0] == codigo:
                return arreglo_ordenado[medio]
            elif arreglo_ordenado[medio][0] < codigo:
                inicio = medio + 1
            else:
                fin = medio - 1

        return None

    def ordenar_por_autor(self):
        self.arreglo.sort(key=lambda libro: libro[2])
        a=self.arreglo.sort(key=lambda libro: libro[2])
        print(f"Libros ordenados por autor.\n ")
        print(a)

    def ordenar_por_codigo_burbuja(self):
        n = len(self.arreglo)

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.arreglo[j][0] > self.arreglo[j + 1][0]:
                    self.arreglo[j], self.arreglo[j + 1] = self.arreglo[j + 1], self.arreglo[j]

        print("Libros ordenados por código con el método burbuja.")
