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
label = tk.Label(win, text = 'My custom TTK buttons', font =(
  'Courier', 15)) # Courier, Helvetica

# load images
btn_img_play = tk.PhotoImage(file = r"./graphics/grey_play.png").subsample(18, 18)
btn_img_pause = tk.PhotoImage(file = r"./graphics/grey_pause.png").subsample(18, 18)
btn_img_stop = tk.PhotoImage(file = r"./graphics/grey_stop.png").subsample(18, 18)
btn_img_record = tk.PhotoImage(file = r"./graphics/grey_record.png").subsample(18, 18)

"""tk variant
btn_play = ttk.Button(win,
font =('Helvetica', 10),
image = btn_img_play,
compound = "right",
height=30,
width=100) #text = 'Play ',
"""
# create button widgets
btn_play = ttk.Button(win,
image = btn_img_play,
width = 200,
takefocus=False) #text = 'Play ',

btn_pause = ttk.Button(win,
image = btn_img_pause, 
takefocus=False,) #text = 'Pause ',

btn_stop = ttk.Button(win,
image = btn_img_stop,
takefocus=False) #text = 'Stop ',

btn_record = ttk.Button(win,
image = btn_img_record,
takefocus=False) #text = 'Record ',

#btn_play.config(image=btn_img_play) #, text="Click me!"
label.grid(column = 0, row = 0, columnspan = 1)

btn_play.grid(column = 0, row = 1, ipady=10, ipadx=10)
btn_pause.grid(column = 0, row = 2, ipady=10, ipadx=10)
btn_stop.grid(column = 0, row = 3, ipady=10, ipadx=10)
btn_record.grid(column = 0, row = 4, ipady=10, ipadx=10)


# start GUI
win.mainloop()