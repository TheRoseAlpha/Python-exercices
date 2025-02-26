import tkinter as tk


#inheritance from tk.frame class
class HelloWorld(tk.Frame):
    def __init__(self, parent):
        # super(HelloWorld, self).__init__(parent)
        super().__init__(parent) #on met parent entre parenthese parce que quand 
        # on va creer une nouvelle instance on va mettre le parent dans la paranthese voir ligne 
        self.label = tk.Label(self, text="Hello World!!")
        # padx=20 → Ajoute 20 pixels d’espace horizontal (gauche et droite) autour du Label
        # pady=20 → Ajoute 20 pixels d’espace vertical (haut et bas) autour du Label
        self.label.pack(padx=20, pady=20)





if __name__ == "__main__":
    #windows creation
    root = tk.Tk()


    #window management
    root.title("First program")
    root.geometry("500x400")
    

    #label creation and management
    main = HelloWorld(root)
    # fill="both" → Le Frame main va s'étendre pour remplir toute la largeur et toute la hauteur de root.
    # expand=True → Permet à main de grandir si root est redimensionné
    main.pack(fill="both", expand=True)

    root.mainloop()