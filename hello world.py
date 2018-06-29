'''
import tkinter
from tkinter import Label
top = tkinter.Tk() # or just Tk() with "from Tkinter import *"
widget = tkinter.Label(None, text='Hello World')
widget.pack()
widget.mainloop()

'''

'''
from tkinter import*
root= Tk()
Button (root, text='Press Me', command=root.quit).pack(side=LEFT)
root.mainloop()

'''
'''
from tkinter import *
def quit():
    print('Hello, getting out of here')
    import sys
    sys.exit()
widget = Button(None, text='Press me to quit' , command=quit)
widget.pack()
widget.mainloop()

'''

'''
from tkinter import*
class HelloClass:
    # create the window in the class constructor
    def __init__(self):
        widget = Button(None, text='Press Me to quit', command=self.quit)
        widget.pack()
    def quit(self):
        print('leaving now')
        import sys ; sys.exit()
HelloClass()
# create a HelloClass object
mainloop()
'''

'''
from tkinter import*
def hello(event):
    print ('Double click to exit')
def quit(event):
    print ('caught a double click, leaving')
    import sys ; sys.exit()
widget= Button(None, text='Hello Event World')
widget.pack()
widget.bind("<Button‐1>", hello)
widget.bind("<Double‐1>" , quit)
widget.mainloop()

'''

'''
from tkinter import *

root = Tk()

def callback(event):
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=200, height=200)
frame.bind("<Button-1>", callback)
frame.pack()
root.mainloop()

'''
'''
import tkinter as tk
import cv2 as cv
button_flag = True
import os
os.chdir("/home/ccr/Documents")
def click():
    """
    respond to the button click
    """
    global button_flag
    # toggle button colors as a test
    if button_flag:
        button1.config(bg="white")
        button_flag = False
    else:
        button1.config(bg="green")
        button_flag = True
root = tk.Tk()
# create a frame and pack it
frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, fill=tk.X)
# pick a (small) image file you have in the working directory ...
photo1 = tk.PhotoImage(file="ka.png")
# create the image button, image is above (top) the optional text
button1 = tk.Button(frame1, compound=tk.TOP, width=148, height=240, image=photo1,
text="optional text", bg='green', command=click)
button1.pack(side=tk.LEFT, padx=2, pady=2)
# save the button's image from garbage collection (needed?)
button1.image = photo1
# start the event loop
root.mainloop()

'''


from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

# mainloop()

i = w.create_line(xy, fill="red")

w.coords(i, new_xy) # change coordinates
w.itemconfig(i, fill="blue") # change color

w.delete(i) # remove

w.delete(ALL) # remove all items
mainloop()