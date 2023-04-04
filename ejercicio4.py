# Ejercicio 4, Ingrese dos números y calcule suma, resta, multiplicacion y division y mostrar en pantalla
# Pedimos al usuario que ingrese dos números
numero1 = input("Ingrese el primer número: ")
if not numero1.isdigit():
    print("Error: El valor ingresado no es un número.")
    exit()
numero1 = float(numero1)

numero2 = input("Ingrese el segundo número: ")
if not numero2.isdigit():
    print("Error: El valor ingresado no es un número.")
    exit()
numero2 = float(numero2)

#Verifica si es 0
if numero1 == 0 or numero2 == 0:
    print("No es posible dividir por 0")
    resultado = None
else:
    # Pedimos al usuario que ingrese la operación que desea realizar
    operacion = input("Ingrese la operación que desea realizar (+, -, *, /): ")

    # Verificamos la operación que desea realizar el usuario
    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        if numero1 == 0 or numero2 == 0:
            print("No es posible dividir por 0")
        else:
            resultado = numero1 / numero2
    else:
        # Si el usuario ingresa una operación incorrecta, mostramos un mensaje de error
        print("Operación incorrecta")
        resultado = None

# Mostramos el resultado en pantalla si no hay errores
if resultado is not None:
    print("El resultado de la operación es:", resultado)
