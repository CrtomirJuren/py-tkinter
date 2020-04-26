"""
https://www.flaticon.com
"""

# Imports
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

# create instance
win = tk.Tk()

# set title
win.title("Python GUI")

# make Esc to exit program
win.bind('<Escape>', lambda exit_tkinter: win.destroy())

# Adding widgets to the root window
label = tk.Label(win, text = 'My custom TK buttons', font =(
  'Courier', 15)) # Courier, Helvetica

# load images
btn_img_play = tk.PhotoImage(file = r"./graphics/grey_play.png").subsample(18, 18)
btn_img_pause = tk.PhotoImage(file = r"./graphics/grey_pause.png").subsample(18, 18)
btn_img_stop = tk.PhotoImage(file = r"./graphics/grey_stop.png").subsample(18, 18)
btn_img_record = tk.PhotoImage(file = r"./graphics/grey_record.png").subsample(18, 18)


# create button widgets
btn_play = tk.Button(win,
image = btn_img_play,
text = ' Play',
font =('Helvetica', 10),
compound = "left",
height=30,
width=100) #text = 'Play ',


btn_pause = tk.Button(win,
image = btn_img_pause,
text = ' Pause',
font =('Helvetica', 10),
compound = "left",
height=30,
width=100) #text = 'Play ',


btn_stop = tk.Button(win,
image = btn_img_stop,
text = ' Stop',
font =('Helvetica', 10),
compound = "left",
height=30,
width=100) #text = 'Play ',


btn_record = tk.Button(win,
image = btn_img_record,
text = ' Rec',
font =('Helvetica', 10),
compound = "left",
height=30,
width=100) #text = 'Play ',


#btn_play.config(image=btn_img_play) #, text="Click me!"
label.grid(column = 0, row = 0, columnspan = 1)

btn_play.grid(column = 0, row = 1)
btn_pause.grid(column = 0, row = 2)
btn_stop.grid(column = 0, row = 3)
btn_record.grid(column = 0, row = 4)


# start GUI
win.mainloop()