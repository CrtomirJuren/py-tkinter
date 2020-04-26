# Imports
import tkinter as tk
from tkinter import ttk

# create instance
win = tk.Tk()

# set title
win.title("Python GUI")

# set size
#win.geometry("300x300")

# make Esc to exit program
win.bind('<Escape>', lambda exit_tkinter: win.destroy())

class button_cluster(object):
	"""docstring for button_cluster
	Behaviour
	- switch
	- latch

	Mechanical action
	- when_pressed
	- when_released
	- until_released
	"""
	def __init__(self, win,
		column = 0,
		row = 0,
		name_frame = "",
		name_button = "",
		name_label = "",
		behaviour = "latch",
		mech_action = "when_pressed"):

		super (button_cluster, self).__init__()
		self.win = win
		self.column = column
		self.row = row

		self.name_frame = name_frame
		self.name_button = name_button
		self.name_label = name_label

		self.behaviour = behaviour
		self.mech_action = mech_action

		self.state = True
		self.state_new = True

		# create embedded frame
		embedded = ttk.LabelFrame(self.win, text = self.name_frame)

		# create label
		self.label = ttk.Label(embedded, text = self.name_label)

		# create button
		self.button = ttk.Button(embedded,
					takefocus = False) # text = self.name_button, command = self._button_press,

		# create led
		#self.led = tk.Canvas(embedded, height=21, width=21)	# bg='SystemButtonFace'
		#self.led.create_oval(1, 1, 20, 20, fill ="green", outline="black")
		self.canvas = tk.Canvas(embedded, height=21, width=21)
		self.led =self.canvas.create_oval(1, 1, 20, 20)
		self.canvas.itemconfigure(self.led, fill='green')

		# put in emmbeded frame
		self.label.grid(column = 0,row = 0, padx = 5, pady = 5)
		self.button.grid(column = 1, row = 0, padx = 5, pady = 5) #, padx = 10, pady = 10
		self.canvas.grid(column = 2, row = 0, padx = 5, pady = 5)
		#self.led.grid(column = 2, row = 0, padx = 5, pady = 5)
		# put embedded frame on grid
		embedded.grid(column = self.column, row = self.row, padx = 5) #, pady = 2

		self.button.bind('<ButtonPress-1>', self._button_press)
		self.button.bind('<ButtonRelease-1>', self._button_release)

	def _button_press(self, *args):
		print(self.name_button + " " + "_button_press")
		self.state_new = True
		self._button_logic(self.state_new)

	def _button_release(self, *args):
		print(self.name_button + " " + "_button_release")
		self.state_new = False
		self._button_logic(self.state_new)

	def _button_enter(self, *args):
		pass

	def _button_logic(self, state):
		# button is considered pressed only at transition
		if self.state_new:
			self.state = not self.state
			print(self.state)
			print("pressed")
			if self.state:
				#print("transition to ON")
				self.canvas.itemconfigure(self.led, fill='green')
			else:
				#print("transition to OFF")
				self.canvas.itemconfigure(self.led, fill='red')

button1 = button_cluster(win,
	column = 0,
	row = 0,
	name_frame = "frame 1",
	name_button = "button 1",
	name_label = "button 1",
	behaviour = "latch",
	mech_action = "when_pressed")

button2 = button_cluster(win,
	column = 0,
	row = 1,
	name_frame = "frame 2",
	name_button = "button 2",
	name_label = "button 2",
	behaviour = "latch",
	mech_action = "when_pressed")

button3 = button_cluster(win,
	column = 0,
	row = 2,
	name_frame = "frame 3",
	name_button = "button 3",
	name_label = "button 3",
	behaviour = "latch",
	mech_action = "when_pressed")

#3.1)put it in front of other windows, but not for all the time
win.attributes("-topmost", True)
win.lift()
win.attributes('-topmost',True)
win.after_idle(win.attributes,'-topmost',False)

#3.2)now we create a loop where everything happens
win.mainloop()

