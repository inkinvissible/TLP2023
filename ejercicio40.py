#Realizar un programa que realice la carga de 10 valores enteros por teclado. Se desea conocer: a) Cantidad de valores igresados positivos, cantidad de valores ingresados negativos, la cantidad de multiplos de 15, el valor acumulados de los numeros ingresados que son pares.
# Inicializamos las variables para contar los valores ingresados
positivos = 0
negativos = 0
multiplos_15 = 0
acumulado_pares = 0

# Solicitamos al usuario que ingrese los valores
for i in range(10):
    valor = int(input("Ingrese un valor entero: "))
    
    # Contamos los valores positivos y negativos
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    
    # Contamos los múltiplos de 15
    if valor % 15 == 0:
        multiplos_15 += 1
    
    # Sumamos los valores pares
    if valor % 2 == 0:
        acumulado_pares += valor

# Mostramos los resultados
print("Cantidad de valores ingresados positivos:", positivos)
print("Cantidad de valores ingresados negativos:", negativos)
print("Cantidad de múltiplos de 15:", multiplos_15)
print("Acumulado de valores ingresados pares:", acumulado_pares)
