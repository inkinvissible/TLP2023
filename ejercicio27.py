#Hacer un programa que permita la carga de x numeros enteros y luego informe la cantidad de pares i impares.
# Inicializar contadores
pares = 0
impares = 0

# Solicitar la cantidad de números a ingresar
cantidad_numeros = int(input("Ingrese la cantidad de números a ingresar: "))

# Solicitar los números
contador = 0
while contador < cantidad_numeros:
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1

# Mostrar el resultado
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
