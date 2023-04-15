

##creacion clase  pila y metodos relacionados
class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.elementos = [None] * capacidad
        self.tope = 0

    def buscar_elemento(self, posicion):
        if posicion < 0 or posicion >= self.tope:
            raise ValueError("Posición fuera de rango")
        return self.elementos[posicion]

    def insertar_elemento(self, elemento):
        if self.tope == self.capacidad:
            raise ValueError("Pila llena")
        self.elementos[self.tope] = elemento
        self.tope += 1

    def actualizar_elemento(self, posicion, elemento):
        if posicion < 0 or posicion >= self.tope:
            raise ValueError("Posición fuera de rango")
        self.elementos[posicion] = elemento

    def eliminar_elemento(self):
        if self.tope == 0:
            raise ValueError("Pila vacía")
        self.tope -= 1
        elemento_eliminado = self.elementos[self.tope]
        self.elementos[self.tope] = None
        return elemento_eliminado

##utilizar metodos de la clase pila
# Creamos una pila de capacidad 5
mi_pila = Pila(5)

# Insertamos algunos elementos en la pila
mi_pila.insertar_elemento('1')
mi_pila.insertar_elemento('2')
mi_pila.insertar_elemento('3')
mi_pila.insertar_elemento('4')
mi_pila.insertar_elemento('5')

print(f'Pila ingresada inicialmente:\n')
for i in range(mi_pila.tope):
    print(f' {mi_pila.buscar_elemento(i)}')

# Buscamos el elemento en la posición 2
print(f'Buscar elemento: {mi_pila.buscar_elemento(2)}\n') # Imprime '3'

# Actualizamos el elemento en la posición 1
mi_pila.actualizar_elemento(1, 'E')

# Eliminamos el elemento en la parte superior de la pila
print(f'Eliminar elemento: {mi_pila.eliminar_elemento()}\n') # Imprime 'D'

# Insertamos otro elemento en la pila
mi_pila.insertar_elemento('F')

# Imprimimos los elementos restantes de la pila
print(f'Elementos de la pila:')
for i in range(mi_pila.tope):
    print(f' {mi_pila.buscar_elemento(i)}')
# Imprime 'A', 'E', 'C', 'F'
