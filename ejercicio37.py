#Desarrolle un programa que solicite la tabla de multiplicar de un numero ingresado hasta llegar al numero multiplicado por 12
num = int(input("Ingrese el número de la tabla de multiplicar que desea mostrar: "))

for i in range(1, 13):
    print("{} x {} = {}".format(num, i, num * i))
