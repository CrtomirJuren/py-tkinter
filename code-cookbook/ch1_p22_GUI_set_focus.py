# Imports
import tkinter as tk
from tkinter import ttk

# create instance
win = tk.Tk()

# set title
win.title("Python GUI")
# set size
#win.geometry("300x300")

# Button click event function
def click_me():
	action.configure(text = "Hello " + name.get())

# Add label
label = ttk.Label(win, text="Enter a name")
label.grid(column=0, row=0)

# adding a text box ENTRY widget
name = tk.StringVar()	# create a string variable
name_entered = ttk.Entry(win, width=12, textvariable=name) # bound string variable to Entry widget
name_entered.grid(column = 1, row = 0)
# adding a button
action = ttk.Button(win, text = "click me!", command = click_me )
action.grid(column = 0, row = 1)

# set focus to entry
name_entered.focus()

# disable button widget
action.configure(state = "disabled")

# Start
win.mainloop()