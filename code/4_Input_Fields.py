# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

tkinter
1.) you have to define and create a thing
2.) you have to put it on screen
"""
from tkinter import *  #import tkinter

#---------------------1. create main root------------------------------------
root = Tk() #this has to be called first

root.title("Simple calculator") #give window a name

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0,columnspan=3,padx=10,pady=10) #spans over 3 columns

e.pack()
e.insert(0,"enter your name: ")

#-------------------------define buttons--------------------------------------
    
button_1 = Button(root, text = "1",padx=40, pady=40, command = button_1_cmd)



#--------------------put buttons on the screen---------------------------------
#myButton.pack()
button_1.grid(row=3,column=0)


#-------------------------RUN APPLICATION--------------------------------------
#put it in front of other windows, but not for all the time
root.attributes("-topmost", True)
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

#now we create a loop where everything happens
root.mainloop()















"""
 #we created a label widget
myLabel1 = Label(root, text="hello world!")
myLabel2 = Label(root, text="My name is Crtomir!")

 #we pack a widget and shove it on to the screen
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)
       
def myClick():
    greeting_var = "hello " + e.get()
    myLabel = Label(root, text = greeting_var)
    myLabel.pack()

"""