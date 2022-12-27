import tkinter as tk
from tkinter import *
from tkinter import ttk


class App(tk.Frame):
    def __init__(self):

        self.root = tk.Tk()
        frm = ttk.Frame(self.root,padding=10)
        self.root.geometry("960x1024")
        self.root.title("Oszczędności")
        self.create_window()


        self.nazwa1 = tk.StringVar()
        self.kwota1 = tk.StringVar()
        self.data1 = tk.StringVar()
        self.opis1 = tk.StringVar()
        frm.grid()

        self.root.mainloop()

    def submit_values(self,nazwatransaskcji,kwotatransakcji,datatransakcji,opistransakcji):
        print(self.nazwa1.get(),self.kwota1.get(),self.data1.get(),self.opis1.get())
        self.nazwa1tekst = self.nazwa1.get()
        self.kwota1tekst = self.kwota1.get()
        self.data1tekst = self.data1.get()
        self.opis1tekst = self.opis1.get()
        self.data_to_txt()



        koniec = 1

    def usun(self):
        print("Usuwanie Transakcji Test")
    def dodaj(self):
        """
        This function is current when button "Add Transaction" was used.
        She is have to create entries and button off submit values which have to save data from the user.
        """
        print("Dodawanie Transakcji Test")
        nazwatransakcji = tk.Entry(self.root, textvariable=self.nazwa1)
        nazwatransakcji.grid(column=1, row=6)
        kwotatransakcji = tk.Entry(self.root, textvariable=self.kwota1)
        kwotatransakcji.grid(column=2, row=6)
        datatransakcji = tk.Entry(self.root, textvariable=self.data1)
        datatransakcji.grid(column=3, row=6)
        opistransakcji = tk.Entry(self.root, textvariable=self.opis1)
        opistransakcji.grid(column=4, row=6)

        tk.Button(self.root, text="Zapisz", command=lambda:
        self.submit_values(nazwatransakcji,kwotatransakcji,datatransakcji,opistransakcji)).grid(column=6,row=5)

    def create_window(self):
        """
        This function is have to create texts and buttons,
        generally She is have to create widgets which won't change self.
        """

        dodaj_transakcje = ttk.Button(self.root, text="Dodaj Transakcję", command=self.dodaj)
        dodaj_transakcje.grid(column=1, row=1)
        usun_transakcje = ttk.Button(self.root, text="Usuń Transakcję", command=self.usun)
        usun_transakcje.grid(column=2, row=1)
        message = tk.Label(self.root, text="Nazwa Transakcji").grid(column=1, row=5)
        message = tk.Label(self.root, text="Kwota").grid(column=2, row=5)
        message = tk.Label(self.root, text="Data ").grid(column=3, row=5)
        message = tk.Label(self.root, text="    Opis").grid(column=4, row=5)

        message = tk.Label(self.root, text="Nazwa Transakcji").grid(column=1, row=8)
        message = tk.Label(self.root, text="Kwota").grid(column=2, row=8)
        message = tk.Label(self.root, text="Data ").grid(column=3, row=8)
        message = tk.Label(self.root, text="    Opis").grid(column=4, row=8)
    def data_to_txt(self):
        """
        This function is have to transfer data from tkinter to .txt file.
        """
        with open("dane transakcji.txt", "w") as f:
            f.write(self.nazwa1tekst)
            f.write(";")
            f.write(self.kwota1tekst)
            f.write(";")
            f.write(self.data1tekst)
            f.write(";")
            f.write(self.opis1tekst)
            f.write(";")
            f.close()

App = App()



