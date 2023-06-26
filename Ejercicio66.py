#Crear y cargar una lista con 5 enteros. Implementar un programa que identifique el mayor valor de la lista
# Crear una lista vacía
numeros = []

# Cargar la lista con 5 enteros
print("Ingrese 5 números enteros:")
for i in range(5):
    numero = int(input("Número {}: ".format(i+1)))
    numeros.append(numero)

# Inicializar la variable para el mayor valor
mayor = numeros[0]

# Iterar sobre la lista y encontrar el mayor valor
for numero in numeros:
    if numero > mayor:
        mayor = numero

# Imprimir el mayor valor
print("El mayor valor de la lista es:", mayor)
