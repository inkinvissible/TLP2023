#67
# Cargar lista con 5 enteros
lista_enteros = []

for i in range(5):
    valor = int(input("Ingrese un entero: "))
    lista_enteros.append(valor)

# Encontrar el entero más pequeño y su posición
valor_menor = min(lista_enteros)
posicion_menor = lista_enteros.index(valor_menor)

# Mostrar el entero más pequeño y su posición
print("El entero más pequeño es:", valor_menor)
print("Se encuentra en la posición:", posicion_menor)


