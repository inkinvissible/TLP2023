#Ejercicio 9. 11 de Abril. Hacer un programa que ingrese 3 numeros si todos son menores a 10, realizar la multiplicación de todos si son mayores hacer la suma de todos.
# Pedir los tres números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Verificar si todos los números son menores a 10
if num1 < 10 and num2 < 10 and num3 < 10:
    # Si todos son menores a 10, hacer la multiplicación
    resultado = num1 * num2 * num3
else:
    # Si alguno es mayor o igual a 10, hacer la suma
    resultado = num1 + num2 + num3

# Mostrar el resultado al usuario
print("El resultado es:", resultado)
