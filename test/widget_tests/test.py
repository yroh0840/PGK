from tkinter import *
import os
root = Tk()
curdir = os.path.dirname(__file__)
image1 = PhotoImage(file = 'PGK/material/backgrounds_02/background_girl02.png')
image2 = PhotoImage(file = 'PGK/material/backgrounds_02/background_gori.png')
#Label(root, image = image1).pack()
canvas = Canvas(root, width=540, height=960, bg="white")
canvas.pack()
canvas.create_image(0,0,image=image1,anchor=NW)
canvas.create_image(0,400,image=image2,anchor=NW)

root.mainloop()