import tkinter as tk

# print(tk.TkVersion)

root = tk.Tk() #creation d'une fenetre principale
root.title("Test Tkinter") 
# label = tk.Label(root, text="Tkinter fonctionne!") #créons un widget Label (une étiquette) dans la fenêtre principale
# label.pack()
# Création de plusieurs labels
label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label2 = tk.Label(root, text="Label 2", bg="green", fg="white")
label3 = tk.Label(root, text="Label 3", bg="blue", fg="white")
# fg (foreground), bg (background)

# Affichage des labels dans l'ordre
label1.pack()
label2.pack()
label3.pack()
root.mainloop()