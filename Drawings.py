'''

from tkinter import *

canvas_width = 200
canvas_height =200
python_green = "#476042"

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

points = [0,0,canvas_width,canvas_height/2, 0, canvas_height]
w.create_polygon(points, outline=python_green,
            fill='yellow', width=7)

mainloop()

'''

'''
from tkinter import *

canvas_width = 200
canvas_height =200
python_green = "#476042"

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]

w.create_polygon(points, outline=python_green,
            fill='yellow', width=3)

mainloop()

'''

'''

from tkinter import *

canvas_width = 300
canvas_height =80

master = Tk()
canvas = Canvas(master,
           width=canvas_width,
           height=canvas_height)
canvas.pack()

bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
nsteps = len(bitmaps)
step_x = int(canvas_width / nsteps)

for i in range(0, nsteps):
   canvas.create_bitmap((i+1)*step_x - step_x/2,50, bitmap=bitmaps[i])

mainloop()

'''

import cv2
import os
from tkinter import *
os.chdir("/home/ccr/Documents")
canvas_width = 300
canvas_height =300

#image = cv2.imread('ka.png')
#cv2.imwrite('MyPic2.jpeg', image)
master = Tk()

canvas = Canvas(master,
           width=canvas_width,
           height=canvas_height)
canvas.pack()

img = PhotoImage(file="champ.gif") # reads only gif , pgm/ppm images
canvas.create_image(20,20, anchor=NW, image=img)

mainloop()