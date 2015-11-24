#!/usr/bin/python3
import tkinter
from tkinter import *
from math import sqrt

def sign(v):
    if v >= 0:
        return 1
    else:
        return -1

def zoom(val, center, scale):
    return int(scale * val + center)

WIDTH = 800; HEIGHT = 600
x0 = 0.0; y0 = 0.0;
a = 0.4; b = 1.0; c = 0.0;
maxIt = 25600
scale = 350

window = Tk()
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "#000000")
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)

x = x0
y = y0
for i in range(maxIt):
    x_new = y - sign(x) * sqrt(abs(b * x - c))
    y_new = a - x
    x_real = zoom(x_new, WIDTH/2, scale)
    y_real = zoom(y_new, HEIGHT/2, scale)
    img.put("#A0A0A0", (x_real, y_real))
    #(int(WIDTH/2+x_new), int(HEIGHT/2+y_new)))
    x = x_new
    y = y_new

canvas.pack()
mainloop()
