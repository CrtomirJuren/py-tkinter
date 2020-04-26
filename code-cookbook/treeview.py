# Imports
import tkinter as tk
from tkinter import ttk

# create instance
win = tk.Tk()

# set title
win.title("Python GUI")

treeview = ttk.Treeview(win)

#first level items
treeview.insert("","0","folder1", text = "folder_1")
treeview.insert("","1","folder2", text = "folder_2")
treeview.insert("","end","folder3", text = "folder_3")
# show folder 1 subfiles
treeview.item("folder1", open = True)

#second level items
treeview.insert("folder1","end","sub-folder1", text = "sub-folder1")
treeview.insert("folder1","end","item1", text = "item1")

treeview.insert("folder2","end","sub-folder2", text = "sub-folder2")
treeview.insert("folder3","end","sub-folder3", text = "sub-folder3")

#third level items
treeview.insert("sub-folder1","end","subsub-folder1", text = "subsub-folder1")

treeview.grid(column = 0, row = 0)
# Start
win.mainloop()