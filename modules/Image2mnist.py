from PIL import ImageFilter
from PIL import Image
import os
from modules.nn import NeuralNetwork
def imageprepare(argv):
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
        wtop = int(round(((32 - nheight) / 2), 0))  # calculate horizontal position
        newImage.paste(img, (4, wtop))  # paste resized image on white canvas
    else:
        # Height is bigger. Heigth becomes 20 pixels.
        nwidth = int(round((20.0 / height * width), 0))  # resize width according to ratio height
        if (nwidth == 0):  # rare case but minimum is 1 pixel
            nwidth = 1
            # resize and sharpen
        img = im.resize((nwidth, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((32 - nwidth) / 2), 0))  # caculate vertical pozition
        newImage.paste(img, (wleft, 4))  # paste resized image on white canvas

    newImage.save("sample.png")

    tv = list(newImage.getdata())  # get pixel values

    # normalize pixels to 0 and 1. 0 is pure black, 1 is pure white.
    # return tv
    tva = [x * 0.99 / 255.0 + 0.01 for x in tv]
    return tva

print(os.getcwd())
res= imageprepare("/home/ccr/PycharmProjects/Tkinter/modules/images/inverted8.png")
print(res)


'''
input_nodes = 1024
hidden_nodes = 100
output_nodes = 10

# learning rate is 0.3
learning_rate = 0.3

# create instance of neural network
n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes,
                  learning_rate)
n.preare_to_train()
n.imageprepare()
'''