# Realice unprograma que solicite la carga de 10 valores flotantes (con parte decimal) por teclado. mostrar al final su promedio y su suma total. con for y while
# suma = 0
# for i in range(10):
#     valor = float(input(f"Ingrese el valor {i+1}: "))
#     suma += valor

# promedio = suma / 10
# print(f"La suma total es: {suma}")
# print(f"El promedio es: {promedio}")

suma = 0
contador = 0

while contador < 10:
    valor = float(input(f"Ingrese el valor {contador+1}: "))
    suma += valor
    contador += 1

promedio = suma / 10
print(f"La suma total es: {suma}")
print(f"El promedio es: {promedio}")

