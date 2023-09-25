import tkinter as tk
import matplotlib.pyplot as plt
import spacy

# Paso 1: Diseño de la Interfaz de Usuario
def ingresar_gasto():
    gasto = entry_gasto.get()
    descripcion_gasto = entry_descripcion_gasto.get()
    categoria = combo_categorias.get()
    moneda = combo_monedas.get()

    # Actualizamos la lista de gastos
    lista_gastos.insert(tk.END, f"Descripción: {descripcion_gasto}, Categoría: {categoria}, Monto: {gasto} {moneda}")

    # Actualizamos el gráfico de gastos
    actualizar_grafico()

# Paso 2: Categorización Automática de Gastos
nlp = spacy.load("en_core_web_sm")

def categorizar_gasto(descripcion):
    doc = nlp(descripcion)
    # Implementar aquí la categorización automática (simulada)
    categoria = "Alimentos"
    return categoria

# Función para actualizar el gráfico de gastos
def actualizar_grafico():
    # Código de visualización de datos (como se mostró anteriormente)
    pass

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Gastos y Tiempo")

# Etiquetas y campos de entrada para ingreso de gastos
label_gasto = tk.Label(root, text="Ingresar Gasto:")
entry_gasto = tk.Entry(root)

label_descripcion_gasto = tk.Label(root, text="Descripción del Gasto:")
entry_descripcion_gasto = tk.Entry(root)

label_categoria = tk.Label(root, text="Categoría:")
combo_categorias = tk.StringVar()
combo_categorias.set("Alimentos")  # Valor predeterminado
dropdown_categorias = tk.OptionMenu(root, combo_categorias, "Alimentos", "Transporte", "Otros")

label_moneda = tk.Label(root, text="Moneda:")
combo_monedas = tk.StringVar()
combo_monedas.set("USD")  # Valor predeterminado
dropdown_monedas = tk.OptionMenu(root, combo_monedas, "USD", "EUR")

button_registrar_gasto = tk.Button(root, text="Registrar Gasto", command=ingresar_gasto)

# Lista de gastos registrados
lista_gastos = tk.Listbox(root)
lista_gastos.pack()

# Colocar elementos en la ventana
label_gasto.pack()
entry_gasto.pack()
label_descripcion_gasto.pack()
entry_descripcion_gasto.pack()
label_categoria.pack()
dropdown_categorias.pack()
label_moneda.pack()
dropdown_monedas.pack()
button_registrar_gasto.pack()

# Ejecutar la aplicación
root.mainloop()

