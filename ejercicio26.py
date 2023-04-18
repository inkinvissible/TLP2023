#Realizar un programa que permita la carga de 2 listas de 15 valores c/u. Informe con un mensaje cual de las dos listas tiene un valor acumulado mayor. (se necesitan dos estructuras repetitivas)
# Inicializar las listas
lista1 = []
lista2 = []

# Solicitar los valores de la primera lista
contador = 0
while contador < 15:
    valor = int(input("Ingrese un valor para la primera lista: "))
    lista1.append(valor)
    contador += 1

# Solicitar los valores de la segunda lista
contador = 0
while contador < 15:
    valor = int(input("Ingrese un valor para la segunda lista: "))
    lista2.append(valor)
    contador += 1

# Calcular la suma de cada lista
suma1 = sum(lista1)
suma2 = sum(lista2)

# Mostrar el resultado
if suma1 > suma2:
    print("La lista 1 tiene un valor acumulado mayor.")
elif suma1 < suma2:
    print("La lista 2 tiene un valor acumulado mayor.")
else:
    print("Ambas listas tienen el mismo valor acumulado.")
