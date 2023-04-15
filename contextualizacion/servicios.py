# crear un programa utilizando arreglos
# unidimensionales sobre el siguiente enunciado:
# a. En un censo familiar se desea colocar subsidios a los servicios públicos, se debe
# crear un programa que pregunte la cantidad de familias y que ingresen el valor del
# agua, luz y gas.
# b. En caso de que, el estrato 1 debe dar el 20% de descuento a cada servicio, si es
# estrato 2 el 15% si es de estrato 3 o más debe dar el 9% de descuento, al final
# nos debe dar el total a pagar discriminado por servicio públic

num_familias = int(input("Ingrese la cantidad de familias: "))
valores = []

# Solicitar los valores de agua, luz y gas para cada familia y almacenarlos en el arreglo valores
for i in range(num_familias):
    print(f"\nFamilia {i+1}:")
    estrato = int(input("Ingrese el estrato:"))
    agua = float(input("Ingrese el valor del agua: "))
    luz = float(input("Ingrese el valor de la luz: "))
    gas = float(input("Ingrese el valor del gas: "))

    # Calcular el descuento dependiendo del estrato
    if estrato == 1:
        descuento = 0.2
    elif estrato == 2:
        descuento = 0.15
    else:
        descuento = 0.09

    # Calcular los valores con descuento y almacenarlos en el arreglo valores
    agua_desc = agua - (agua * descuento)
    luz_desc = luz - (luz * descuento)
    gas_desc = gas - (gas * descuento)
    valores.append([agua_desc, luz_desc, gas_desc])

# Calcular el total a pagar discriminado por servicio público para cada familia
for i in range(num_familias):
    total_familia = 0
    total_familia += valores[i][0] + valores[i][1] + valores[i][2]
    print(f"\nTotal a pagar por servicios públicos para la familia {i+1}: {total_familia:.2f}")
    print(f"Total a pagar por agua: {valores[i][0]:.2f}")
    print(f"Total a pagar por luz: {valores[i][1]:.2f}")
    print(f"Total a pagar por gas: {valores[i][2]:.2f}")
2


