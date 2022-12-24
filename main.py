import tkinter as tk
from tkinter import *
from tkinter import ttk

class App(tk.Frame):
    def __init__(self):



        root = tk.Tk()
        frm = ttk.Frame(root,padding=10)
        root.geometry("960x1024")
        root.title("Oszczędności")

        message = tk.Label(root, text="Nazwa Transakcji").grid(column=1,row=5)
        message = tk.Label(root, text="Kwota").grid(column=2, row=5)
        message = tk.Label(root, text="Data ").grid(column=3, row=5)
        message = tk.Label(root, text="    Opis").grid(column=4, row=5)

        message = tk.Label(root, text="Nazwa Transakcji").grid(column=1,row=8)
        message = tk.Label(root, text="Kwota").grid(column=2, row=8)
        message = tk.Label(root, text="Data ").grid(column=3, row=8)
        message = tk.Label(root, text="    Opis").grid(column=4, row=8)
        nazwa1 = tk.StringVar()
        kwota1 = tk.StringVar()
        data1 = tk.StringVar()
        opis1 = tk.StringVar()

        def submitValues():
            print(nazwa1.get(),kwota1.get(),data1.get(),opis1.get())
            koniec = 1

        def dodaj():
            print("Dodawanie Transakcji Test")
            koniec = 0
            while koniec ==0:
                nazwatransakcji = tk.Entry(root, textvariable=nazwa1).grid(column=1, row=6)
                kwotatransakcji = tk.Entry(root, textvariable=kwota1).grid(column=2, row=6)
                datatransakcji = tk.Entry(root, textvariable=data1).grid(column=3, row=6)
                opistransakcji = tk.Entry(root, textvariable=opis1).grid(column=4, row=6)
                submit = tk.Button(root, text="Zapisz", command=submitValues).grid(column=6, row=5)




        frm.grid()

        dodaj_transakcje = ttk.Button(root, text="Dodaj Transakcję", command=dodaj).grid(column=1,row=1)
        usun_transakcje = ttk.Button(root, text="Usuń Transakcję", command=Transakcja.usun).grid(column=2, row=1)




        root.mainloop()
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








