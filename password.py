import tkinter as tk
from tkinter import StringVar
import random

def generate_password():
    
    length = 12

    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

    
    password = ''.join(random.choice(characters) for i in range(length))

    
    password_var.set(password)


app = tk.Tk()
app.title("Generator password")


password_var = StringVar()


password_label = tk.Label(app, text="Mot de passe:")
password_label.pack(pady=10)


password_entry = tk.Entry(app, textvariable=password_var, state='readonly', width=30)
password_entry.pack(pady=10)


generate_button = tk.Button(app, text="Générer mot de passe", command=generate_password)
generate_button.pack(pady=10)


quit_button = tk.Button(app, text="fermer la page", command=app.destroy)
quit_button.pack(pady=10)


app.mainloop()
