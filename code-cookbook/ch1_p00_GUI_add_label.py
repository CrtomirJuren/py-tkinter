# Imports
import tkinter as tk
from tkinter import ttk

# create instance
win = tk.Tk()

# set title
win.title("Python GUI")
# set size
win.geometry("300x300")

# Add label
a_label = ttk.Label(win, text="A label text")
a_label.grid(column=0, row=0)

# Button click event function
def click_me():
	action.configure(text = "i have been clicked!")
	a_label.configure(foreground = "red")
	a_label.configure(text = "a red label")

# adding a button
action = ttk.Button(win, text = "click me!", command = click_me )
action.grid(column = 1, row = 0)

# Start
win.mainloop()