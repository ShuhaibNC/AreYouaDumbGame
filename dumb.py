import customtkinter
import random
from tkinter import Menu, messagebox

app = customtkinter.CTk()
app.geometry('700x500')
app.title('Are you a dumb?')

def debug_mode():
    nbutton.configure(command=on_debug_no)
    
def on_debug_no():
    title.configure(text="You're right, You're not dumb")

def show_about():
    messagebox.showinfo("About", "Developed by ShuhaibNC\nCopyright (C) 2016 All Rights Reserved")
def reset_all():
    nbutton.place(x=120, y = 40)
    nbutton.pack(side=customtkinter.RIGHT, padx=100)
    title.configure(text="Are you a dumb?")
    nbutton.configure(command=onno)
    messagebox.showinfo("Success", 'Successfully Reset')
menu_bar = Menu(app)
app.config(menu=menu_bar)

options_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset", command=reset_all)
options_menu.add_command(label='Turn on Debug mode', command=debug_mode)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)


def onyes():
    title.configure(text="I knew it!")

def onno():
    title.configure(text="Are you a dumb?")
    rwidth = random.randint(200, 570)
    rheight = random.randint(100, 460)
    print(f"X: {rwidth} Y: {rheight}")
    nbutton.place(x=rwidth, y = rheight)


title = customtkinter.CTkLabel(app, text="Are you a dumb? ", font=("Sans serif", 40, "bold"))
title.pack(pady=60)

ybutton =  customtkinter.CTkButton(app, text="Yes",font=('Sans serif', 19),width=120, height=40, command=onyes)
nbutton = customtkinter.CTkButton(app, text="No", font=('Sans serif', 19),width=120, height=40, command=onno)
ybutton.pack(side=customtkinter.LEFT, padx=100)
nbutton.pack(side=customtkinter.RIGHT, padx=100)

app.mainloop()