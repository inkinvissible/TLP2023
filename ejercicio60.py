#definir una lista que almacene por asignacion los nombres de 5 personas. Contar cuantas de esas nombres tienen mas de 5 caracteres.
# Definir la lista por asignación
nombres = ['Ana', 'Carlos', 'Lucía', 'Pedro', 'Sofía']

# Contar cuántos nombres tienen más de 5 caracteres
contador = 0
for nombre in nombres:
    if len(nombre) > 5:
        contador += 1

# Mostrar el resultado
print("Cantidad de nombres con más de 5 caracteres:", contador)
