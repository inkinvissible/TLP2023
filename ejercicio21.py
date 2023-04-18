#Hacer un programa que ingrese la cantidad de piezas y su longitud y decir que son aptas solo las comprendidas entre 1.20 metros. Realizar las comprobaciones necesarias. Imprimir dicha cantidad. Usar while.
# Solicitar la cantidad de piezas
cantidad_piezas = int(input("Ingrese la cantidad de piezas: "))

# Solicitar la longitud de cada pieza y comprobar si es apta
piezas_aptas = 0
for i in range(cantidad_piezas):
    longitud = float(input(f"Ingrese la longitud de la pieza {i+1}: "))
    if longitud >= 1.20:
        piezas_aptas += 1

# Mostrar el resultado
print(f"De las {cantidad_piezas} piezas ingresadas, {piezas_aptas} son aptas para su uso.")

# cantidad_piezas = int(input("Ingrese la cantidad de piezas: "))

# piezas_aptas = 0
# contador = 0

# while contador < cantidad_piezas:
#     longitud = float(input(f"Ingrese la longitud de la pieza {contador+1}: "))
#     if longitud >= 1.20:
#         piezas_aptas += 1
#     contador += 1

# print(f"De las {cantidad_piezas} piezas ingresadas, {piezas_aptas} son aptas para su uso.")

