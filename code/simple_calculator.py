# -*- coding: utf-8 -*-
"""
Spyder Editor

Python version of windows calculator

"""
from tkinter import *  #import tkinter

#---------------------1. create main root------------------------------------
root = Tk() #this has to be called first

root.title("Simple calculator") #give window a name

e = Entry(root, width=16, borderwidth=5)
e.grid(row=0, column=0,columnspan=4,padx=5,pady=10) #spans over 3 columns
e.config(font=("Courier", 20))

#e.pack()
#e.insert(0,"enter your name: ")

#-------------------------define functions--------------------------------------
def button_click(number):
    #e.delete(0,END) #clear input screen
    current = e.get() #first read what is already on display
    e.delete(0,END) #clear input screen
    e.insert(0,str(current) + str(number)) #put number in display, change it to string
    return

#1st row-------------------------
def button_percent(): #NOT WORKING
    """
    global f_num
    print("f_num",f_num)
    second_number = float(e.get())
    print("second_number",second_number)
    percentage = f_num/100
    second_number = second_number*percentage
    e.delete(0,END) #clear input screen
    e.insert(0,second_number) #put number in display, change it to string
    """
    return
#OK
def button_CE(): #clear recent entry
    e.delete(0,END) #clear input screen
    return

def button_C(): #clear all memory
    global f_num
    f_num = 0
    e.delete(0,END) #clear input screen
    return

#deletes last input number
def button_DEL():                         
    current = e.get()                      #first read what is already on display
    current = current[:-1]                      #first read what is already on display
    e.delete(0,END)                        #clear input screen
    e.insert(0,str(current)) #put number in display, change it to string
    return

#--------2nd row-------------------

#clear recent entry
def button_reciprocal():
    number = float(e.get()) #first remember number
    number = 1/number
    e.delete(0,END) #clear input screen
    e.insert(0,number) #put number in display, change it to string
    return

def button_square(): #clear all memory
    e.delete(0,END) #clear input screen
    return

def button_sqare_root(): #deletes last input number
    e.delete(0,END) #clear input screen
    return

def button_divide():
    first_number = e.get()#first remember number
    global f_num
    global math
    math = "divide"
    f_num = float(first_number)
    e.delete(0,END) #remove old number, so we can write a new one 
    print("button divide action")
    return

#3rd row-------------------
def button_multiply():
    first_number = e.get()#first remember number
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    e.delete(0,END) #remove old number, so we can write a new one 
    print("button multiply action")
    return

#4th row-------------------
def button_subtract():
    first_number = e.get()#first remember number
    global f_num
    global math
    math = "subtract"
    f_num = float(first_number)
    e.delete(0,END) #remove old number, so we can write a new one 
    print("button subtract action")
    return

#5th row-----------------
def button_add(): #WORKING
    first_number = e.get()#first remember number
    global f_num
    global math
    math = "add"
    f_num = float(first_number)
    e.delete(0,END) #remove old number, so we can write a new one 
    print("button add action")
    print("f_num=",f_num)
    return

#6th row--------------------
def button_sign(): #deletes last input number
    number = float(e.get())#first remember number
    number = -number
    e.delete(0,END) #clear input screen
    e.insert(0,number) #put number in display, change it to string
    return

def button_decimal(): #deletes last input number
    e.delete(0,END) #clear input screen
    return

def button_equal():
    #print("hello")
    second_number = float(e.get())
    print("second_number=",second_number)
        
    e.delete(0,END)
    
    if math == "add":
        result = f_num + second_number

    if math == "subtract":
        result = f_num - second_number
        
    if math == "multiply":
        result = f_num * second_number

    if math == "divide":
        result = f_num / second_number
        
    e.insert(0,result)
    
    #print("button equal action")
    #print("f_num=",f_num)
    #print("result=",result)
    return
    
#-------------------------define buttons-------1-------------------------------
#0st row
    #text display here
    
#1st row
button_percent = Button(root, text = "%",padx=28, pady=13, command = button_percent)
button_CE = Button(root, text = "CE",padx=25, pady=13, command = button_CE) #clear recent entry
button_C = Button(root, text = "C",padx=28, pady=13, command = button_C) # clear all memory
button_DEL = Button(root, text = "DEL",padx=23, pady=13, command = button_DEL)

#2nd row
button_reciprocal = Button(root, text = "1/x",padx=25, pady=13, command = button_reciprocal)
button_square = Button(root, text = "X^2",padx=22, pady=13, command = button_CE) #clear recent entry
button_square_root = Button(root, text = "sq(x)",padx=20, pady=13, command = button_C) # clear all memory
button_divide = Button(root, text = "/",padx=30, pady=13, command = button_divide)

#3rd row
button_7 = Button(root, text = "7",padx=30, pady=13, command = lambda:button_click(7))
button_8 = Button(root, text = "8",padx=30, pady=13, command = lambda:button_click(8))
button_9 = Button(root, text = "9",padx=30, pady=13, command = lambda:button_click(9))
button_multiply = Button(root, text = "x",padx=30, pady=13, command = button_multiply)

#4th row
button_4 = Button(root, text = "4",padx=30, pady=13, command = lambda:button_click(4))
button_5 = Button(root, text = "5",padx=30, pady=13, command = lambda:button_click(5))
button_6 = Button(root, text = "6",padx=30, pady=13, command = lambda:button_click(6))
button_subtract = Button(root, text = "-",padx=30, pady=13, command = button_subtract)

#5th row
button_1 = Button(root, text = "1",padx=30, pady=13, command = lambda:button_click(1))
button_2 = Button(root, text = "2",padx=30, pady=13, command = lambda:button_click(2))
button_3 = Button(root, text = "3",padx=30, pady=13, command = lambda:button_click(3))
button_add = Button(root, text = "+",padx=29, pady=13, command = button_add)

#6th row
button_sign = Button(root, text = "+/-",padx=24, pady=13, command = button_sign)
button_0 = Button(root, text = "0",padx=30, pady=13, command = lambda:button_click(0))
button_decimal = Button(root, text = ",",padx=30, pady=13, command = button_decimal)   
button_equal = Button(root, text = "=", padx=29, pady=13, command = button_equal)

"""


button_clear = Button(root, text = "Clear",padx=79, pady=20, command = button_clear)






"""
#--------------------put buttons on the screen---------------------------------
#1st row
button_percent.grid(row=1,column=0)
button_CE.grid(row=1,column=1)
button_C.grid(row=1,column=2)
button_DEL.grid(row=1,column=3)

#2nd row
button_reciprocal.grid(row=2,column=0)
button_square.grid(row=2,column=1)
button_square_root.grid(row=2,column=2)
button_divide.grid(row=2,column=3)
#3rd row
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_multiply.grid(row=3,column=3)

#4th row
button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)
button_subtract.grid(row=4,column=3)

#5th row
button_1.grid(row=5,column=0)
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2)
button_add.grid(row=5,column=3)

#6th row
button_sign.grid(row=6,column=0)
button_0.grid(row=6,column=1)
button_decimal.grid(row=6,column=2)
button_equal.grid(row=6,column=3)

#-------------------------RUN APPLICATION--------------------------------------
#-----1. POSITIONING THE WINDOW IN MIDDLE SCREEN-----------
w = 300 # width for the Tk root
h = 360 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#-----2. PUT IT IN FRONT OF OTHER WINDOWS-----------
#put it in front of other windows, but not for all the time
#root.attributes("-topmost", True)
root.lift()
root.attributes('-topmost',True)
#root.after_idle(root.attributes,'-topmost',False)

#---------3. MAIN LOOP-------------
#now we create a loop where everything happens
root.mainloop()

