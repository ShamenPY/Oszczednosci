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

    def submitValues(self):
        print(self.nazwa1.get(),self.kwota1.get(),self.data1.get(),self.opis1.get())
        koniec = 1

    def dodaj(self):
        print("Dodawanie Transakcji Test")
        koniec = 0
        while koniec ==0:
            nazwatransakcji = tk.Entry(self.root, textvariable=self.nazwa1).grid(column=1, row=6)
            kwotatransakcji = tk.Entry(self.root, textvariable=self.kwota1).grid(column=2, row=6)
            datatransakcji = tk.Entry(self.root, textvariable=self.data1).grid(column=3, row=6)
            opistransakcji = tk.Entry(self.root, textvariable=self.opis1).grid(column=4, row=6)
            submit = tk.Button(self.root, text="Zapisz", command=self.submitValues()).grid(column=6, row=5)

    def create_window(self):

        dodaj_transakcje = ttk.Button(self.root, text="Dodaj Transakcję", command=self.dodaj).grid(column=1, row=1)
        usun_transakcje = ttk.Button(self.root, text="Usuń Transakcję", command=Transakcja.usun).grid(column=2, row=1)
        message = tk.Label(self.root, text="Nazwa Transakcji").grid(column=1, row=5)
        message = tk.Label(self.root, text="Kwota").grid(column=2, row=5)
        message = tk.Label(self.root, text="Data ").grid(column=3, row=5)
        message = tk.Label(self.root, text="    Opis").grid(column=4, row=5)

        message = tk.Label(self.root, text="Nazwa Transakcji").grid(column=1, row=8)
        message = tk.Label(self.root, text="Kwota").grid(column=2, row=8)
        message = tk.Label(self.root, text="Data ").grid(column=3, row=8)
        message = tk.Label(self.root, text="    Opis").grid(column=4, row=8)




class Transakcja():
    def __init__(self):

        pass
    def kwota(self):
        pass
    def data(selfO):
        pass
    def opis(self):
        pass
    def usun():
        print("Usuwanie Transakcji Test")




App = App()




"""
Plany na dzis:
Petla ktora bedzie odpalac sie gdy chcesz dodac transakcje, wywali ci ona te entry do wpisywania tekstu,
po petli wszystko sie zapisze i stworzy sie pod spodem cala transakcja
"""


