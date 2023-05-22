#Cargar una oracion y mostrar cuantos espacios en blanco se ingresan. Tener en cuenta que el espacio en blanco es: "". Luego transformar la oracion a minuscula, mayuscula y capitilize. 
import tkinter as tk
from tkinter import messagebox

def contar_espacios(oracion):
    contador = 0
    for caracter in oracion:
        if caracter == " ":
            contador += 1
    return contador

def transformar_oracion():
    oracion = entrada.get()
    espacios = contar_espacios(oracion)

    oracion_minuscula = oracion.lower()
    oracion_mayuscula = oracion.upper()
    oracion_capitalize = oracion.capitalize()

    messagebox.showinfo("Resultados",
                        f"Espacios en blanco: {espacios}\n\n"
                        f"Oración en minúscula: {oracion_minuscula}\n"
                        f"Oración en mayúscula: {oracion_mayuscula}\n"
                        f"Oración con capitalize: {oracion_capitalize}")

ventana = tk.Tk()
ventana.title("Contador de Espacios y Transformación de Oración")

etiqueta = tk.Label(ventana, text="Ingrese una oración:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Procesar", command=transformar_oracion)
boton.pack()

ventana.mainloop()
