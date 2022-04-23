from tkinter import *
from PIL import ImageTk , Image
import time
win = Tk()
win.title(None)
win.geometry('80x75+1400+700')

#canvas
canvas = Canvas(win , width = 80 , height=75)
canvas.pack()

#animate
img = ImageTk.PhotoImage(Image.open("mic1.jpg"))
canvas.create_image(1,1,anchor=NW,image=img)
#win.wm_attributes('-topmost','True')

##only on windows
win.wm_attributes('-toolwindow','True')
win.mainloop()
