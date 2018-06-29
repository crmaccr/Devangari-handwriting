

from tkinter import *
import os
canvas_width = 128
canvas_height = 128
os.chdir("/home/ccr/Documents")

def paint(event):
    python_black = "#000000"
    python_white = "#FFFFFF"
    python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill=python_white)



master = Tk()
master.title("Painting using Ovals")
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack(expand=YES, fill=BOTH)
w.bind("<B1-Motion>", paint)
w.config(background='black')

message = Label(master, text="Press and Drag the mouse to draw")
message.pack(fill=BOTH, expand=1)



canvasimg =Canvas(master, width=canvas_width, height=canvas_height)
img = PhotoImage(file="champ.gif") # reads only gif , pgm/ppm images
canvasimg.create_image(20,20, anchor=NW, image=img)
canvasimg.pack()

mainloop()

