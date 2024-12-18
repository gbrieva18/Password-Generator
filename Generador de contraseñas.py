import re
import secrets
import string
import tkinter as tk
from tkinter import ttk, messagebox

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password

def generate_password_gui():
    try:
        length = int(length_entry.get())
        nums = int(numbers_var.get())
        special_chars = int(special_chars_var.get())
        uppercase = int(uppercase_var.get())
        lowercase = int(lowercase_var.get())

        if length < nums + special_chars + uppercase + lowercase:
            messagebox.showerror("Error", "La longitud no puede ser menor que la suma de los requisitos.")
            return

        password = generate_password(length, nums, special_chars, uppercase, lowercase)
        result_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores válidos.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Generador de Contraseñas")

# Variables
length_label = tk.Label(root, text="Longitud de la contraseña:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

length_entry = ttk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, "1")

numbers_var = tk.StringVar(value="")
special_chars_var = tk.StringVar(value="")
uppercase_var = tk.StringVar(value="")
lowercase_var = tk.StringVar(value="")

# Opciones
numbers_label = tk.Label(root, text="Números (mínimo):")
numbers_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
numbers_entry = ttk.Entry(root, textvariable=numbers_var)
numbers_entry.grid(row=1, column=1, padx=5, pady=5)

special_chars_label = tk.Label(root, text="Caracteres especiales (mínimo):")
special_chars_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
special_chars_entry = ttk.Entry(root, textvariable=special_chars_var)
special_chars_entry.grid(row=2, column=1, padx=5, pady=5)

uppercase_label = tk.Label(root, text="Mayúsculas (mínimo):")
uppercase_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
uppercase_entry = ttk.Entry(root, textvariable=uppercase_var)
uppercase_entry.grid(row=3, column=1, padx=5, pady=5)

lowercase_label = tk.Label(root, text="Minúsculas (mínimo):")
lowercase_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
lowercase_entry = ttk.Entry(root, textvariable=lowercase_var)
lowercase_entry.grid(row=4, column=1, padx=5, pady=5)

# Resultado
result_var = tk.StringVar()
result_label = tk.Label(root, text="Contraseña generada:")
result_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
result_entry = ttk.Entry(root, textvariable=result_var, state="readonly")
result_entry.grid(row=5, column=1, padx=5, pady=5)

# Botón para generar contraseña
generate_button = ttk.Button(root, text="Generar", command=generate_password_gui)
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
