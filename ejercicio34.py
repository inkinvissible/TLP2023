#Escribe un programa que lea n numeros enteros y calcule la cantidad de valores mayores o iguales a 1000 
n = int(input("Ingrese la cantidad de números: "))
numeros = []

for i in range(n):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

contador = 0

for numero in numeros:
    if numero >= 1000:
        contador += 1

print("La cantidad de valores mayores o iguales a 1000 es:", contador)
