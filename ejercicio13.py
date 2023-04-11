#Ejercicio 12. 11 de abril. Hacer un programa que ingrese 3 números y me de el mayor y el menor de ellos
# Pedir al usuario que ingrese los 3 números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Encontrar el número mayor y menor utilizando la función max() y min()
mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

# Imprimir el resultado
print("El mayor número es:", mayor)
print("El menor número es:", menor)
