#Realizar la carga de dos nombres por teclado. Moatrar cual de los dos es mayor alfabéticamente
# Pedimos al usuario que ingrese los dos nombres
nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")

# Comparamos los nombres en orden alfabético
if nombre1 > nombre2:
    print(f"{nombre1} es mayor alfabéticamente que {nombre2}.")
elif nombre2 > nombre1:
    print(f"{nombre2} es mayor alfabéticamente que {nombre1}.")
else:
    print("Ambos nombres son iguales alfabéticamente.")
