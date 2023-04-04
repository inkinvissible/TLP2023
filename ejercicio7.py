#Ejercicio 7. Ingresar cuatro numeros calcule la resta del 1ero con el 2do
# Pedir al usuario que ingrese los cuatro números
while True:
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        numero3 = float(input("Ingrese el tercer número: "))
        numero4 = float(input("Ingrese el cuarto número: "))
        break
    except ValueError:
        print("Debe ingresar un número válido. Intente nuevamente.")

# Realizar la resta del primer número con el segundo y la multiplicación del tercer número con el cuarto
resta = numero1 - numero2
multiplicacion = numero3 * numero4

# Mostrar los resultados de las operaciones en pantalla
print("La resta del primer número con el segundo es:", resta)
print("La multiplicación del tercer número con el cuarto es:", multiplicacion)
