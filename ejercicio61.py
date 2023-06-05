# Definir una lista vacia u luego la carga de 5 enteros por teckado y añadir a la lsita. Imprimir la lista generada.
# Definir una lista vacía
lista = []

# Cargar la lista con 5 enteros ingresados por teclado
for i in range(5):
    entero = int(input("Ingrese un número entero: "))
    lista.append(entero)

# Imprimir la lista generada
print("La lista generada es:", lista)
