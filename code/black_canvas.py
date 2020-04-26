# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:16:26 2020

@author: crtjur
"""

import tkinter as tk

#-------------our snake class is our canvas----
#because there will be a lot of stuff in canvas we create our class

class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600,height=620,background="black",highlightthickness=0)
        
        
#----------------------------------------------
root = tk.Tk() #creates our main window


#----------------------------------------------
root.title("snake") #window name
root.resizable(False,False) #not resizable

board = Snake()
board.pack() #we put canvas into window


#----------------------------------------------
root.mainloop() #this runs main loop