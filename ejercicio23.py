#En una empresa trabajan empleados cuyo sueldo oscila entre los 100 y los 500 dolares, realizar el programa que lea los sueldos que cobra cada uno e informe cuantos empleados cobran entre 100 y 300 dolares y cuantos mayor a 300 dolares. Además debe informar el total de sueldos que gasta la empresa.
# Inicializar los contadores
empleados_entre_100_y_300 = 0
empleados_mas_de_300 = 0
total_sueldos = 0

# Solicitar los sueldos de los empleados hasta que se ingrese un sueldo negativo
sueldo = float(input("Ingrese el sueldo del empleado (ingrese un número negativo para finalizar): "))
while sueldo >= 0:
    total_sueldos += sueldo
    if sueldo >= 100 and sueldo <= 300:
        empleados_entre_100_y_300 += 1
    elif sueldo > 300 and sueldo <= 500:
        empleados_mas_de_300 += 1
    sueldo = float(input("Ingrese el sueldo del empleado (ingrese un número negativo para finalizar): "))

# Mostrar los resultados
print(f"La empresa tiene {empleados_entre_100_y_300} empleados que cobran entre 100 y 300 dólares, y {empleados_mas_de_300} empleados que cobran más de 300 dólares.")
print(f"El total de sueldos que gasta la empresa es de {total_sueldos} dólares.")
