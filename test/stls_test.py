import tkinter as tk
import os

root = tk.Tk()
# Hide the root window drag bar and close button
root.overrideredirect(True)
# Make the root window always on top
root.wm_attributes("-topmost", True)
# Turn off the window shadow
root.wm_attributes("-transparent", True)
# Set the root window background color to a transparent color
root.config(bg='systemTransparent')

root.geometry("+300+300")

curdir = os.path.dirname(__file__) # 現在のフォルダのパス取得

# Store the PhotoImage to prevent early garbage collection
root.image = tk.PhotoImage(file= curdir+'/../material/buttons&entrywindows/girl_01_invi_circle.png')
# Display the image on a label
label = tk.Label(root, image=root.image)
# Set the label background color to a transparent color
label.config(bg='systemTransparent')
label.pack()

root.mainloop()