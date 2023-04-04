# def opcion_1():
#     print("Has elegido la opción 1")

# def opcion_2():
#     print("Has elegido la opción 2")

# def opcion_3():
#     print("Has elegido la opción 3")

# def opcion_4():
#     print("Has elegido la opción 4")

# def opcion_5():
#     print("Has elegido la opción 5")

# # Creamos el diccionario con cada opción y su respectiva función
# opciones = {
#     1: opcion_1,
#     2: opcion_2,
#     3: opcion_3,
#     4: opcion_4,
#     5: opcion_5
# }

# # Pedimos al usuario que elija una opción
# opcion = int(input("Elige una opción: \n1) Cargar Cliente\n2) Eliminar Cliente\n3) Ver Clientes\n4) Listar clientes\n5) Hola"))

# #

# # Llamamos a la función correspondiente a la opción elegida
# opciones[opcion]()

########Inputs, Ejercicio 1##############
#       #     #
# lado = int(input("Ingrese la medida del lado del cuadrado\n"))
# superficie = lado*lado
# print("La sup del cuadrado es: ")
# print(superficie)

########Ejercicio 2##############
#       #     #
# num1 = int(input("Ingrese un valor"))
# num2 = int(input("Ingrese otro valor"))
# suma = num1+num2
# producto= num1*num2
# print("La suma de los valores es: ")
# print(suma)
# print("El producto de los números es: ")
# print(producto)

########Ejercicio 3##############
#       #     #Realizar la carga del precio y la cantidad y mostrar el importe
precio = int(input("Ingrese el precio\n"))
cantidad = int(input("Ingrese la cantidad del producto\n"))
total = precio*cantidad
print("El valor es: "+str(total))