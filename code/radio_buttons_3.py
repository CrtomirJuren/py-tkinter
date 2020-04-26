'''
	All "connected" Radiobuttons should have the same variable value; 
	in this way, you can call theVariable.get() and compare that with 
	the value of each Radiobutton; you shouldn't need a reference to 
	every Radiobutton; nor should you have a StringVar for each Radiobutton,
	only each line.
'''

import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def ShowChoice():
    print(v.get())

tk.Label(root, 
         text="""Choose your favourite 
programming language:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root, 
                  text=language,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)


root.mainloop()