import tkinter as tk
from random import randint


Height = 600
Weight = 400

color = "blue"


def cercle():
    global color
    x, y = randint(5+1, 405+1), randint(5+1, 405+1)
    canvas_noir.create_oval(x, y, x+100, y+100, fill=color)


def carre():
    global color
    x, y = randint(5+1, 405+1), randint(5+1, 405+1)
    canvas_noir.create_rectangle(x, y, x+100, y+100, fill=color)


def croix():
    global color
    x, y = randint(55+1, 405+1), randint(55+1, 405+1)
    canvas_noir.create_line(x, y, x + 100, y, fill=color, width=25)
    canvas_noir.create_line(x+50, y+50, x+50, y - 50, fill=color, width=25)


def choisircouleur():
    global color
    color = input("Quel couleur voulez vous ?")


root = tk.Tk()
title = root.title("Mon dessin")
root.config(bg="azure3")
b_cercle = tk.Button(text="Cercle", width=5, height=2, bg="darkseagreen3",
                     command=cercle)
b_carre = tk.Button(text="Carre", width=5, height=2, bg="darkseagreen3",
                    command=carre)
b_croix = tk.Button(text="Croix", width=5, height=2, bg="darkseagreen3",
                    command=croix)
b_choisircouleur = tk.Button(text="Choisir une couleur", width=20, height=2,
                             bg="darkseagreen3", command=choisircouleur)
canvas_noir = tk.Canvas(bg="black", width=Weight + 100, height=Height - 100,
                        bd=5, relief="groove")
b_cercle.grid(row=1, column=0)
b_carre.grid(row=2, column=0)
b_croix.grid(row=3, column=0)
b_choisircouleur.grid(row=0, column=1)
canvas_noir.grid(row=1, rowspan=3, column=1)

root.mainloop()
