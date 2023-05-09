#Realiza un programa que permita la carga por teclado del nombre, edad y altura de dos personas. Mostrar por pantalla el nombre de la persona con mayor altura.
# Pedimos al usuario que ingrese los datos de las dos personas
nombre1 = input("Ingrese el nombre de la primera persona: ")
edad1 = int(input("Ingrese la edad de la primera persona: "))
altura1 = float(input("Ingrese la altura de la primera persona (en metros): "))

nombre2 = input("Ingrese el nombre de la segunda persona: ")
edad2 = int(input("Ingrese la edad de la segunda persona: "))
altura2 = float(input("Ingrese la altura de la segunda persona (en metros): "))

# Comparamos las alturas de ambas personas
if altura1 > altura2:
    print(f"{nombre1} es la persona más alta con {altura1} metros.")
elif altura2 > altura1:
    print(f"{nombre2} es la persona más alta con {altura2} metros.")
else:
    print("Ambas personas tienen la misma altura.")
