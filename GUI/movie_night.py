import tkinter as tk
from tkinter import ttk


# main window
root = tk.Tk()
root.title("Movie night")
root.geometry("400x300")


# movie management
movies = { "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
           "Comedy": ["Superbad", "Step Brothers", "The Big Lebowski", "Dumb and Dumber"],
            "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic", "The Green Mile"], 
            "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"], 
            "Horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out", "The Exorcist"] 
        }
genre = list(movies.keys())

# month_cb.bind('<<ComboboxSelected>>', month_changed)


# choise of the genre
combo = ttk.Combobox(root, values=genre)
combo.pack()
combo.set("Selectionnez un genre")


def print_films(event):
    pass



root.mainloop()