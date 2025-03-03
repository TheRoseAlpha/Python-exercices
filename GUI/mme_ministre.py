import tkinter as tk

def risposta(vero):
    if vero:
        # label_risultato.config(text="Tu as choisi vrai ✅", fg="green")
        label_risultato.config(text="ET ben NON 💀❌", fg="red")
    else:
        label_risultato.config(text="C'est exacte 💀❌", fg="green")

# Creazione della finestra principale
root = tk.Tk()
root.title("Quiz du Ministre")
root.geometry("300x200")

# Label con la domanda
label_domanda = tk.Label(root, text="Mme la Ministre Mary Poppins se sent très fatiguée ces derniers jours.\n"
                         " Ira elle en pharmacie prendre son magnesium ? ", font=("Arial", 12))
label_domanda.pack(pady=10)

# Bottoni Vero / Falso
frame_bottoni = tk.Frame(root)
frame_bottoni.pack(pady=10)

btn_vero = tk.Button(frame_bottoni, text="Vrai", font=("Arial", 10), command=lambda: risposta(True))
btn_vero.pack(side="left", padx=10)

btn_falso = tk.Button(frame_bottoni, text="Faux", font=("Arial", 10), command=lambda: risposta(False))
btn_falso.pack(side="left", padx=10)

# Label per mostrare la risposta
label_risultato = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_risultato.pack(pady=20)

# Avvia la finestra Tkinter
root.mainloop()