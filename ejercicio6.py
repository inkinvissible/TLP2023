#Ejercicio 6. Ingrese cuatro numeros y que me indique cual es el mayor de ellos
# Pedimos al usuario que ingrese cuatro números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
numero4 = float(input("Ingrese el cuarto número: "))

# Comparamos los cuatro números para encontrar el mayor
if numero1 >= numero2 and numero1 >= numero3 and numero1 >= numero4:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3 and numero2 >= numero4:
    mayor = numero2
elif numero3 >= numero1 and numero3 >= numero2 and numero3 >= numero4:
    mayor = numero3
else:
    mayor = numero4

# Mostramos el resultado en pantalla
print("El número mayor es:", mayor)
