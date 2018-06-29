import tkinter
from tkinter import  *
DEFAULT_PEN_SIZE = 9.0
DEFAULT_COLOR = 'black'

root = Tk()
root.title("MINST Predictor")
root.resizable(0, 0)

#model = Model()

old_x = None
old_y = None
line_width = DEFAULT_PEN_SIZE
color = DEFAULT_COLOR
eraser_on = False

def setup():
    c.bind('<B1-Motion>', paint)
    c.bind('<ButtonRelease-1>', reset)


def paint(event):
    line_width = DEFAULT_PEN_SIZE
    paint_color = 'white' if eraser_on else color

    if old_x and old_y:
        c.create_line(old_x, old_y, event.x, event.y,
                           width=line_width, fill=paint_color,
                           capstyle=ROUND, smooth=TRUE, splinesteps=36)
        

    old_x = event.x
    old_y = event.y



def reset(event):
    old_x, old_y = None, None



brush_button = Button(root, text='Predict') #, command=Predict)
brush_button.grid(row=0, column=2)

eraser_button = Button(root, text='Clear') #, command=use_eraser)
eraser_button.grid(row=0, column=3)

c = Canvas(root, bg='white', width=150, height=150)
c.grid(row=1, columnspan=5)

predictionLabel = Text(root, fg='blue', height=1, width=30,
                            borderwidth=0, highlightthickness=0,
                            relief='ridge')
predictionLabel.grid(row=0, column=6)

predictionScores = Text(root, height=10, width=30, padx=10,
                             borderwidth=0, highlightthickness=0,
                             relief='ridge')
predictionScores.grid(row=1, column=6)

image = Canvas(root, width=150, height=150,
                    highlightthickness=0, relief='ridge')
image.create_image(0, 0, anchor=NW, tags="IMG")
image.grid(row=2, rowspan=5, columnspan=5)
setup()
root.mainloop()







