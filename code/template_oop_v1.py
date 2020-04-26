# from tkinter import * --> avoid wildcard imports
import tkinter as tk
from tkinter import ttk

from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep

class Navbar(tk.Frame): ...
class Toolbar(tk.Frame): ...
class Statusbar(tk.Frame): ...
class Main(tk.Frame): ...

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.statusbar = Statusbar(self, ...)
        self.toolbar = Toolbar(self, ...)
        self.navbar = Navbar(self, ...)
        self.main = Main(self, ...)

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

