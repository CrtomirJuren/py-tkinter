import os
from tkinter import *

#initialize tinker
root = Tk()

#get icon path
script_path = os.getcwd() #get the script file's directory location
#icon_path= script_path + '\py_icon.ico'
#set as window icon
#root.iconbitmap(icon_path)

root.title('dropdown example')
root.geometry('400x400')

#create drop down box
def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday'
    ]

clicked = StringVar()
clicked.set(options[0]) #set first options to default value

myButton = Button(root, text='show selection').pack()

drop = OptionMenu(root,clicked,*options) #pointer to optins
drop.pack()

#main loop
root.mainloop()
