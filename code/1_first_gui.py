""" simple label widget
1.) you have to define and create a thing
2.) you have to put it on screen
"""
from tkinter import *  #import tkinter

root = Tk() #this has to be called first
root.title("Python tkinter GUI")

# Disable resizing
root.resizable(False, False)
#we created a label widget
myLabel = Label(root, text="hello world!")

#we pack a widget and shove it on to the screen
myLabel.pack() #pack is the minimum automatic size of the widget
                #pack is good for simple things

#put it in front of other windows, but not for all the time
#root.attributes("-topmost", True)
#root.lift()
#root.attributes('-topmost',True)
#root.after_idle(root.attributes,'-topmost',False)

#root.attributes('-topmost', True)
#root.update()
#root.attributes('-topmost', False)

#now we create a loop where everything happens
root.mainloop()