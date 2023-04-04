#Ejercicio 8. Ingrese dos numeros y que indique cual es el mayor y el menor. Si num1 es mayor que haga la suma y la resta de los numeros. Si num2 es mayor que haga producto y division.
# Pedimos al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Comprobamos si los números son iguales
if num1 == num2:
    print("Los números son iguales")
else:
    # Comprobamos cuál es el número mayor
    if num1 > num2:
        mayor = num1
        menor = num2
        # Realizamos la suma y la resta
        suma = num1 + num2
        resta = num1 - num2
    else:
        mayor = num2
        menor = num1
        # Realizamos el producto y la división
        producto = num1 * num2
        if num2 == 0:
            print("No es posible dividir por 0")
        else:
            division = num1 / num2
    
    # Mostramos los resultados si no hay errores
    if mayor is not None and menor is not None:
        print("El número mayor es:", mayor)
        print("El número menor es:", menor)
        if suma is not None and resta is not None:
            print("La suma es:", suma)
            print("La resta es:", resta)
        elif producto is not None and division is not None:
            print("El producto es:", producto)
            print("La división es:", division)
