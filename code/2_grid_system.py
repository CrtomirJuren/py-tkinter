# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

tkinter
1.) you have to define and create a thing
2.) you have to put it on screen
"""
from tkinter import *  #import tkinter

root = Tk() #this has to be called first

 #we created a label widget
myLabel1 = Label(root, text="hello world!")
myLabel2 = Label(root, text="My name is Crtomir!")

 #we pack a widget and shove it on to the screen
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)
       

#put it in front of other windows, but not for all the time
root.attributes("-topmost", True)
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

#now we create a loop where everything happens
root.mainloop()