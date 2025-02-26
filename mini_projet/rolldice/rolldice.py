import tkinter as tk
from tkinter import ttk


class Dice_Roller(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Digital Dice Roller")
        self.label.pack(padx=20, pady=20)

        self.dice_option = ['D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']

        self.option_var = tk.StringVar(self) #pas compris mais a voir

        # self.option_menu = tk.OptionMenu(self, self.option_var, "Select Dice", *self.dice_option)
        # self.option_menu.pack(padx=20, pady=20)
        self.option_menu = ttk.Combobox(self, 
                                      textvariable=self.option_var,
                                      values=self.dice_option,
                                      state="readonly")
        self.option_menu.set("Select Dice")
        self.option_menu.pack(padx=20, pady=20)

if __name__ == "__main__":
    #windows creation
    root = tk.Tk()

    #windows management
    root.title("Digital Dice Roller")
    root.geometry("500x450")

    main= Dice_Roller(root)
    main.pack(fill="both", expand=True)


    root.mainloop()
