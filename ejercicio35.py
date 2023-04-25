#Confeccionar un programa que lea n pares de datos, corresponde a medida de base y de altura de un triangulo. El programa debe: a)De cada triangulo la medida de base, altura y superficie. b)la caqntidad de triangulos cuya superficie es mayora a 12. Realizar todas las comprobaciones necesarias para no permitir el ingreso de datos invalidos.
import math

n = int(input("Ingrese la cantidad de pares de datos que desea ingresar: "))
count = 0

for i in range(n):
    while True:
        try:
            base = float(input("Ingrese la medida de la base del triángulo {}: ".format(i+1)))
            altura = float(input("Ingrese la medida de la altura del triángulo {}: ".format(i+1)))
            if base <= 0 or altura <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Ingrese un número positivo para la base y altura del triángulo.")
    
    superficie = (base * altura) / 2
    print("El triángulo {} tiene una base de {} y una altura de {}. Su superficie es de {}.".format(i+1, base, altura, superficie))
    
    if superficie > 12:
        count += 1
        
print("La cantidad de triángulos cuya superficie es mayor a 12 es: {}.".format(count))
