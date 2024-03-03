import customtkinter
import random

app = customtkinter.CTk()
app.geometry('700x500')
app.title('Are you a dumb?')

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