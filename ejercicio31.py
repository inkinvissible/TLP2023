#Realiza un programa que permita la carga de 10 valores y nos muestre la seuma de los valores y su promedio
# Pedir al usuario que ingrese 10 valores
numeros = []
for i in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

# Calcular la suma de los valores
suma = sum(numeros)

# Calcular el promedio de los valores
promedio = suma / len(numeros)

# Mostrar la suma y el promedio
print("La suma de los valores es:", suma)
print("El promedio de los valores es:", promedio)
