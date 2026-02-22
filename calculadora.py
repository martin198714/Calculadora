import tkinter as tk
import math

# ----------------------------
# Funciones
# ----------------------------

def agregar(valor):
    pantalla_var.set(pantalla_var.get() + str(valor))

def limpiar():
    pantalla_var.set("")

def limpiar_historial():
    historial.delete(0, tk.END)

def cambiar_signo():
    valor = pantalla_var.get()
    if valor:
        if valor.startswith("-"):
            pantalla_var.set(valor[1:])
        else:
            pantalla_var.set("-" + valor)

def calcular():
    try:
        expresion = pantalla_var.get()
        resultado = eval(expresion)
        pantalla_var.set(str(resultado))
        historial.insert(tk.END, str(resultado))  # 🔥 solo resultado
    except:
        pantalla_var.set("Error")

def raiz():
    try:
        valor = float(pantalla_var.get())
        raiz_valor = math.sqrt(valor)

        if raiz_valor.is_integer():
            resultado = int(raiz_valor)
        else:
            resultado = round(raiz_valor, 6)

        pantalla_var.set(str(resultado))
        historial.insert(tk.END, str(resultado))  # 🔥 solo resultado
    except:
        pantalla_var.set("Error")

# ----------------------------
# Ventana
# ----------------------------

ventana = tk.Tk()
ventana.title("Calculadora con Historial")
ventana.geometry("600x600")
ventana.config(bg="#222831")
ventana.resizable(False, False)

pantalla_var = tk.StringVar()

# ----------------------------
# Pantalla
# ----------------------------

pantalla = tk.Entry(
    ventana,
    textvariable=pantalla_var,
    font=("Arial", 28),
    bd=0,
    justify="right",
    bg="#393E46",
    fg="white",
    insertbackground="white"
)
pantalla.pack(fill="x", padx=20, pady=20, ipady=20)

# ----------------------------
# Frame principal
# ----------------------------

main_frame = tk.Frame(ventana, bg="#222831")
main_frame.pack(expand=True, fill="both")

# Frame botones
frame = tk.Frame(main_frame, bg="#222831")
frame.pack(side="left", expand=True, fill="both", padx=10)

# Historial (Lista)
historial = tk.Listbox(
    main_frame,
    font=("Arial", 14),
    bg="#2E2E2E",
    fg="white"
)
historial.pack(side="right", fill="y", padx=10)

# Config grid
for i in range(6):
    frame.rowconfigure(i, weight=1)

for j in range(4):
    frame.columnconfigure(j, weight=1)

# ----------------------------
# Crear botón
# ----------------------------

def crear_boton(texto, fila, columna, comando, color="#00ADB5", colspan=1):
    boton = tk.Button(
        frame,
        text=texto,
        command=comando,
        font=("Arial", 18),
        bg=color,
        fg="white",
        bd=0,
        activebackground="#11999E"
    )
    boton.grid(row=fila, column=columna,
               columnspan=colspan,
               sticky="nsew", padx=5, pady=5)

# ----------------------------
# Botones
# ----------------------------

crear_boton("C", 0, 0, limpiar, "#E84545")
crear_boton("Hist C", 0, 1, limpiar_historial, "#6C757D")
crear_boton("√", 0, 2, raiz, "#6C757D")
crear_boton("/", 0, 3, lambda: agregar("/"), "#F8B500")

crear_boton("7", 1, 0, lambda: agregar("7"))
crear_boton("8", 1, 1, lambda: agregar("8"))
crear_boton("9", 1, 2, lambda: agregar("9"))
crear_boton("*", 1, 3, lambda: agregar("*"), "#F8B500")

crear_boton("4", 2, 0, lambda: agregar("4"))
crear_boton("5", 2, 1, lambda: agregar("5"))
crear_boton("6", 2, 2, lambda: agregar("6"))
crear_boton("-", 2, 3, lambda: agregar("-"), "#F8B500")

crear_boton("1", 3, 0, lambda: agregar("1"))
crear_boton("2", 3, 1, lambda: agregar("2"))
crear_boton("3", 3, 2, lambda: agregar("3"))
crear_boton("+", 3, 3, lambda: agregar("+"), "#F8B500")

crear_boton("+/-", 4, 0, cambiar_signo)
crear_boton("0", 4, 1, lambda: agregar("0"), colspan=2)
crear_boton(".", 4, 3, lambda: agregar("."))

crear_boton("=", 5, 0, calcular, "#00C853", colspan=4)

ventana.mainloop()