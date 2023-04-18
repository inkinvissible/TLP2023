#Programa que permita la carga de 10 numeros y nos muestre la suma de los valores y su promedio. Usa while
numeros = []
for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

print("Los números ingresados son:")
for numero in numeros:
    print(numero)

# Calcular la suma de los valores
suma = sum(numeros)

# Calcular el promedio de los valores
promedio = suma / len(numeros)

print(f"La suma de los valores es: {suma}")
print(f"El promedio de los valores es: {promedio}")

# numeros = []
# contador = 0

# while contador < 10:
#     numero = int(input(f"Ingrese el número {contador+1}: "))
#     numeros.append(numero)
#     contador += 1

# print("Los números ingresados son:")
# for numero in numeros:
#     print(numero)

# # Calcular la suma de los valores
# suma = sum(numeros)

# # Calcular el promedio de los valores
# promedio = suma / len(numeros)

# print(f"La suma de los valores es: {suma}")
# print(f"El promedio de los valores es: {promedio}")
