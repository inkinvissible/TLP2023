#Realizar la carga de dos enteros por teclado. preguntar despues que ingresa el valor si desea cargar otro valor debiendo el operador ingresar la cadena "Si" para continuar, siingresa otra cosa, que termine. Mostrar la suma de los valores ingresados.
# Pedimos al usuario que ingrese los dos enteros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Pedimos al usuario si desea ingresar otro valor
continuar = input("¿Desea ingresar otro número? (Ingrese 'Si' para continuar): ").upper

# Mientras el usuario ingrese "Si", seguimos pidiendo valores
while continuar == "SI":
    num = int(input("Ingrese otro número: "))
    num1 += num
    continuar = input("¿Desea ingresar otro número? (Ingrese 'Si' para continuar): ")

# Mostramos la suma de los valores ingresados
print(f"La suma de los valores ingresados es {num1 + num2}.")
