#Ejercicio 5. Ingresar el sueldo de una persona si  supera los 3000 dolares tendra que abonar impuestos.

# Pedimos al usuario que ingrese el sueldo
sueldo = input("Ingrese su sueldo en dólares: ")

# Comprobamos que el valor ingresado sea un número positivo
if not sueldo.isdigit() or float(sueldo) < 0:
    print("Error: El valor ingresado debe ser un número positivo.")
    exit()
else:
    sueldo = float(sueldo)
    # Comprobamos si se deben abonar impuestos o no
    if sueldo > 3000:
        impuestos = sueldo * 0.15
        sueldo_neto = sueldo - impuestos
        print("Sueldo bruto:", sueldo)
        print("Impuestos:", impuestos)
        print("Sueldo neto:", sueldo_neto)
    else:
        print("Sueldo:", sueldo)

