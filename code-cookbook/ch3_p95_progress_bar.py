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

#from tkinter import Progressbar
#-------------------------------------------------------------------
#--------------------INITIALIZATION---------------------------------
#-------------------------------------------------------------------
# create instance
win = tk.Tk()
# make Esc to exit program
win.bind('<Escape>', lambda exit_tkinter: win.destroy())
# set title
win.title("Progress bar")

#-------------------------------------------------------------------
#----------------------SPINBOX WIDGET-------------------------------
#-------------------------------------------------------------------
# progress bar functions
# update progress bar in a callback loop
def run_progressbar():
	progress_bar["maximum"] = 100
	for i in range(101):
		time.sleep(0.01)
		progress_bar["value"] = i
		progress_bar.update()
	progress_bar["value"] = 0

def start_progressbar():
	pass

def stop_progressbar():
	progress_bar.stop()

def stopafter_progressbar(wait_ms=1000):
	win.after(wait_ms, progress_bar.stop)
	pass

# create frame for buttons
buttons_frame = ttk.LabelFrame(win, text="Progres Bar Control")
buttons_frame.grid(column=0, row=0, padx=0, pady=20)

# Add buttons for progress bar control
ttk.Button(buttons_frame, text = "Run", command=run_progressbar).grid(column=0, row=0, sticky = "W, E")
ttk.Button(buttons_frame, text = "Start", command=start_progressbar).grid(column=0, row=1, sticky = "W, E")
ttk.Button(buttons_frame, text = "Stop Immediately", command=stop_progressbar).grid(column=0, row=2, sticky = "W, E")
ttk.Button(buttons_frame, text = "Stop Graduately", command=stopafter_progressbar).grid(column=0, row=3, sticky = "W, E")

# add progress bar
progress_bar = ttk.Progressbar(win, orient="horizontal", length=286, mode="determinate")
progress_bar.grid(column=0, row=4, pady=2)

#-------------------------------------------------------------------
#---------------------------START GUI-------------------------------
#-------------------------------------------------------------------
win.mainloop()