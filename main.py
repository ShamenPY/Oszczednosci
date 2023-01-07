import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3


def database_read(sorting_string):
    """
    This function is have to transform data from database to python and return list of data
    """
    conn = sqlite3.connect("baza.db")
    cursor = conn.execute(f"SELECT * FROM transactions {sorting_string}")

    list_of_data = []
    for i in cursor:
        list_of_data.append(i)

    return list_of_data


class App:
    def __init__(self):
        super().__init__()
        self.date = None
        self.data_to_number = None
        self.price1text = None
        self.description1text = None
        self.data1text = None
        self.name1text = None
        self.date_int = None
        self.root = tk.Tk()
        self.Name1 = tk.StringVar()
        self.price1 = tk.StringVar()
        self.data1 = tk.StringVar()
        self.description1 = tk.StringVar()
        self.main()

        self.root.mainloop()

    def main(self):
        self.create_window()
        self.add()
        self.submit_values()
        database_read(sorting_string=None)

    @staticmethod
    def delete():
        print("Delete transaction Test")

    def print_transactions(self, sorting_string="ORDER BY price_of_transaction DESC"):
        """
        This function is have to create window where are all data of transactions
        """
        list_of_data = database_read(sorting_string)
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

        # Change data (for example: 20233001 to 01.30.2023)
        for i in list_of_data:
            self.date = str(i[2])

            # self.date = self.data_to_number

            self.date_int = (self.date[6:8] + "." + self.date[4:6] + "." + self.date[0:4])
            # self.date_int = self(f"{self.date[6:7]}:{self.date[4:5]}:{self.date[0:3]}")
            print(self.date_int)

            tree.insert('', 'end', text="1", values=(i[0], i[1], self.date_int, i[3]))

        tree.pack()
        win.mainloop()

        conn.commit()
        conn.close()

    def submit_values(self):
        """
        This function is have to get text from entries (data of name, price, date, description)
        """
        self.name1text = self.Name1.get()
        self.price1text = self.price1.get()
        self.data1text = self.data1.get()
        self.description1text = self.description1.get()
        self.database_submit()
        self.print_transactions()

    def add(self):
        """
        This function is current when button "Add Transaction" was used.
        She is to create entries and button off submit values which have to save data from the user.
        """

        name_of_transaction = tk.Entry(self.root, textvariable=self.Name1)
        name_of_transaction.grid(column=1, row=6)
        price_of_transaction = tk.Entry(self.root, textvariable=self.price1)
        price_of_transaction.grid(column=2, row=6)
        data_of_transaction = tk.Entry(self.root, textvariable=self.data1)
        data_of_transaction.grid(column=3, row=6)
        description_of_transaction = tk.Entry(self.root, textvariable=self.description1)
        description_of_transaction.grid(column=4, row=6)

        tk.Button(self.root, text="Submit", command=lambda:
        self.submit_values()).grid(column=6, row=5)

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

        sorting_string = StringVar()
        #Buttons of sorting
        Radiobutton(self.root, text="Sort by cheapest", variable=sorting_string,
                    value="ORDER BY price_of_transaction",
                    command=lambda: self.print_transactions(sorting_string.get())).grid(column=16, row=10)
        Radiobutton(self.root, text="Sort by most expensive", variable=sorting_string,
                    value="ORDER BY price_of_transaction DESC",
                    command=lambda: self.print_transactions(sorting_string.get())).grid(column=16, row=11)
        Radiobutton(self.root, text="Sort by most recent", variable=sorting_string,
                    value="ORDER BY data_of_transaction",
                    command=lambda: self.print_transactions(sorting_string.get())).grid(column=16, row=12)
        Radiobutton(self.root, text="Sort by oldest", variable=sorting_string,
                    value="ORDER BY data_of_transaction DESC",
                    command=lambda: self.print_transactions(sorting_string.get())).grid(column=16, row=13)

    def database_submit(self):
        """
        This function is have to change data (for example: 2023.01.01 to 20230101 ) for easy sort
        and submit all data from user to database
        """

        self.data1text = str(self.data1text)
        self.data_to_number = self.data1text

        # def Date_to_database(self):
        self.date = self.data_to_number
        # self.date = self.data_to_number

        self.date_int = (self.date[0:4] + self.date[5:7] + self.date[8:])

        conn = sqlite3.connect("baza.db")
        conn.execute(
            "insert into transactions (name_of_transaction,price_of_transaction,data_of_transaction, "
            "description_of_transaction) values (?,?, ? ,?)",
            (self.name1text, self.price1text, self.date_int, self.description1text))

        conn.commit()

        conn.close()

        return self.date_int


App = App()
