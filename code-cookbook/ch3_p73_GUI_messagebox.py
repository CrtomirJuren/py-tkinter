# Imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

# create instance
win = tk.Tk()

# make Esc to exit program
win.bind('<Escape>', lambda exit_tkinter: win.destroy())

# set title
win.title("Python GUI")
# set size
# win.geometry("300x300")

#-----------------tab control----------------------------------------------------------
tabControl = ttk.Notebook(win)	# create tab control

tab1 = ttk.Frame(tabControl)	#create a tab 1
tab2 = ttk.Frame(tabControl)	#create a tab 2

tabControl.add(tab1, text="Tab 1") #add the tab
tabControl.add(tab2, text="Tab 2") #add the tab

tabControl.pack(expand=1, fill="both")#pack to make visible
#---------------------------------------------------------------------------
#----------embed frame------------
mighty = ttk.LabelFrame(tab1, text = " Embedded Frame stuff")
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
check1 = tk.Checkbutton(tab2, text="disabled", variable=chVarDis, state="disabled")
check1.select()

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(tab2, text="UnChecked", variable=chVarUn)
check2.deselect()

chVarEn = tk.IntVar()
check3 = ttk.Checkbutton(tab2, text="Enabled", variable=chVarEn)
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
	rad = ttk.Radiobutton(tab2, text=colors[col], variable=radVar, value=col, command=radCall)
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

#---------create a container to hold labels----------
buttons_frame = ttk.LabelFrame(tab2, text="labels in a frame")
buttons_frame.grid(column=0, row=7, padx=0, pady=20)

# place labels into the container element
ttk.Label(buttons_frame, text="label1").grid(column=0, row=0)
ttk.Label(buttons_frame, text="label2").grid(column=1, row=0)
ttk.Label(buttons_frame, text="label3").grid(column=2, row=0)

for child in buttons_frame.winfo_children():
	child.grid_configure(padx=8, pady=4)

#-------------------menu bar---------------------------

def _quit():
	win.quit()
	win.destroy()
	exit()

def _normal_msgBox():
	msg.showinfo("Python Normal Message","A Python GUI using tkinter: \nThe year is 2020.")
def _warning_msgBox():
	msg.showwarning("Python Warning Message","A Python GUI using tkinter: \nThe year is 2020.\nWarning: There might be a bug in your code.")
def _error_msgBox():
	msg.showerror("Python Error Message","A Python GUI using tkinter: \nThe year is 2020.\nError: Huston we have a problem.")
def _multichoice_msgBox():
	answer = msg.askyesnocancel("Python Multi Choice Message","Are you sure ?")
	print(f"{answer}")
	if answer == None:
		return
	if answer == True:
		print("user sayed yes :)")
	else:
		print("user sayed no :(")

# creating a menu bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# create menu and add menu items
file_menu = Menu(menu_bar, tearoff=0) # remove default dashed line separator
help_menu = Menu(menu_bar, tearoff = 0)

# create dropdown menus
menu_bar.add_cascade(label="File", menu = file_menu)
menu_bar.add_cascade(label ="Help", menu = help_menu)

# add commands to file menu
file_menu.add_command(label = "New")
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = _quit)

# add commands to Help menu
help_menu.add_command(label="normal_msg", command=_normal_msgBox) # display msgbox when called
help_menu.add_command(label="warning_msg", command=_warning_msgBox) # display msgbox when called
help_menu.add_command(label="error_msg", command=_error_msgBox) # display msgbox when called
help_menu.add_command(label="multichoice_msg", command=_multichoice_msgBox) # display msgbox when called
#--------------------message box---------------------------

# add another menu to the menu bar and an item

#-------------out focus on selected control---------
name_entered.focus()
#---------START GUI-------------
win.mainloop()







