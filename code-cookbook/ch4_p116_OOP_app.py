
"""Summary

Attributes:
    oop (TYPE): Description
"""
#------------------------------------------------------------
#--------------------imports---------------------------------
#------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep

import __init__
#from folder2_hello import *
from folder2_hello import folder2_hello_function
folder2_hello_function()
#------------------------------------------------------------
#--------------- application class----------------------------
#------------------------------------------------------------
class OOP():

	"""Summary

	Attributes:
	    action (TYPE): Description
	    name (TYPE): Description
	    win (TYPE): Description
	"""

	def __init__(self):
		"""Initializer method
		"""
		self.win = tk.Tk()# Create instance
		self.win.title("Python GUI")# Add a title
		# win.geometry("300x300") # set size
		self.win.iconbitmap("python.ico") # set icon
		self.win.resizable(0,0)# Disable resizing the GUI
		self.create_widgets()

	def _btn1_callback(self):
		"""Button callback
		"""
		self.btn1.configure(text='Hello '+ self.number.get())

	def _spinbox_callback(self):
		"""Spinbox callback
		"""
		self.value = self.spinbox.get()
		print(self.value)
		#scr.insert(tk.INSERT, value + '\n')

	def radiobtn_call(self):
		"""radio buttons callback function
		"""
		radSel = self.radVar.get()
		if radSel == 0:
			self.win.configure(background = self.colors[0])
		if radSel == 1:
				self.win.configure(background = self.colors[1])
		if radSel == 2:
			self.win.configure(background = self.colors[2])

	def _create_embed_frame_1(self):
		#----------embeded frame 1------------
		self.embed_frame_1 = ttk.LabelFrame(self.tab1, text = " Embedded Frame 1")
		self.embed_frame_1.grid(column=0,row=0,padx=8,pady=4)

		#----------embedded frame 1 widgets------------
		# entry text box widget + label
		self.name = tk.StringVar()	# create a string variable

		self.name_input_lbl = ttk.Label(self.embed_frame_1, text="Enter a name: ")
		self.name_input = ttk.Entry(self.embed_frame_1, width=12, textvariable=self.name) # bound string variable to Entry widget

		# button 1 control
		self.btn1_lbl = ttk.Button(self.embed_frame_1, text = "button1 event", command = self._btn1_callback)
		self.btn1 = ttk.Label(self.embed_frame_1, text="Enter a name")

		# combo box control		self.number = tk.StringVar()
		self.number = tk.StringVar()
		self.combobox_lbl = ttk.Label(self.embed_frame_1, text="Choose a number: ")
		self.combobox = ttk.Combobox(
			self.embed_frame_1,
			width=12,
			textvariable = self.number,
			state ="readonly")
		self.combobox["values"] = (1,2,4,42,100)
		self.combobox.current(0)

		#-------------------------------------------------------------------
		#--------------------------Spinbox widget---------------------------
		#-------------------------------------------------------------------
		self.spinbox_lbl = ttk.Label(self.embed_frame_1, text="Spinbox control: ")
		self.spinbox = Spinbox(self.embed_frame_1, from_=0, to=10, width=5, bd=8, command = self._spinbox_callback, relief=tk.SUNKEN) #

		#-------------------------------------------------------------------
		#-----------------------SCROLLED TEXT-------------------------------
		#-------------------------------------------------------------------
		self.scroll_w = 50
		self.scroll_h = 10
		self.scroll = scrolledtext.ScrolledText(self.embed_frame_1, width=self.scroll_w, height=self.scroll_h, wrap=tk.WORD)

		#--------------grid positions---------------------------
		self.name_input_lbl.grid(column=0, row=0)
		self.name_input.grid(column=1, row=0)

		self.combobox_lbl.grid(column = 0, row = 1)
		self.combobox.grid(column = 1, row = 1)

		self.spinbox_lbl.grid(column=0, row=2)
		self.spinbox.grid(column=1, row=2)

		self.btn1_lbl.grid(column=0,row=3)
		self.btn1.grid(column=1,row=3)

		self.scroll.grid(column=0,row=4, columnspan = 2)

	def _create_embed_frame_2(self):
		#----------embeded frame 2------------
		self.embed_frame_2 = ttk.LabelFrame(self.tab2, text = " Embedded Frame 2")
		self.embed_frame_2.grid(column=0,row=0,padx=8,pady=4)
		#-------------------------------------------------------------------
		#---------------------CHECK BUTTONS---------------------------------
		#-------------------------------------------------------------------
		self.checkbtn1Var = tk.IntVar()
		self.checkbtn1 = tk.Checkbutton(self.embed_frame_2, text="checkbtn1", variable=self.checkbtn1Var)

		self.checkbtn2Var = tk.IntVar()
		self.checkbtn2 = tk.Checkbutton(self.embed_frame_2, text="checkbtn2", variable=self.checkbtn2Var)

		self.checkbtn3Var = tk.IntVar()
		self.checkbtn3 = tk.Checkbutton(self.embed_frame_2, text="checkbtn3", variable=self.checkbtn3Var)

		#---------------RADIO BUTTONS-----------------------

		self.colors = ["blue", "gold", "red"]
		# create three radiobuttons using one variable
		self.radVar = tk.IntVar()
		self.radVar.set(99)	#unselect
		for col in range(3):
			self.rad = ttk.Radiobutton(
				self.embed_frame_2,
				text=self.colors[col],
				variable=self.radVar,
				value=col,
				command=self.radiobtn_call)
			self.rad.grid(column = col, row = 2, sticky = tk.W, columnspan = 3)

		#--------------grid positions---------------------------

		self.checkbtn1.grid(column = 0, row = 0, sticky = tk.W)
		self.checkbtn2.grid(column = 1, row = 0, sticky = tk.W)
		self.checkbtn3.grid(column = 2, row = 0, sticky = tk.W)

	def _create_tabs(self):
		#-------------------Tab Control----------------------
		self.tabControl = ttk.Notebook(self.win)

		self.tab1 = ttk.Frame(self.tabControl) # Create a tab
		self.tabControl.add(self.tab1, text='Tab 1') # Add the tab

		self.tab2 = ttk.Frame(self.tabControl) # Create second tab
		self.tabControl.add(self.tab2, text='Tab 2') # Add second tab

		self.tabControl.pack(expand=1, fill="both")# Pack to make visible

	def _quit_event(self):
		self.win.quit()
		self.win.destroy()
		exit()

	def _normal_msgBox(self):
		msg.showinfo("Python Normal Message","A Python GUI using tkinter: \nThe year is 2020.")
	def _warning_msgBox(self):
		msg.showwarning("Python Warning Message","A Python GUI using tkinter: \nThe year is 2020.\nWarning: There might be a bug in your code.")
	def _error_msgBox(self):
		msg.showerror("Python Error Message","A Python GUI using tkinter: \nThe year is 2020.\nError: Huston we have a problem.")
	def _multichoice_msgBox(self):
		answer = msg.askyesnocancel("Python Multi Choice Message","Are you sure ?")
		print(f"{answer}")
		if answer == None:
			return
		if answer == True:
			print("user sayed yes :)")
		else:
			print("user sayed no :(")
	def _create_menu(self):
		"""menu
		"""
		# creating a menu bar
		self.menu_bar = Menu(self.win)
		self.win.config(menu=self.menu_bar)

		# create menu and add menu items
		self.file_menu = Menu(self.menu_bar, tearoff=0) # remove default dashed line separator
		self.help_menu = Menu(self.menu_bar, tearoff = 0)

		# create dropdown menus
		self.menu_bar.add_cascade(label="File", menu = self.file_menu)
		self.menu_bar.add_cascade(label ="Help", menu = self.help_menu)

		# add commands to file menu
		self.file_menu.add_command(label = "New")
		self.file_menu.add_separator()
		self.file_menu.add_command(label = "Exit", command = self._quit_event)

		# add commands to Help menu
		self.help_menu.add_command(label="normal_msg", command = self._normal_msgBox) # display msgbox when called
		self.help_menu.add_command(label="warning_msg", command = self._warning_msgBox) # display msgbox when called
		self.help_menu.add_command(label="error_msg", command = self._error_msgBox) # display msgbox when called
		self.help_menu.add_command(label="multichoice_msg", command = self._multichoice_msgBox) # display msgbox when called

	def create_widgets(self):
		"""create widgets
		"""
		self._create_menu()
		self._create_tabs()
		#------------------------Tab 1 Controls----------------------
		self._create_embed_frame_1()
		self._create_embed_frame_2()
		#------------------------Tab 2 Controls----------------------

#======================
# Start GUI
#======================
oop = OOP() # create an instance of the class
# use instance variable to call mainloop via win
oop.win.mainloop()