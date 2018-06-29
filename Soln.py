from PIL import Image, ImageTk
#from cStringIO import StringIO
#from urllib import urlopen
from tkinter import *
from PIL import Image
import tkinter as tk
import os

root = Tk()
os.chdir("/home/ccr/Documents")
'''
url = "http://www.wired.com/wp-content/uploads/2015/03/10182025tonedfull-660x441.jpg"
u = urlopen(url)
raw_data = u.read()
u.close()

'''


#image_file = Image.open(StringIO(raw_data))
image_file = Image.
photo_image = ImageTk.PhotoImage(image_file)
label = tk.Label(image=photo_image)
label.pack()
root.mainloop()