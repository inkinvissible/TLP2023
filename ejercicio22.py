#Hacer un programa que ingrese 10 notas y nos informe cuantos tienen notas mayor a 7 y cuantas menores a 7. Realizar todas las comprobaciones. Usar while
# Solicitar las 10 notas
notas = []
for i in range(10):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

# Contar la cantidad de notas mayores o menores a 7
notas_mayores_7 = 0
notas_menores_7 = 0
for nota in notas:
    if nota > 7:
        notas_mayores_7 += 1
    elif nota < 7:
        notas_menores_7 += 1

# Mostrar el resultado
print(f"De las 10 notas ingresadas, {notas_mayores_7} son mayores a 7 y {notas_menores_7} son menores a 7.")

# notas = []
# contador = 0
# while contador < 10:
#     nota = float(input(f"Ingrese la nota {contador+1}: "))
#     notas.append(nota)
#     contador += 1

# notas_mayores_7 = 0
# notas_menores_7 = 0
# contador = 0
# while contador < len(notas):
#     if notas[contador] > 7:
#         notas_mayores_7 += 1
#     elif notas[contador] < 7:
#         notas_menores_7 += 1
#     contador += 1

# print(f"De las 10 notas ingresadas, {notas_mayores_7} son mayores a 7 y {notas_menores_7} son menores a 7.")
