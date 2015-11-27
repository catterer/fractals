#!/usr/bin/python3
import tkinter
from tkinter import *
from math import sqrt
import random

def sign(v):
    if v >= 0:
        return 1
    else:
        return -1

def zoom(val, center, scale):
    return int(scale * val + center)

class IterState(object):
    def __init__(self, pa, wi, he):
        self.colors = ["red", "orange", "yellow", "green", "blue", "violet"]
        self.parent = pa
        self.width = wi
        self.colorInc = 0
        self.height = he
        self.a = 0.4
        self.b = 1.0
        self.c = 0.0
        self.iter_time = 1
        self.newColor()
        self.reCenter(self.width/2, self.height/2)
        self.setScale(350)
        self.move_x = None
        self.move_y = None

        self.canvas = Canvas(window, width = self.width, height = self.height, bg = "#000000")
        self.img = PhotoImage(width = self.width, height = self.height)
        self.cimg = self.canvas.create_image((0, 0), image = self.img, state = "normal", anchor = tkinter.NW)
        self.canvas.tag_bind(self.cimg, '<ButtonPress-1>', self.onClick)
        self.canvas.tag_bind(self.cimg, '<ButtonRelease-1>', self.onUnclick)
        self.canvas.tag_bind(self.cimg, '<Motion>', self.onMotion)

        # Linux-only. On win use <MouseWheel> binding
        self.parent.bind("<Button-4>", self.onWheelUp)
        self.parent.bind("<Button-5>", self.onWheelDown)

        self.canvas.pack()

        self.parent.after(self.iter_time, self.next)

    def newColor(self):
        self.color = random.choice(self.colors)

    def reCenter(self, x, y):
        self.center_x = x
        self.center_y = y
        self.x = 0.0
        self.y = 0.0

    def next(self):
        self.colorInc = self.colorInc+1
        if self.colorInc == 10:
            self.colorInc = 0
            self.newColor()
        x_new = self.y - sign(self.x) * sqrt(abs(self.b * self.x - self.c))
        y_new = self.a - self.x
        x_real = zoom(x_new, self.center_x, self.scale)
        y_real = zoom(y_new, self.center_y, self.scale)
        if (x_real > 0 and y_real > 0):
            self.img.put(self.color, (x_real, y_real))
        self.x = x_new
        self.y = y_new
        self.parent.after(self.iter_time, self.next)

    def onMotion(self, event):
        self.img.blank()
        self.reCenter(event.x, event.y)

    def onClick(self, event):
        self.newColor()
        self.move_x = event.x
        self.move_y = event.y

    def onUnclick(self, event):
        self.canvas.move(self.cimg, event.x - self.move_x, event.y - self.move_y)

    def setScale(self, new):
        self.scale = new

    def onWheelUp(self, event):
        self.modScale(1.1)
    def onWheelDown(self, event):
        self.modScale(0.9)

    def modScale(self, coef):
        print('TODO')
#       iw, ih = self.img.size
#       size = int(iw * coef), int(ih * coef)
#       self.img = PhotoImage(self.img.resize(size))
#       self.setScale(self.scale * coef)
#       self.cimg = self.canvas.create_image((0, 0), image = self.img, state = "normal", anchor = tkinter.NW)



if __name__ == '__main__':
    window = Tk()
    it = IterState(window, 800, 600)
    mainloop()
