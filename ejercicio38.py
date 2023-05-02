#Realiza un programa que lea n cantidad de triangulos y que lea sus lados e informe: a) De c/u, qué tipo de triángulo es: equilátero (los 3 iguales), isoceles y escalenos. b) Cantidad de triangulos de cada tipo.
# Pedimos al usuario que ingrese la cantidad de triángulos que quiere analizar
n = int(input("Ingrese la cantidad de triángulos que desea analizar: "))

# Inicializamos los contadores para cada tipo de triángulo
equilateros = 0
isoceles = 0
escalenos = 0

# Creamos un ciclo for para que el usuario ingrese los datos de cada triángulo
for i in range(n):
    print("Ingrese los lados del triángulo", i+1)
    a = float(input("Lado a: "))
    b = float(input("Lado b: "))
    c = float(input("Lado c: "))
    
    # Analizamos el tipo de triángulo y lo contamos
    if a == b == c:
        print("El triángulo", i+1, "es equilátero")
        equilateros += 1
    elif a == b or a == c or b == c:
        print("El triángulo", i+1, "es isósceles")
        isoceles += 1
    else:
        print("El triángulo", i+1, "es escaleno")
        escalenos += 1

# Mostramos los resultados
print("Cantidad de triángulos equiláteros:", equilateros)
print("Cantidad de triángulos isósceles:", isoceles)
print("Cantidad de triángulos escalenos:", escalenos)
