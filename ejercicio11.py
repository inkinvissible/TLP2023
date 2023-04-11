#Ejercicio 11. 11 de abril. Hacer un programa que pida dos valores que son las coordenadas (x,y) y mostrar los datos indicando el "punto es x,y". Luego, que indique en que cuadrante se encuentra. (1º cuadrante x>0), (2do cuadrante x<0, y<0), (3er cuadratnte y>0, x<0, y<0), (4to cuadrante x>0, y<0)
# Pedir las coordenadas x e y al usuario
x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))

# Mostrar los datos del punto
print("El punto es ({}, {})".format(x, y))

# Determinar en qué cuadrante se encuentra el punto
if x > 0 and y > 0:
    print("El punto se encuentra en el primer cuadrante")
elif x < 0 and y > 0:
    print("El punto se encuentra en el segundo cuadrante")
elif x < 0 and y < 0:
    print("El punto se encuentra en el tercer cuadrante")
elif x > 0 and y < 0:
    print("El punto se encuentra en el cuarto cuadrante")
else:
    print("El punto se encuentra sobre alguno de los ejes")
