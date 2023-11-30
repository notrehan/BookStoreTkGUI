import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image
from functions import addRecord, searchRecord, sell_book, login
from db_functions import logged_in_status

root = tk.Tk()
root.geometry("1200x600")
root.title("Book Store")
root.iconbitmap("e:/Rehan/Python/Learning Tkinter/book.ico")

primary_bg = "#fff"
nav_bg = '#FF7600'
nav_button_bg = '#974702'

logged_in = logged_in_status()

Helvetica = Font(family = "Helvetica", weight = 'bold')

def homepage():
    login(main_frame, "Login", "Welcome Back!")


def add_record():
    if logged_in_status() == True:
        addRecord(main_frame, root)
    # home_frame = tk.Frame(main_frame)
    # lb = tk.Label(home_frame, text = "adding Page", font = ('Bold', 30))
    # lb.pack()
    # home_frame.pack(pady=20)

def sell_record():
    sell_book(main_frame)
    # home_frame = tk.Frame(main_frame)
    
    # lb = tk.Label(home_frame, text = "selling Page", font = (Helvetica, 30))
    # lb.pack()

    # home_frame.pack(pady=20)

def search_record():
    if logged_in_status() == True:
        searchRecord(main_frame)
    # home_frame = tk.Frame(main_frame)
    
    # lb = tk.Label(home_frame, text = "Dearchng page Page", font = ('Bold', 30))
    # lb.pack()

    # home_frame.pack(pady=20)

def hide_all_indicators():
    home_link.configure(bg = nav_bg)
    add_link.configure(bg = nav_bg)
    Sell_link.configure(bg = nav_bg)
    Search_link.configure(bg = nav_bg)

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicator(button, page):
    hide_all_indicators()
    button.configure(bg = nav_button_bg) 
    delete_pages()
    page()


options_frame = tk.Frame(root, bg = nav_bg)
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=150, height=600)


home_link = tk.Button(options_frame, text = 'Home', font = (Helvetica, 12), fg = 'White', bd = 0, bg = nav_bg, activebackground = nav_bg,activeforeground='White' , width=13, command = lambda: indicator(home_link, homepage), anchor='w', padx=15)
home_link.place(x=0, y=100)

add_link = tk.Button(options_frame, text = 'Add Book', font = (Helvetica, 12), fg = 'White', bd = 0, bg = nav_bg, activebackground = nav_bg,activeforeground='White' , width=13, command = lambda: indicator(add_link, add_record), anchor='w', padx=15)
add_link.place(x=0, y=135)

Sell_link = tk.Button(options_frame, text = 'Sell a Book', font = (Helvetica, 12), fg = 'White', bd = 0, bg = nav_bg, activebackground = nav_bg,activeforeground='White' , width=13, command = lambda: indicator(Sell_link, sell_record), anchor='w', padx=15)
Sell_link.place(x=0, y=170)

Search_link = tk.Button(options_frame, text = 'Search Books', font = (Helvetica, 12), fg = 'White', bd = 0, bg = nav_bg, activebackground = nav_bg,activeforeground='White' , width=13, command = lambda: indicator(Search_link, search_record), anchor='w', padx=15)
Search_link.place(x=0, y=205)


main_frame = tk.Frame(root, bg = primary_bg)

main_frame.pack(side=tk.RIGHT)
main_frame.pack_propagate(False)
main_frame.configure(width=1050, height=600)

root.mainloop()