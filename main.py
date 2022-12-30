import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3


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
        self.DBsubmit()
        self.DBread()



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


    # def ButtonOfChoose():
    #     print("XD")
    # def ChooseList(self):
    #     v = IntVar()
    #     Radiobutton(screen, text="Sortuj od najnizszej kwoty", variable=v, value=1, command=ChooseList).pack(anchor=W)
    #     Radiobutton(screen, text="Sortuj od najwyzszej kwoty", variable=v, value=2, command=ChooseList).pack(anchor=W)
    def DBsubmit(self):
        """

        """
        conn = sqlite3.connect("baza.db")
        conn.execute("insert into transakcje (nazwa_transakcji,kwota_transakcji,data_transakcji,opis_transakcji) values (?, ?, ?, ?)",
                    (self.nazwa1tekst,self.kwota1tekst,self.data1tekst,self.opis1tekst))


        conn.commit()


        conn.close()
    def DBread(self):


        """
        This function is have to transform data from database to python, and print sorted data's
        """
        conn = sqlite3.connect("baza.db")
        cursor = conn.execute(
            "SELECT nazwa_transakcji,kwota_transakcji,data_transakcji,opis_transakcji from transakcje")
        for i in cursor:
            # print("NAZWA = ", row[0])
            # print("KWOTA = ", row[1])
            # print("DATA = ", row[2])
            # print("OPIS = ", row[3], "\n")
            list_of_data = []
            list_of_data.append(i)



        cursor = conn.execute(
            "SELECT * from transakcje ORDER BY kwota_transakcji DESC")

        for i in cursor:



            # Create an instance of tkinter frame
            win = Tk()

            # Set the size of the tkinter window
            win.geometry("700x350")

            # Create an object of Style widget
            style = ttk.Style()
            style.theme_use('clam')

            # Add a Treeview widget
            tree = ttk.Treeview(win, column=("Nazwa", "Kota", "Data","Opis"), show='headings', height=5)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Nazwa Transakcji")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Kwota Transakcji")
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Data Transakcji")
            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Opis Transakcji")

            # Insert the data in Treeview widget
            tree.insert('', 'end', text="1", values=(self.nazwa1tekst, 'Kumar', '17701'))
            tree.insert('', 'end', text="1", values=('0','0','0','0'))
            tree.insert('', 'end', text="1", values=('Manisha', 'Joshi', '17703'))
            tree.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))
            tree.pack()
            win.mainloop()

            message = tk.Label(self.root, text=i[0]).grid(column=1,row=10),
            message = tk.Label(self.root, text=i[1]).grid(column=2,row=10),
            message = tk.Label(self.root, text=i[2]).grid(column=3,row=10),
            message = tk.Label(self.root, text=i[3]).grid(column=4, row=10),
        conn.commit()
        conn.close()
        return list_of_data



App = App()




#
# screen = Tk()
# def ChooseList():
#     print("XD")
# v = IntVar()
# Radiobutton(screen, text="Sortuj od najnizszej kwoty", variable=v, value=1,command=ChooseList).pack(anchor=W)
# Radiobutton(screen, text="Sortuj od najwyzszej kwoty", variable=v, value=2,command=ChooseList).pack(anchor=W)
#
# mainloop()
