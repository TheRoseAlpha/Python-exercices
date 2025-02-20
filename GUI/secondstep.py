# Import de la bibliothèque
import tkinter as tk
from tkinter import ttk  # Pour les widgets modernes

# 1. Création de la fenêtre principale
root = tk.Tk()
root.title("Ma première application")
root.geometry("400x300")  # Définit la taille initiale (largeur x hauteur)

# 2. Les widgets de base
# Label - Pour afficher du texte
label = tk.Label(root, text="Bonjour!", font=("Arial", 12))
label.pack(pady=10)  # pady ajoute de l'espace vertical

# Button - Pour les actions
button = tk.Button(root, text="Cliquez-moi!", command=lambda: print("Bouton cliqué!"))
button.pack(pady=5)

# Entry - Pour la saisie de texte
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

# Text - Pour le texte multiligne
text_area = tk.Text(root, height=4, width=30)
text_area.pack(pady=5)

# Checkbutton - Pour les cases à cocher
var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Cochez-moi", variable=var)
checkbox.pack(pady=5)

# 3. Les gestionnaires de géométrie
frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
frame.pack(fill=tk.X)  # Remplit horizontalement

# Exemple avec pack()
tk.Label(frame, text="Pack:").pack(side=tk.LEFT)
tk.Button(frame, text="1").pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="2").pack(side=tk.LEFT, padx=5)

# Exemple avec grid()
frame2 = tk.Frame(root, pady=10)
frame2.pack()

tk.Label(frame2, text="Grid:").grid(row=0, column=0)
tk.Button(frame2, text="A").grid(row=0, column=1)
tk.Button(frame2, text="B").grid(row=1, column=0)
tk.Button(frame2, text="C").grid(row=1, column=1)

# Lancement de la boucle principale
root.mainloop()