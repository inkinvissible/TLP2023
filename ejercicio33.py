#Escribe un progrma que lea 10 numeros y muestre cauntos valores ingresados son multiplos de 3 y de 5. (Pueden ser de ambos multiplos)
# Inicializar una variable para contar el número de múltiplos de 3 y 5
num_multiplos = 0

# Leer 10 números ingresados por el usuario
for i in range(10):
    num = int(input("Ingrese un número: "))
    
    # Verificar si el número es múltiplo de 3 y 5
    if num % 3 == 0 and num % 5 == 0:
        num_multiplos += 1

# Mostrar el resultado
print(f"Hay {num_multiplos} números que son múltiplos de 3 y 5.")
