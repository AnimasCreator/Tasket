import tkinter as tk
from tkinter import scrolledtext
import matplotlib.pyplot as plt
import spacy

# Lista de categorías preseleccionadas
categorias_preseleccionadas = ["Alimentos", "Transporte", "Educación", "Entretenimiento", "Salud", "Hogar", "Tecnología", "Viajes", "Otros"]

# Paso 1: Diseño de la Interfaz de Usuario
def ingresar_gasto():
    gasto = entry_gasto.get()
    descripcion_gasto = entry_descripcion_gasto.get()
    categoria = combo_categorias.get()
    moneda = combo_monedas.get()

    # Validar los datos ingresados
    if not validar_monto(gasto) or not descripcion_gasto or categoria not in categorias_preseleccionadas:
        mostrar_error ("Error de Validacion", "Por favor, ingrese datos validos en todos los campos.")
        return

    # Crear el registro del gasto
    registro_gasto = f"Descripción: {descripcion_gasto}\nCategoría: {categoria}\nMonto: {gasto} {moneda}\n\n"

    # Actualizamos la lista de gastos
    registro_text.insert(tk.END, registro_gasto)

    # Limpiar los campos de entrada después de registrar el gasto
    entry_gasto.delete(0, tk.END)
    entry_descripcion_gasto.delete(0, tk.END)

    # Actualizamos el gráfico de gastos
    actualizar_grafico()

#Funcion para validar el monto como un numero valido
def validar_monto(monto):
    try:
        float(monto)
        return True
    except ValueError:
        return False

#Funcion para mostrar mensaje de error
def mostrar_error(titulo, mensaje):
    error_window = tk.Toplevel(root)
    error_window.title(titulo)
    error_label = tk.Label(error_window, text=mensaje)
    error_label.pack()
    error_button = tk.Button(error_window, text="Cerrar", command=error_window.destroy)
    error_button.pack()

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
root.title("Tasket")

# Etiquetas y campos de entrada para ingreso de gastos
label_gasto = tk.Label(root, text="Monto del Gasto (en USD o EUR)")
entry_gasto = tk.Entry(root)

#Etiqueta y campo de entrada para la descripcion del gasto
label_descripcion_gasto = tk.Label(root, text="Descripcion del Gasto")
entry_descripcion_gasto = tk.Entry(root)

# Etiqueta y menú desplegable para seleccionar la categoría del gasto
label_categoria = tk.Label(root, text="Categoria del Gasto")
combo_categorias = tk.StringVar()
combo_categorias.set(categorias_preseleccionadas[0])  # Valor predeterminado
dropdown_categorias = tk.OptionMenu(root, combo_categorias, *categorias_preseleccionadas)

# Etiqueta y menú desplegable para seleccionar la moneda del gasto
label_moneda = tk.Label(root, text="Moneda:")
combo_monedas = tk.StringVar()
combo_monedas.set("EUR")  # Valor predeterminado
dropdown_monedas = tk.OptionMenu(root, combo_monedas, "USD", "EUR")

# Botón para registrar el gasto
button_registrar_gasto = tk.Button(root, text="Registrar Gasto", command=ingresar_gasto)

# Widget de registro de datos con barras de desplazamiento vertical y horizontal
registro_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)

# Colocar elementos en la ventana usando la cuadrícula
label_gasto.grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_gasto.grid(row=0, column=1, padx=10, pady=5)
label_descripcion_gasto.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_descripcion_gasto.grid(row=1, column=1, padx=10, pady=5)
label_categoria.grid(row=2, column=0, sticky="w", padx=10, pady=5)
dropdown_categorias.grid(row=2, column=1, padx=10, pady=5)
label_moneda.grid(row=3, column=0, sticky="w", padx=10, pady=5)
dropdown_monedas.grid(row=3, column=1, padx=10, pady=5)
button_registrar_gasto.grid(row=4, column=0, columnspan=2, pady=10)
registro_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Ejecutar la aplicación
root.mainloop()

