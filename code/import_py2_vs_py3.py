try:
    # for Python2
    import Tkinter as tk
    import ScrolledText as tkst
except ImportError:
    # for Python3
    import tkinter as tk
    import tkinter.scrolledtext as tkst