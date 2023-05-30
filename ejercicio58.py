#Definir por asignacion una lista con 8 enteros. Contar cuantos de dichos valores son mayores a 100
# Definir la lista de enteros
lista_enteros = [85, 120, 95, 150, 110, 75, 200, 90]

# Contar cuántos valores son mayores a 100
contador = 0
for valor in lista_enteros:
    if valor > 100:
        contador += 1

# Mostrar el resultado
print("La cantidad de valores mayores a 100 es:", contador)
