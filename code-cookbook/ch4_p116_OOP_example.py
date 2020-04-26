#-------------------------------------------------------------------
#--------------------imports---------------------------------
#-------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep

class OOP():
	def __init__(self): # Initializer method
		# Create instance
		self.win = tk.Tk()
		# Add a title
		self.win.title("Python GUI")
		self.create_widgets()

	# Button callback
	def click_me(self):
		self.action.configure(text='Hello ' + self.name.get() + ' '
		+self.number_chosen.get())
		# ... more callback methods

	def create_widgets(self):
		# Create Tab Control
		tabControl = ttk.Notebook(self.win)
		tab1 = ttk.Frame(tabControl) # Create a tab
		tabControl.add(tab1, text='Tab 1') # Add the tab
		tab2 = ttk.Frame(tabControl) # Create second tab
		tabControl.add(tab2, text='Tab 2') # Add second tab
		# Pack to make visible
		tabControl.pack(expand=1, fill="both")
		# Adding a Textbox Entry widget - using self
		self.name = tk.StringVar()
		name_entered = ttk.Entry(mighty, width=12,
		textvariable=self.name)
		name_entered.grid(column=0, row=1, sticky='W')
		# Adding a Button - using self
		self.action = ttk.Button(mighty, text="Click Me!",
		command=self.click_me)
		self.action.grid(column=2, row=1)

#======================
# Start GUI
#======================
oop = OOP() # create an instance of the class
# use instance variable to call mainloop via win
oop.win.mainloop()