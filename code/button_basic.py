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

# Button click event function
def Button1_call():
	print("button was pressed")
	pass

# Single Button widget
Button1 = ttk.Button(win, text="Button1", command = Button1_call) #
#Button1 = Button(root, text="Button1")
#Button1 = Button(root, text="Button1",state = DISABLED)
#Button1 = Button(root, text="Button1",padx=50,pady=50)
#Button1 = Button(root, text="Button1",padx=50,pady=50,command = Button1_call, fg="blue",bg="red")

Button1.grid(column = 0, row = 0,padx=10,pady=10)


#3.1)put it in front of other windows, but not for all the time
win.attributes("-topmost", True)
win.lift()
win.attributes('-topmost',True)
win.after_idle(win.attributes,'-topmost',False)

#3.2)now we create a loop where everything happens
win.mainloop()