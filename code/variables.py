strVar = StringVar() # Holds a string; the default value is an empty string ""
intVar = IntVar() # Holds an integer; the default value is 0
dbVar = DoubleVar() # Holds a float; the default value is 0.0
blVar = BooleanVar() # Holds a Boolean, it returns 0 for False and 1 for True

import tkinter as tk
win = tk.Tk()
# initialize variable
dbVar1 = tk.DoubleVar()
dbVar2 = tk.DoubleVar()
# set values
dbVar1.set(3.14)
dbVar2.set(1.01)
# get values
add_doubles = dbVar1.get() + dbVar2.get()
print(dbVar1) # PY_VAR0
print(dbVar2) # PY_VAR1
print(dbVar1.get()) # 3.14
print(dbVar2.get()) # 1.01
print(add_doubles) # 4.15