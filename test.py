#!/usr/bin/python

import Tkinter as tk
from time import *

window = tk.Tk()
window.title("Espresso")
window.attributes("-fullscreen", True)
window.config(cursor='none')


def exitProgram():
    window.quit()


def updateTime():
    topBar.config(text=strftime('%H:%M', localtime()))


topBar = tk.Label(window, width=0, height=0, takefocus=0)
topBar.grid(row=0, column=0, sticky=tk.W)
timeButton = tk.Button(window, text='update', command=updateTime, height=2, width=12)
timeButton.grid(row=1, column=0, sticky=tk.S)
exitButton = tk.Button(window, text='exit', command=exitProgram, height=2, width=12)
exitButton.grid(row=1, column=1, sticky=tk.S)

tk.mainloop()
