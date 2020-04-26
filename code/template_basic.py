# from tkinter import * --> avoid wildcard imports
import tkinter as tk
from tkinter import ttk

from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep

win = tk.Tk() #this has to be called first
win.title("Python tkinter GUI")
# set size
win.geometry("300x300")
# make Esc to exit program
win.bind('<Escape>', lambda exit_tkinter: win.destroy())

# Start
win.mainloop()