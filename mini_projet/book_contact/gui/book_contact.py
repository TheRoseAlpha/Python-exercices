import tkinter as tk 


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact 👥")
        self.geometry("400x250")
        self.config(bg='AntiqueWhite2')


        self.contact_dic = {}

        self.name_var = tk.StringVar()
        self.number_var = tk.StringVar()

        self.create_main_frame()
        self.create_widgets()

    def create_main_frame(self):
        self.main_frame = tk.Frame(self, bg='AntiqueWhite2')
        self.main_frame.pack()

        # frame_label = tk.Label(self.main_frame, text="Trying to learn about tkinter's frame", bg='azure1').pack()


    def create_widgets(self):
        self.name_label = tk.Label(self.main_frame, text="Name", bg='AntiqueWhite2')
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.name_entry = tk.Entry(self.main_frame, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)


        self.number_label = tk.Label(self.main_frame, text="Number", bg='AntiqueWhite2')
        self.number_label.grid(row=1, column=0, padx=5, pady=5)

        self.number_entry = tk.Entry(self.main_frame, textvariable=self.number_var)
        self.number_entry.grid(row=1, column=1, padx=5, pady=5)


        #button
        self.submit_button = tk.Button(self.main_frame, text='Submit', command=self.save_number)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.show_button = tk.Button(self.main_frame, text='Show contact', command=self.show_contact_list)
        self.show_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    def save_number(self):
        name = self.name_var.get()
        number = self.number_var.get()

        self.file_location = ".\\mini_projet\\book_contact\\contact_file.txt"


        if name and number:
            self.contact_dic[name] = number
            print(f"Contatto salvato: {name} -> {number}")

            with open(self.file_location, "a") as file:
                file.write(f"{name} : {number}\n")
            
        else:
            print("Errore: Nome o numero vuoti!")


    def show_contact_list(self):
        # with open(self.file_location, "r") as file:
        #     for line in file:
        #         print(line)
        
        for name, number in self.contact_dic.items():
            print(f"{name} : {number}")

        
     

        

app = App()
app.mainloop()








'''Se usi Python, Tkinter è una buona scelta. Alcuni widget utili:

Entry → per inserire nome, numero di telefono, email, ecc.
Listbox → per visualizzare i contatti salvati.
Button → per aggiungere, eliminare o modificare un contatto.
Label → per mostrare il nome dei campi (es. "Nome", "Telefono").
Frame o PanedWindow → per organizzare l'interfaccia.
Treeview (da ttk) → per mostrare una tabella con i contatti salvati.

usare grid invece di pack
config

columnspan=2 -> utilizzare piu di una colonna quindi in questo caso 2


Possibili valori di sticky
"n": Attacca il widget alla parte superiore della cella (North).
"s": Attacca il widget alla parte inferiore della cella (South).
"e": Attacca il widget al lato destro della cella (East).
"w": Attacca il widget al lato sinistro della cella (West).
"ne": Attacca il widget alla parte superiore destra della cella (North-East).
"nw": Attacca il widget alla parte superiore sinistra della cella (North-West).
"se": Attacca il widget alla parte inferiore destra della cella (South-East).
"sw": Attacca il widget alla parte inferiore sinistra della cella (South-West).
"nsew": Distribuisce il widget in tutti e quattro i lati della cella, facendolo espandere (North-South-East-West).'''
