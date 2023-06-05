#Almacenar en una lista los sueldos (float) de 5 operarios. Imprimir lista y promedio de sueldos.
# Definir una lista vacía
sueldos = []

# Cargar los sueldos de los 5 operarios
for i in range(5):
    sueldo = float(input("Ingrese el sueldo del operario: "))
    sueldos.append(sueldo)

# Imprimir la lista de sueldos
print("La lista de sueldos es:", sueldos)

# Calcular el promedio de los sueldos
promedio = sum(sueldos) / len(sueldos)
print("El promedio de los sueldos es:", promedio)
