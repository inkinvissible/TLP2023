#Programa que pida un valor positivo y muestra del 1 al valor ingresado
valor = int(input("Ingrese un número entero positivo: "))
while valor <= 0:
    valor = int(input("El número ingresado no es positivo. Ingrese otro número: "))
    
for i in range(1, valor+1):
    print(i)

# valor = int(input("Ingrese un número entero positivo: "))
# while valor <= 0:
#     valor = int(input("El número ingresado no es positivo. Ingrese otro número: "))

# i = 1
# while i <= valor:
#     print(i)
#     i += 1
