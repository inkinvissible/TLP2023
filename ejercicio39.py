#Escriba un programa que pida (x,y) coordenadas que representa puntos en el plano. Informar cuantos puntos se han ingresado en el primer cuadrante, segundo cuadrante, tercer cuadrante y cuarto cuadrante. Los valores se ingresan por teclado.
# Pedimos al usuario que ingrese la cantidad de puntos que quiere analizar
n = int(input("Ingrese la cantidad de puntos que desea analizar: "))

# Inicializamos los contadores para cada cuadrante
cuadrante_1 = 0
cuadrante_2 = 0
cuadrante_3 = 0
cuadrante_4 = 0

# Creamos un ciclo for para que el usuario ingrese las coordenadas de cada punto
for i in range(n):
    print("Ingrese las coordenadas del punto", i+1)
    x = float(input("Coordenada x: "))
    y = float(input("Coordenada y: "))
    
    # Analizamos en qué cuadrante se encuentra el punto y lo contamos
    if x > 0 and y > 0:
        cuadrante_1 += 1
    elif x < 0 and y > 0:
        cuadrante_2 += 1
    elif x < 0 and y < 0:
        cuadrante_3 += 1
    elif x > 0 and y < 0:
        cuadrante_4 += 1

# Mostramos los resultados
print("Cantidad de puntos en el primer cuadrante:", cuadrante_1)
print("Cantidad de puntos en el segundo cuadrante:", cuadrante_2)
print("Cantidad de puntos en el tercer cuadrante:", cuadrante_3)
print("Cantidad de puntos en el cuarto cuadrante:", cuadrante_4)




# import turtle

# # Creamos la ventana y el lápiz
# window = turtle.Screen()
# pen = turtle.Turtle()

# # Definimos los límites del plano cartesiano
# plano_x_min = -200
# plano_x_max = 200
# plano_y_min = -200
# plano_y_max = 200

# # Dibujamos los ejes cartesianos
# pen.penup()
# pen.goto(plano_x_min, 0)
# pen.pendown()
# pen.goto(plano_x_max, 0)
# pen.penup()
# pen.goto(0, plano_y_min)
# pen.pendown()
# pen.goto(0, plano_y_max)

# # Creamos la lista vacía para almacenar los puntos
# puntos = []

# # Solicitamos al usuario que ingrese los puntos hasta que ingrese una coordenada negativa
# while True:
#     x = float(input("Ingrese la coordenada x del punto (ingrese un valor negativo para salir): "))
#     if x < 0:
#         break
#     y = float(input("Ingrese la coordenada y del punto: "))
#     puntos.append((x, y))

# # Clasificamos los puntos en uno de los cuatro cuadrantes y los agregamos a la lista correspondiente
# primer_cuadrante = []
# segundo_cuadrante = []
# tercer_cuadrante = []
# cuarto_cuadrante = []

# for x, y in puntos:
#     if x > 0 and y > 0:
#         primer_cuadrante.append((x, y))
#     elif x < 0 and y > 0:
#         segundo_cuadrante.append((x, y))
#     elif x < 0 and y < 0:
#         tercer_cuadrante.append((x, y))
#     elif x > 0 and y < 0:
#         cuarto_cuadrante.append((x, y))

# # Dibujamos los puntos en cada cuadrante con distintos colores
# pen.penup()
# for x, y in primer_cuadrante:
#     pen.goto(x, y)
#     pen.pendown()
#     pen.dot(5, "blue")
# pen.penup()
# for x, y in segundo_cuadrante:
#     pen.goto(x, y)
#     pen.pendown()
#     pen.dot(5, "red")
# pen.penup()
# for x, y in tercer_cuadrante:
#     pen.goto(x, y)
#     pen.pendown()
#     pen.dot(5, "green")
# pen.penup()
# for x, y in cuarto_cuadrante:
#     pen.goto(x, y)
#     pen.pendown()
#     pen.dot(5, "purple")

# # Mostramos la cantidad de puntos en cada cuadrante
# print("Cantidad de puntos en el primer cuadrante:", len(primer_cuadrante))
# print("Cantidad de puntos en el segundo cuadrante:", len(segundo_cuadrante))
# print("Cantidad de puntos en el tercer cuadrante:", len(tercer_cuadrante))
# print("Cantidad de puntos en el cuarto cuadrante:", len(cuarto_cuadrante))

# # Cerramos la ventana al hacer clic en ella
# window.exitonclick()
