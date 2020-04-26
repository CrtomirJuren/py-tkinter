from tkinter import *

root = Tk()
root.geometry("300x300")

#create menu button 
mb = Menubutton(root,text = "this is a menu")
mb.menu = Menu(mb)
mb["menu"] = mb.menu


mb.menu.add_command(label="option 1", command=lambda: print("this is option 1"))
mb.menu.add_command(label="option 2", command=lambda: print("this is option 2"))
mb.menu.add_command(label="option 3", command=lambda: print("this is option 3"))

mb.pack()

root.mainloop()