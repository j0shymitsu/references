import tkinter as tk
from tkinter import font as tkfont

root = tk.Tk()

available_fonts = tkfont.families()

for font in available_fonts:
    print(font)