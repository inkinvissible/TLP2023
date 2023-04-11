#Ejercicio 12. 11 de abril. Hacer un programa que ingrese el sueldo y la antiguedad de un empleado. si el soeldo es menor a 500 y la antiguedad es igual o superior a 10 años, otorgarle un aumento del 20%. Si el sueldo es inferior a 500 pero su atiguedad es menor a 10 años, otorgarle un aumento del 5%. Si el sueldo es mayor o igual a 50, no hay cambios.
# Pedir al usuario que ingrese el sueldo y la antigüedad
sueldo = float(input("Ingrese el sueldo del empleado: "))
antiguedad = int(input("Ingrese la antigüedad del empleado (en años): "))

# Calcular el aumento correspondiente
if sueldo < 500 and antiguedad >= 10:
    aumento = sueldo * 0.2
    nuevo_sueldo = sueldo + aumento
    print("El nuevo sueldo del empleado es:", nuevo_sueldo)
elif sueldo < 500 and antiguedad < 10:
    aumento = sueldo * 0.05
    nuevo_sueldo = sueldo + aumento
    print("El nuevo sueldo del empleado es:", nuevo_sueldo)
else:
    print("El sueldo del empleado no cambia")
