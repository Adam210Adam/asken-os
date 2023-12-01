# Terms
# PID: Service number
# SRV: Service
# Palaxe: Firmware

from tkinter import * # Graphics import
from PIL import ImageTk, Image
import time
import random
import os
import importlib
import datetime
import math
import hashlib
import calendar
def configure_ax(nameofedit: str):

    edit = Tk()
    edit.geometry("400x200")
    Label(edit, text=nameofedit, font=("Ubuntu", 10)).place(x=10,y=10)
    hey = Text(edit, width=200,height=4)
    hey.insert(1.0, open(f"{nameofedit}.opt", "r").readlines()[0])
    hey.place(x=10,y=100)
    def Save():
        virtualization = hey.get(1.0, "end-1c")
        with open(f"{nameofedit}.opt", "w") as file:
            file.write(f"{virtualization}")
    Button(edit, text="Save", command=Save).pack()
    edit.mainloop()

def systemcontrolVirtualization(root: Tk):
    root.destroy()
    newRoot1 = Tk()
    newRoot1.state("zoomed")
    Label(newRoot1, text="Palaxe", font=("Ubuntu", 20)).place(x=10,y=10)
    Button(newRoot1, text="Virtualization,VT", command=lambda: configure_ax("VIRTUALIZATION AND VT")).place(x=10, y=100)
    newRoot1.mainloop()
def systemcontrol_Customization(root: Tk):
    root.destroy()
    newRoot1 = Tk()
    newRoot1.state("zoomed")
    Label(newRoot1, text="Palaxe", font=("Ubuntu", 20)).place(x=10,y=10)
    Button(newRoot1, text="Vs code", command=lambda: configure_ax("VS CODE")).place(x=10, y=100)
    newRoot1.mainloop()
def openPalexe(root: Tk):
    root.destroy()
    newRoot = Tk()
    newRoot.state("zoomed")
    system_image = ImageTk.PhotoImage(Image.open("systemcontrol.png"))
    custom_image = ImageTk.PhotoImage(Image.open("customization1.png"))
    Label(newRoot, text="Palaxe", font=("Ubuntu", 20)).place(x=10,y=10)
    systemControl = Button(newRoot, image=system_image, command=lambda: systemcontrolVirtualization(newRoot)).place(x=10,y=100)
    customization = Button(newRoot, image=custom_image, command=lambda: systemcontrol_Customization(newRoot)).place(x=500,y=100)
    newRoot.mainloop()
root_ = Tk()
root_.state("zoomed")
root_.configure(bg="black")
icon_image = ImageTk.PhotoImage(Image.open("icon.png"))
loading_image = ImageTk.PhotoImage(Image.open("loading.gif"))
panel1 = Label(image=icon_image).pack()
openPalaxeButton = Button(text="Open Palaxe", padx=50, pady=10, fg="blue", borderwidth=1, command=lambda: openPalexe(root_)).pack(expand=True)
root_.mainloop()