import tkinter as tk
from tkinter import ttk

#-----------------tkinter initialization----------------------------------------------------------
# create instance
win = tk.Tk()
# set title
win.title("Python GUI")
# make Esc to exit program, easyer code testing
win.bind('<Escape>', lambda exit_tkinter: win.destroy())

#-----------------tab control----------------------------------------------------------
tabControl = ttk.Notebook(win)	# create tab control

tab1 = ttk.Frame(tabControl)	#create a tab 1
tab2 = ttk.Frame(tabControl)	#create a tab 2

tabControl.add(tab1, text="Tab 1") #add the tab
tabControl.add(tab2, text="Tab 2") #add the tab

tabControl.pack(expand=1, fill="both")#pack to make visible
#---------------------------------------------------------------------------

#start GUI
win.mainloop()
