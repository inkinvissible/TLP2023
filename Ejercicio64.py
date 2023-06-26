#Cargar por teclado y almacenar en una lista las alturas de 5 personas. Obtener el promedio de las mismas, contar cuántas personas son más altas y más bajas
# Inicializar una lista vacía para almacenar las alturas
alturas = []

# Cargar las alturas de las 5 personas
for i in range(5):
    altura = float(input("Ingrese la altura de la persona {}: ".format(i+1)))
    alturas.append(altura)

# Calcular el promedio de las alturas
promedio = sum(alturas) / len(alturas)

# Contar cuántas personas son más altas y más bajas que el promedio
mas_altas = 0
mas_bajas = 0
for altura in alturas:
    if altura > promedio:
        mas_altas += 1
    elif altura < promedio:
        mas_bajas += 1

# Imprimir los resultados
print("El promedio de las alturas es: {:.2f}".format(promedio))
print("Personas más altas que el promedio: {}".format(mas_altas))
print("Personas más bajas que el promedio: {}".format(mas_bajas))
