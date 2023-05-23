# ingresar una oracion que puede tener mayusculas o minuscùlas. contar la cantidad de vocales. Convertit en mayusculas toda la oracion.
oracion = input("Ingresa una oración: ")
oracion_mayusculas = oracion.upper()

cantidad_vocales = 0
vocales = "AEIOUÁÉÍÓÚ"
for letra in oracion:
    if letra.upper() in vocales:
        cantidad_vocales += 1

print("Cantidad de vocales:", cantidad_vocales)
print("Oración en mayúsculas:", oracion_mayusculas)
