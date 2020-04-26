# Imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# create instance
win = tk.Tk()

# make Esc to exit program
win.bind('<Escape>', lambda exit_tkinter: win.destroy())

# set title
win.title("Python GUI")
# set size
# win.geometry("300x300")

#----------embed frame------------
mighty = ttk.LabelFrame(win, text = " Embedded Frame stuff")
mighty.grid(column=0,row=0,padx=8,pady=4)

#--------------------------------

# Button click event function
def click_me():
	action.configure(text = "Hello " + number.get())

# adding a text box ENTRY widget
name = tk.StringVar()	# create a string variable
name_entered = ttk.Entry(mighty, width=12, textvariable=name) # bound string variable to Entry widget

# adding a button
action = ttk.Button(mighty, text = "click me!", command = click_me )

# Add label
label = ttk.Label(mighty, text="Enter a name")

# adding combo box
combobox_label = ttk.Label(mighty, text="Choose a number: ")
number = tk.StringVar()
number_choosen = ttk.Combobox(mighty, width=12,textvariable=number, state ="readonly")
number_choosen["values"] = (1,2,4,42,100)
number_choosen.current(0)

#----------------checkbuttons-------------
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text="disabled", variable=chVarDis, state="disabled")
check1.select()

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text="UnChecked", variable=chVarUn)
check2.deselect()

chVarEn = tk.IntVar()
check3 = ttk.Checkbutton(mighty, text="Enabled", variable=chVarEn)
#check3.select()
#----------------radiobuttons-------------
colors = ["blue", "gold", "red"]

#radiobutton callback
def radCall():
	radSel = radVar.get()
	if radSel == 0:
		win.configure(background = colors[0])
	if radSel == 1:
		win.configure(background = colors[1])
	if radSel == 2:
		win.configure(background = colors[2])

# create three radiobuttons using one variable
radVar = tk.IntVar()
radVar.set(99)
for col in range(3):
	rad = ttk.Radiobutton(mighty, text=colors[col], variable=radVar, value=col, command=radCall)
	rad.grid(column = col, row = 5, sticky = tk.W, columnspan = 3)

#----scrolled text--------------
scroll_w = 30
scroll_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scroll_w, height=scroll_h, wrap=tk.WORD)


#---------------grid positions--------------
# building up the grid and positioning
# First row
label.grid(column=0, row=0)
combobox_label.grid(column=1,row=0)
# second row
name_entered.grid(column = 0, row = 1)
number_choosen.grid(column=1, row=1)
#
action.grid(column = 2, row = 1)
#4 row
check1.grid(column = 0, row = 4, sticky = tk.W)
check2.grid(column = 1, row = 4, sticky = tk.W)
check3.grid(column = 2, row = 4, sticky = tk.W)
#5 row
scr.grid(column=0, columnspan=3)

#---------create a container to hold labels
buttons_frame = ttk.LabelFrame(mighty, text="labels in a frame")
buttons_frame.grid(column=0, row=7, padx=0, pady=20)

# place labels into the container element
ttk.Label(buttons_frame, text="label1").grid(column=0, row=0)
ttk.Label(buttons_frame, text="label2").grid(column=1, row=0)
ttk.Label(buttons_frame, text="label3").grid(column=2, row=0)

for child in buttons_frame.winfo_children():
	child.grid_configure(padx=8, pady=4)



name_entered.focus()
# Start
win.mainloop()







