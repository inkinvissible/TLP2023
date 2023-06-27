#68
# Cargar nombres de personas en una lista
lista_nombres = []

for i in range(5):
    nombre = input("Ingrese el nombre de una persona: ")
    lista_nombres.append(nombre)

# Encontrar el nombre más pequeño en orden alfabético
nombre_menor = min(lista_nombres)

# Mostrar el nombre más pequeño
print("El nombre más pequeño en orden alfabético es:", nombre_menor)
