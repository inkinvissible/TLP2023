# Una empresa tiene 2 turnos mañana y tarde en la que trabajan 8 empleados 4 de la mañana y 4 de la tarde. Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en 2 listas. Imprimir las listas 2 de sueldo
# Inicializar las listas de sueldos para la mañana y la tarde
sueldos_manana = []
sueldos_tarde = []

# Cargar los sueldos de los empleados de la mañana
print("Ingresar los sueldos de los empleados de la mañana:")
for i in range(4):
    sueldo = float(input("Ingrese el sueldo del empleado {}: ".format(i+1)))
    sueldos_manana.append(sueldo)

# Cargar los sueldos de los empleados de la tarde
print("\nIngresar los sueldos de los empleados de la tarde:")
for i in range(4):
    sueldo = float(input("Ingrese el sueldo del empleado {}: ".format(i+1)))
    sueldos_tarde.append(sueldo)

# Imprimir las listas de sueldos
print("\nLista de sueldos de los empleados de la mañana:")
print(sueldos_manana)

print("\nLista de sueldos de los empleados de la tarde:")
print(sueldos_tarde)
