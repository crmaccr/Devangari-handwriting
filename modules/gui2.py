#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk, ImageOps
import os
print(os.getcwd())
import numpy as np
import cv2
from tkinter import filedialog


# from modules.load import Model
from threading import Thread
import webbrowser
from modules.nn import NeuralNetwork


class Paint(object):
    HIDDEN = True
    DEFAULT_PEN_SIZE = 9.0
    DEFAULT_COLOR = 'black'

    def __init__(self):

        print(os.getcwd())
        self.root = Tk()
        self.root.title(" Predictor")
        self.root.resizable(0, 0)
        self.panelA = None
        self.tva =[]

        # number of input, hidden and output nodes
        # input_nodes = 784
        input_nodes = 1024
        hidden_nodes = 100
        output_nodes = 10

        # learning rate is 0.3
        learning_rate = 0.3

        # create instance of neural network
        self.net = NeuralNetwork(input_nodes, hidden_nodes, output_nodes,learning_rate)

        self.brush_button = Button(self.root, text='Predict', command=self.Show)
        self.brush_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='Clear', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.c = Canvas(self.root, bg='white', width=150, height=150)
        self.c.grid(row=1, columnspan=5)

        self.predictionLabel = Text(self.root, fg='blue', height=1, width=30,
                                    borderwidth=0, highlightthickness=0,
                                    relief='ridge')
        self.predictionLabel.grid(row=0, column=6)

        self.predictionScores = Text(self.root, height=10, width=30, padx=10,
                                     borderwidth=0, highlightthickness=0,
                                     relief='ridge')
        self.predictionScores.grid(row=1, column=6)

        self.image = Canvas(self.root, width=150, height=150,
                            highlightthickness=0, relief='ridge')
        self.image.create_image(0, 0, anchor=NW, tags="IMG")
        self.image.grid(row=2, rowspan=5, columnspan=5)
        '''
        self.nnImageOriginal = Image.open("images/nn.png")
        self.resizeAndSetImage(self.nnImageOriginal)
        '''
        ''''''
        self.train_button = Button(self.root, text='Train', command=self.Train)
        self.train_button.grid(row=0, column=4)

        self.browse_btn = Button(self.root, text='Select an image', command=self.selectImage_andToggle)
        self.browse_btn.grid(row=0, column=5)

        self.recognize_btn = Button(self.root, text='recognize image', command=self.recognizeimage)
        # self.recognize_btn.grid(row=3, column=6)
        self.setup()
        self.root.mainloop()



    def resizeAndSetImage(self, image):
        size = (150, 150)
        resized = image.resize(size, Image.BILINEAR)
        self.nnImage = ImageTk.PhotoImage(resized)
        self.image.delete("IMG")
        self.image.create_image(0, 0, image=self.nnImage, anchor=NW, tags="IMG")

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.DEFAULT_PEN_SIZE
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)




    def Show(self):

        self.c.postscript(file="tmp.ps", colormode="color")
        img = Image.open("tmp.ps")
        img.save("/home/ccr/PycharmProjects/Tkinter/modules/out.png", "png")
        # im =Image.open("out.png")
        # inverted_image = ImageOps.invert(im)
        # inverted_image.save("inverted.png")
        # inverted_image.show()
        #self.resizeAndSetImage(inverted_image)

        hold = self.net.imageprepare("/home/ccr/PycharmProjects/Tkinter/modules/out.png")
        res = self.net.query(hold)
        char = np.argmax(res)
        print(char)
        char2 = self.numbers_to_strings(char)

        self.predictionLabel.insert(END, "This is a {}".format(char2))

    def numbers_to_strings(self,argument):
        switcher = {0: "०",
                    1: "१",
                    2: "२"
                    }
        return switcher.get(argument, "nothing")

    def use_eraser(self):
        self.predictionLabel.delete(1.0, END)
        self.predictionScores.delete(1.0, END)
        self.c.delete("all")
        # self.resizeAndSetImage(self.nnImageOriginal)

    def paint(self, event):
        self.line_width = self.DEFAULT_PEN_SIZE
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def Train(self):
        self.net.preare_to_train()
        messagebox.showinfo("Training", "training completed")

    def select_image(self):
        # grab a reference to the image panels

        # open a file chooser dialog and allow the user to select an input image
        path = filedialog.askopenfilename()

        # ensure a file path was selected
        if len(path) > 0:
            # load the image from disk, convert it to grayscale, and detect  edges in it
            image = cv2.imread(path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            x = np.asarray(gray)
            y = []
            for row in x:
                for element in row:
                    y.append(element)
            self.tva = [k * 0.99 / 255.0 + 0.01 for k in y]
            edged = cv2.Canny(gray, 50, 100)

            # OpenCV represents images in BGR order; however PIL represents
            # images in RGB order, so we need to swap the channels
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # converting the images to PIL format
            image = Image.fromarray(image)
            edged = Image.fromarray(edged)

            # and then to ImageTk format
            image = ImageTk.PhotoImage(image)
            edged = ImageTk.PhotoImage(edged)

            # if the panels are None, initialize them
            if self.panelA is None:
                # the first panel will store our original image
                self.panelA = Label(image=image, height=200, width=200)
                self.panelA.image = image
                # self.panelA.pack(side="left", padx=10, pady=10)
                self.panelA.grid(row=2, column=6)

            else:
                # update the panels
                self.panelA.configure(image=image)
                self.panelA.image = image

    def toggle_browse(self):
        if self.HIDDEN:
            self.recognize_btn.grid(row=3, column=6)
        else:
            self.recognize_btn.grid_remove()
        self.HIDDEN = not self.HIDDEN

    def selectImage_andToggle(self):
        self.select_image()
        self.toggle_browse()

    def recognizeimage(self):
        res = self.net.query(self.tva)
        print(np.argmax(res))



if __name__ == '__main__':
    ge = Paint()
