#Desarrolle un programa que solicite por teclado 10 notas de alumnos y nos inbforme cuantas tienen mayores o iguales a 7 y cuantas menores
mayores_o_iguales = 0
menores = 0

for i in range(10):
    nota = float(input("Ingrese la nota del alumno {}: ".format(i+1)))
    if nota >= 7:
        mayores_o_iguales += 1
    else:
        menores += 1

print("La cantidad de notas mayores o iguales a 7 es:", mayores_o_iguales)
print("La cantidad de notas menores a 7 es:", menores)
