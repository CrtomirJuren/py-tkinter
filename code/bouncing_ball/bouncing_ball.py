# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:06:52 2020

@author: crtjur
"""

import tkinter
import time


#initialize tkinter
tk = tkinter.Tk()

#1. create canvas
canvas = tkinter.Canvas(tk, width=300,height=400)
canvas.grid()

#2. draw a ball
ball = canvas.create_oval(5,5,60,60,fill="blue") #(left,top,right,bottom)

#speed of moving the ball
x = 1
y = 1

#3. move ball
while True:
    canvas.move(ball,x,y)
    pos = canvas.coords(ball)

    #LEFT SIDE - change x direction
    if pos[0] <= 0:
        x=-x
    #TOP - change y direction 
    if pos[1] <= 0:
        y=-y
    #RIGHT - change x direction    
    if pos[2] >= 300:
        x=-x
    #BOTTOM - change y direction
    if pos[3] >= 400:
        y=-y
    
    tk.update()
    time.sleep(0.01)
    pass
        
#-------start running tkinter------
tk.mainloop()