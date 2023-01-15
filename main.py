import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3


def database_submit(name_var, price_var, data_var, description_var, ):
    """
    This function is have to change data (for example: 2023.01.01 to 20230101 ) for easy sort
    and submit all data from user to database
    """

    data_var = str(data_var)
    data_to_number = data_var

    # def Date_to_database(self):
    date = data_to_number
    # date = self.data_to_number

    date_int = (date[0:4] + date[5:7] + date[8:])

    conn = sqlite3.connect("baza.db")
    conn.execute(
        "insert into transactions (name_of_transaction,price_of_transaction,data_of_transaction, "
        "description_of_transaction) values (?,?, ? ,?)",
        (name_var, price_var, date_int, description_var))

    conn.commit()

    conn.close()


class App:
    def __init__(self):
        self.data_to_number = ""

        self.root = tk.Tk()
        self.sorting_string = StringVar()
        self.main()
        self.root.mainloop()

    @staticmethod
    def delete():
        print("Delete transaction Test")

    def database_read(self):
        """
        This function is have to transform data from database to python and return list of data
        """

        conn = sqlite3.connect("baza.db")
        cursor = conn.execute(f"SELECT * FROM transactions {self.sorting_string.get()}")

        list_of_data = []
        for i in cursor:
            list_of_data.append(i)

        return list_of_data

    def print_transactions(self):
        """
        This function is have to create window where are all data of transactions
        """

        list_of_data = self.database_read()
        conn = sqlite3.connect("baza.db")
        win = Tk()
        win.geometry("700x350")
        style = ttk.Style()
        style.theme_use('clam')

        tree = ttk.Treeview(win, show='headings', height=10, columns="#1, #2, #3, #4")
        tree.column("#1", anchor=CENTER)
        tree.heading("# 1", text="Name transaction")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="price transaction")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Data transaction")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="description transaction")

        for i in list_of_data:
            date = str(i[2])

            date_int = (date[6:8] + "." + date[4:6] + "." + date[0:4])

            tree.insert('', 'end', text="1", values=(i[0], i[1], date_int, i[3]))

        tree.pack()
        win.mainloop()

        conn.commit()
        conn.close()

    def submit_values(self, name_var, price_var, data_var, description_var):
        """
        This function is have to get text from entries (data of name, price, date, description)
        """
        print(name_var, price_var, data_var, description_var, "TEST")
        database_submit(name_var, price_var, data_var, description_var)
        self.print_transactions()

    def add(self):
        """
        This function is current when button "Add Transaction" was used.
        She is to create entries and button off submit values which have to save data from the user.
        """
        Name1 = tk.StringVar()
        price1 = tk.StringVar()
        data1 = tk.StringVar()
        description1 = tk.StringVar()
        name_of_transaction = tk.Entry(self.root, textvariable=Name1)
        name_of_transaction.grid(column=1, row=6)
        price_of_transaction = tk.Entry(self.root, textvariable=price1)
        price_of_transaction.grid(column=2, row=6)
        data_of_transaction = tk.Entry(self.root, textvariable=data1)
        data_of_transaction.grid(column=3, row=6)
        description_of_transaction = tk.Entry(self.root, textvariable=description1)
        description_of_transaction.grid(column=4, row=6)

        tk.Button(self.root, text="Submit", command=lambda:
        self.submit_values(Name1.get(), price1.get(), data1.get(), description1.get())).grid(column=4, row=4)

    def create_window(self):
        """
        This function is have to create main window with texts and buttons
        """
        self.root.geometry("960x1024")
        self.root.title("Oszczędności")
        add_transaction = ttk.Button(self.root, text="Add Transaction", command=self.add)
        add_transaction.grid(column=1, row=1)
        delete_transaction = ttk.Button(self.root, text="Delete Transaction", command=self.delete())
        delete_transaction.grid(column=2, row=1)
        tk.Label(self.root, text="Name transaction").grid(column=1, row=5)
        tk.Label(self.root, text="price").grid(column=2, row=5)
        tk.Label(self.root, text="Data ").grid(column=3, row=5)
        tk.Label(self.root, text="    description").grid(column=4, row=5)

        self.sorting_string = tk.StringVar()
        # Buttons of sorting
        Radiobutton(self.root, text="Sort by cheapest", variable=self.sorting_string,
                    value="ORDER BY price_of_transaction",
                    command=lambda: self.print_transactions()).grid(column=16, row=10)
        Radiobutton(self.root, text="Sort by most expensive", variable=self.sorting_string,
                    value="ORDER BY price_of_transaction DESC",
                    command=lambda: self.print_transactions()).grid(column=16, row=11)
        Radiobutton(self.root, text="Sort by most recent", variable=self.sorting_string,
                    value="ORDER BY data_of_transaction",
                    command=lambda: self.print_transactions()).grid(column=16, row=12)
        Radiobutton(self.root, text="Sort by oldest", variable=self.sorting_string,
                    value="ORDER BY data_of_transaction DESC",
                    command=lambda: self.print_transactions()).grid(column=16, row=13)

    def main(self):
        self.create_window()


App = App()
