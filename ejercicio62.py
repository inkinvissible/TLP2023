#Realizar la carga de valores enteros por teclado, almacenados em una lista. Finalizar la carga al ingresar el 0. Mostrar el tamaño de la lista.
# Definir una lista vacía
lista = []

# Cargar valores enteros por teclado hasta ingresar 0
while True:
    valor = int(input("Ingrese un número entero (ingrese 0 para finalizar): "))
    if valor == 0:
        break
    lista.append(valor)

# Mostrar el tamaño de la lista
tamaño = len(lista)
print("El tamaño de la lista es:", tamaño)
