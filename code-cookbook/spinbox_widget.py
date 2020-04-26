#-------------------------------------------------------------------
#--------------------imports---------------------------------
#-------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox

#-------------------------------------------------------------------
#--------------------INITIALIZATION---------------------------------
#-------------------------------------------------------------------
# create instance
win = tk.Tk()
# make Esc to exit program
win.bind('<Escape>', lambda exit_tkinter: win.destroy())
# set title
win.title("Spinbox widgets")

#-------------------------------------------------------------------
#----------------------SPINBOX WIDGET-------------------------------
#-------------------------------------------------------------------
spin1 = Spinbox(win, from_=0, to=10, width=5, bd=8) #default: SUNKEN
spin2 = Spinbox(win, from_=0, to=10, width=5, bd=8, relief=tk.FLAT)
spin3 = Spinbox(win, from_=0, to=10, width=5, bd=8, relief=tk.RAISED)
spin4 = Spinbox(win, from_=0, to=10, width=5, bd=8, relief=tk.GROOVE)
spin5 = Spinbox(win, from_=0, to=10, width=5, bd=8, relief=tk.RIDGE)

spin1.grid(column=0, row=0)
spin2.grid(column=1, row=0)
spin3.grid(column=2, row=0)
spin4.grid(column=3, row=0)
spin5.grid(column=4, row=0)

#-------------------------------------------------------------------
#---------------------------START GUI-------------------------------
#-------------------------------------------------------------------
win.mainloop()