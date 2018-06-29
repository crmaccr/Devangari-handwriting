import numpy as np
import scipy.special
import os
from PIL import ImageFilter
from PIL import Image

class NeuralNetwork:

    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.innodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lrate = learningrate

        # link weight  matrices
        # wih = np.random.randn(self.hnodes, self.innodes) - 0.5
        # who = np.random.randn(self.onodes, self.hnodes)-0.5

        # a more sophisticatd weight initalisation
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.innodes))
        self.woh = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))
        # Activation function
        self.activation_function = lambda x: scipy.special.expit(x)
        return

    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = np.dot(self.woh, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        # improving  the weights
        output_errors = targets-final_outputs
        # hidden layer error is the output_errror split by weights,recombined at hidden nodes
        errors_hidden = np.dot(self.woh.T, output_errors)
        self.woh += self.lrate*np.dot(output_errors*final_outputs*(1-final_outputs), np.transpose(hidden_outputs))

        self.wih += self.lrate * np.dot(errors_hidden * hidden_outputs * (1 - hidden_outputs),
                                         np.transpose(inputs))



        pass

    def query(self, inputs_list):
        # converts input list to 2 dmin
        inputs = np.array(inputs_list, ndmin=2).T
        # query takes input from user and gives the output of neural network
        hidden_inputs = np.dot(self.wih, inputs)

        # output of hidden layer

        hidden_outputs= self.activation_function(hidden_inputs)
        # input to the final layer
        final_input = np.dot(self.woh,hidden_outputs)
        # input from the final layer
        final_output = self.activation_function(final_input)
        return final_output

    def preare_to_train(self):
        os.chdir("/home/ccr/Documents")
        # load the mnist training data CSV file into a list
        training_data_file = open("train_digit.csv", 'r')
        # training_data_file = open("testnum.csv", 'r')
        training_data_list = training_data_file.readlines()
        training_data_file.close()

        # training the neural network

        # go through all records in the training data set

        # train the neural network

        # epochs is the number of times the training data set is used for training
        epochs = 2

        for e in range(epochs):

            for record in training_data_list:
                # split the record by the ',' commas
                all_values = record.split(',')
                # scale and shift the inputs
                inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
                # create the target output values (all 0.01, except the desired  label which is 0.99)
                targets = np.zeros(self.onodes) + 0.01
                # all_values[0] is the target label for this record
                targets[int(all_values[0])] = 0.99
                self.train(inputs, targets)
                pass
            print("training done")
            pass

    def imageprepare(self,argv):
        im = Image.open(argv).convert('L')
        width = float(im.size[0])
        height = float(im.size[1])
        newImage = Image.new('L', (32, 32), "black")  # creates black canvas of 32x32 pixels
        # plt.imshow(newImage)
        # plt.show()

        if width > height:  # check which dimension is bigger
            # Width is bigger. Width becomes 20 pixels.
            nheight = int(round((20.0 / width * height), 0))  # resize height according to ratio width
            if (nheight == 0):  # rare case but minimum is 1 pixel
                nheight = 1
                # resize and sharpen
            img = im.resize((20, nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
            wtop = int(round(((28 - nheight) / 2), 0))  # calculate horizontal position
            newImage.paste(img, (4, wtop))  # paste resized image on white canvas
        else:
            # Height is bigger. Heigth becomes 20 pixels.
            nwidth = int(round((20.0 / height * width), 0))  # resize width according to ratio height
            if (nwidth == 0):  # rare case but minimum is 1 pixel
                nwidth = 1
                # resize and sharpen
            img = im.resize((nwidth, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
            wleft = int(round(((28 - nwidth) / 2), 0))  # caculate vertical pozition
            newImage.paste(img, (wleft, 4))  # paste resized image on white canvas

        newImage.save("sample.png")

        tv = list(newImage.getdata())  # get pixel values

        # normalize pixels to 0 and 1. 0 is pure black, 1 is pure white.
        # return tv
        tva = [x * 0.99 / 255.0 + 0.01 for x in tv]
        return tva


    


