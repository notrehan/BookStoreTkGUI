import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image
from tkinter import messagebox
from db_functions import add_record_to_db, search_record_in_db, login_db, sell_book_from_db

def SignUp(main_frame, y):
    login(main_frame, "SignUp", y)

def login(main_frame, x, welcome_mssg):
    home_frame = tk.Frame(main_frame)

     #defining fonts
    Helvetica = Font(family = "Helvetica", weight = 'bold')

    Heading = tk.Label(home_frame, text = x, font = (Helvetica, 20))
    lb = tk.Label(home_frame, text = welcome_mssg, font = (Helvetica, 15), fg='Black')
    Heading.grid(row = 0, column=0, columnspan=2, sticky='w')
    lb.grid(row = 1, column=0, columnspan=2, sticky='w')
    

    home_frame.pack(pady=20)
    book_lb = tk.Label(home_frame, text = "Username: ", font = (Helvetica, 15)).grid(row=2, column=0, sticky='w')
    username_e = tk.Entry(home_frame, width= 30, font=(Helvetica, 20))
    username_e.grid(row=2, column=1, columnspan = 1, pady=5)

    book_lb = tk.Label(home_frame, text = "Password: ", font = (Helvetica, 15)).grid(row=3, column=0, sticky='w')
    password_e = tk.Entry(home_frame, width= 30, font=(Helvetica, 20))
    password_e.grid(row=3, column=1, columnspan = 1, pady=5)

    submit_btn = tk.Button(home_frame, text = x, font = (Helvetica, 15), fg = 'White', bd = 0, bg = "Blue", command = lambda: login_db(username_e.get(), password_e.get(), x))
    submit_btn.grid(row=4, column=1,pady=5)

    sign_up_btn = tk.Button(home_frame, text = "Sign Up for new account", font = (Helvetica, 15), fg = 'Blue', bd = 0, command = lambda: SignUp(main_frame,"First Time?"))
    sign_up_btn.grid(row=5, column=1, pady=5)




def add_to_record(name, genre, quantity, author, publication, price):
    book = name.get()
    genre = genre.get()
    quantity = quantity.get()
    author = author.get()
    publication = publication.get()
    price = price.get()
    add_record_to_db(book, genre, quantity, author, publication, price,)

    messagebox.showinfo("Success", "Record Added Succesfully!")

def addRecord(main_frame, root):
    home_frame = tk.Frame(main_frame)

    #defining fonts
    Helvetica = Font(family = "Helvetica", weight = 'bold')
    
    Heading = tk.Label(home_frame, text = "ADD BOOKS (To Database)\n", font = (Helvetica, 20))
    lb = tk.Label(home_frame, text = "All information prompted are mandatory to be filled", font = (Helvetica, 15), fg='Red')
    Heading.grid(row = 0, column=0, columnspan=2, sticky='w')
    lb.grid(row = 1, column=0, columnspan=2, sticky='w')
    

    home_frame.pack(pady=20)
    book_lb = tk.Label(home_frame, text = "Book Name: ", font = (Helvetica, 15)).grid(row=2, column=0, sticky='w')
    book_e = tk.Entry(home_frame, width= 30, font=(Helvetica, 20))
    book_e.grid(row=2, column=1, columnspan = 1, pady=5)

    genre_lb = tk.Label(home_frame, text = "Genre: ", font = (Helvetica, 15)).grid(row=3, column=0, sticky='w')
    genre_e = tk.Entry(home_frame, width= 30, font=(Helvetica, 20))
    genre_e.grid(row=3, column=1, columnspan = 1, pady=5)
    

    quantity_lb = tk.Label(home_frame, text = "Quantity: ", font = (Helvetica, 15)).grid(row=4, column=0, sticky='w')
    quantity_e = tk.Entry(home_frame, width= 30, font=(Helvetica, 20))
    quantity_e.grid(row=4, column=1, columnspan = 1, pady=5)
    

    author_lb = tk.Label(home_frame, text = "Author Name: ", font = (Helvetica, 15)).grid(row=5, column=0, sticky='w')
    author_e = tk.Entry(home_frame, width= 30, font=(Helvetica, 20))
    author_e.grid(row=5, column=1, columnspan = 1, pady=5)
    

    publication_lb = tk.Label(home_frame, text = "Publisher Name: ", font = (Helvetica, 15)).grid(row=6, column=0, sticky='w')
    publication_e = tk.Entry(home_frame, width= 30, font=(Helvetica, 20))
    publication_e.grid(row=6, column=1, columnspan = 1, pady=5)

    price_lb = tk.Label(home_frame, text = "Price: ", font = (Helvetica, 15)).grid(row=7, column=0, sticky='w')
    price_e = tk.Entry(home_frame, width= 30, font=(Helvetica, 20))
    price_e.grid(row=7, column=1, columnspan = 1, pady=5)

    submit_btn = tk.Button(home_frame, text = 'Submit Into Database', font = (Helvetica, 15), fg = 'White', bd = 0, bg = "Red", command = lambda: add_to_record(book_e,genre_e,quantity_e,author_e,publication_e,price_e))
    submit_btn.grid(row=9, column=1,pady=5)


def searchRecord(main_frame):
    home_frame = tk.Frame(main_frame)

    #defining fonts
    Helvetica = Font(family = "Helvetica", weight = 'bold')

    Heading = tk.Label(home_frame, text = "SEARCH BOOKS\n", font = (Helvetica, 20))
    lb = tk.Label(home_frame, text = "All information prompted are mandatory to be filled", font = (Helvetica, 15), fg='Red')
    Heading.grid(row = 0, column=0, columnspan=3, sticky='w')
    lb.grid(row = 1, column=0, columnspan=3, sticky='w')
    
    selector = tk.StringVar()
    selector.set("                                        ")

    home_frame.pack(pady=20)
    Picker_lb = tk.Label(home_frame, text = "Select Filter: ", font = (Helvetica, 15))
    Picker_lb.grid(row=2, column=0,columnspan = 2,  sticky='w')
    search_by = tk.OptionMenu(home_frame, selector, "BookName", "Genre", "Author", "                                        ")
    search_by.grid(row=2, column=2, columnspan = 2, sticky='w', pady=5)

    search_box = tk.Entry(home_frame, width= 15, font=(Helvetica, 20))
    search_box.grid(row=3, column=0, columnspan = 2, sticky='w')

    go_btn = tk.Button(home_frame, text = 'GO!', font = (Helvetica, 12), width=18, fg = 'White', bd = 0, bg = "#003EFF", command = lambda: search_record_in_db(display_frame, search_box.get(), str(selector.get())))
    go_btn.grid(row=3, column=2, columnspan = 2, sticky='w')

    display_frame = tk.Frame(main_frame, bg = "White")
    display_frame.pack(side=tk.BOTTOM)
    display_frame.pack_propagate(False)
    display_frame.configure(width=950, height=450)
    
def sell_book(main_frame):
    home_frame = tk.Frame(main_frame)
    home_frame.pack(pady=20)
    #defining fonts
    Helvetica = Font(family = "Helvetica", weight = 'bold')

    Heading = tk.Label(home_frame, text = "SELL BOOKS", font = (Helvetica, 20))
    Heading.grid(row = 0, column=0, columnspan=3, sticky='w')

    cname_lb = tk.Label(home_frame, text = "Customer Name:", font = (Helvetica, 15)).grid(row=2, column=0, sticky='w')
    cname_e = tk.Entry(home_frame, width= 30, font=(Helvetica, 20))
    cname_e.grid(row=2, column=1, columnspan = 1, pady=5)

    phone_lb = tk.Label(home_frame, text = "Phone Number:", font = (Helvetica, 15)).grid(row=3, column=0, sticky='w')
    phone_e = tk.Entry(home_frame, width= 30, font=(Helvetica, 20))
    phone_e.grid(row=3, column=1, columnspan = 1, pady=5)

    quantity_lb = tk.Label(home_frame, text = "Quantity:", font = (Helvetica, 15)).grid(row=5, column=0, sticky='w')
    quantity_e = tk.Entry(home_frame, width= 30, font=(Helvetica, 20))
    quantity_e.grid(row=5, column=1, columnspan = 1, pady=5)

    bookname_lb = tk.Label(home_frame, text = "Book Name:", font = (Helvetica, 15)).grid(row=4, column=0, sticky='w')

    sell_book_from_db(home_frame, cname_e.get(), phone_e.get(), quantity_e.get())
    

        