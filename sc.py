from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import ttk, messagebox, filedialog, Canvas, Button, Frame, Label,Tk
from typing import Sized
from PIL import ImageTk, Image


root = tk.Tk()
root.title('Lemur Scouting')
root.geometry("1280x1000")

pane = Frame (root)
pane.pack (fill=BOTH, expand=True)

#FONTS
fontbanner = font.Font(family="Calibri", size=35, weight="bold")

#IMAGES
logo = PhotoImage(file="img/Lemur-1.png")

banner = Label(pane, background="#000", image=logo)
banner.pack (side=TOP, fill=BOTH, ipady=140, padx=0)

titulo = Label(banner, text="TOTAL SCOUTING SOFTWARE", background="#000", fg="#363636", font=fontbanner)
titulo.pack (side=BOTTOM, ipady=10)







root.mainloop()