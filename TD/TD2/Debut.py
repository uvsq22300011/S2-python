import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400


root = tk.Tk()

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
y1 = CANVAS_WIDTH
canvas.create_line(x0 + 200 , y - 200, x0 + 200, y1 - 200)
canvas.create_oval(x0 + 250, y - 95, x0 + 150 , y - 195)
canvas.create_oval(x0 + 250, y + 95, x0 + 150 , y + 195)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)


# Fin de votre code

canvas.grid(row=0, column=0)
root.mainloop()

