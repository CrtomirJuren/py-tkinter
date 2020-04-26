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
	action.configure(text = "Hello " + number.get())

# adding a text box ENTRY widget
name = tk.StringVar()	# create a string variable
name_entered = ttk.Entry(win, width=12, textvariable=name) # bound string variable to Entry widget

# adding a button
action = ttk.Button(win, text = "click me!", command = click_me )

# Add label
label = ttk.Label(win, text="Enter a name")

# adding combo box
combobox_label = ttk.Label(win, text="Choose a number: ")
number = tk.StringVar()
number_choosen = ttk.Combobox(win, width=12,textvariable=number, state ="readonly")
number_choosen["values"] = (1,2,4,42,100)
number_choosen.current(0)

# building up the grid and positioning
# First row
label.grid(column=0, row=0)
combobox_label.grid(column=1,row=0)
# second row
name_entered.grid(column = 0, row = 1)
number_choosen.grid(column=1, row=1)
action.grid(column = 1, row = 3)

# set focus to entry
name_entered.focus()

# disable button widget
#action.configure(state = "disabled")

# Start
win.mainloop()