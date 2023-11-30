import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import mysql.connector
mydb=mysql.connector.connect (host="localhost", user="root", password="root")

#CREATING DATABASE AND TABLE
mycursor=mydb.cursor()
mycursor.execute("create database if not exists store")
mycursor.execute("use store")
mycursor.execute("create table if not exists signup(username varchar(20),password varchar(20))")


logged_in = False
def logged_in_status():
    return logged_in
def login_db(username, pw, mode):
    global logged_in
    if mode == 'SignUp':
        mycursor.execute("insert into signup values('"+username+"','"+pw+"')")
        mydb.commit()
        messagebox.showinfo("Success", "Signed Up Succesfully!")
    if mode == 'Login':
        mycursor.execute("select username from signup where username='"+username+"'")
        pot = mycursor.fetchone()

        mycursor.execute("select password from signup where password='"+pw+"'")
        a = mycursor.fetchone()

        if pot is not None and a is not None:
            messagebox.showinfo("Success", "Logged in Succesfully!")
            logged_in = True

#DEFINGING ALL THE FUNCTIONS USED
def add_record_to_db(book, genre, quantity, author, publication, price):

    mycursor.execute("select * from Available_Books where bookname='"+book+"'")
    row=mycursor.fetchone()

    if row is not None:
        mycursor.execute("update Available_Books set quantity=quantity+'"+str(quantity)+"' where bookname='"+book+"'")
        mydb.commit()
                        
                        
    else:
        mycursor.execute("insert into Available_Books(bookname,genre,quantity,author,publication,price) values('"+book+"','"+genre+"','"+str(quantity)+"','"+author+"','"+publication+"','"+str(price)+"')")
        mydb.commit()
                   
def search_record_in_db(display_frame, name, filter):
    mycursor.execute(f"select BookName, Genre, Author, Publication, Price from available_books where {filter} = '{name}'")
    records = mycursor.fetchall()
    records.insert(0, ("Book Name", "Genre", "Author", "Publisher", "Price"))

    for frame in display_frame.winfo_children():
        frame.destroy()

    Helvetica = Font(family = "Helvetica", weight = 'bold')
    
    print_record = ''
    for i, record in enumerate(records):
        bg_color = "#B9B9B9" if i == 0 else "#DCDCDC"
        for j, itm in enumerate(record):
            row_data = tk.Label(display_frame, text = str(itm), font = (Helvetica, 12), bg=bg_color, fg = "Black", width=20, height=2,highlightthickness=1, highlightbackground = "Black")
            row_data.place(x = j*190, y = i*45)

def sell_update_to_db(selector, name, phone, quantity, lk, p):
    print(name)

def get_available_books_from_db():
    mycursor.execute("select bookname from Available_Books")
    row = mycursor.fetchall()
    book_list = []
    for item in row:
        book_list.append(item[0])
    return book_list

def sell_book_from_db(book_name, name, phone, quantity):
    print(book_name)
    mycursor.execute("select price from Available_Books where bookname='"+str(book_name)+"'")
    p=mycursor.fetchone()
    price = p[0]
    mycursor.execute("select quantity from available_books where bookname='"+str(book_name)+"'")
    lk=mycursor.fetchone()

    mycursor.execute("select bookname from available_books where bookname='"+book_name+"'")
    log=mycursor.fetchone()

    if log is not None:
        mycursor.execute("insert into Sell_rec values('"+name+"','"+str(phone)+"','"+book_name+"','"+str(quantity)+"','"+str(price)+"')")
        mycursor.execute("update Available_Books set quantity=quantity-'"+quantity+"' where BookName='"+book_name+"'")
        mydb.commit()

        messagebox.showinfo("Success", "BOOK SOLD!")

    else:
        messagebox.showinfo("Sad", "BOOK UNAVAILABLE")

def sell_rec_display(display_frame):
    mycursor.execute(f"select * from sell_rec")
    records = mycursor.fetchall()
    records.insert(0, ("Customer", "Phone", "Book", "Qty", "Price"))

    for frame in display_frame.winfo_children():
        frame.destroy()

    Helvetica = Font(family = "Helvetica", weight = 'bold')
    
    print_record = ''
    for i, record in enumerate(records):
        bg_color = "#B9B9B9" if i == 0 else "#DCDCDC"
        for j, itm in enumerate(record):
            row_data = tk.Label(display_frame, text = str(itm), font = (Helvetica, 12), bg=bg_color, fg = "Black", width=20, height=2,highlightthickness=1, highlightbackground = "Black")
            row_data.place(x = j*190, y = i*45)

    




