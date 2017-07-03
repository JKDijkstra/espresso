#!/usr/bin/python

import threading
import tkinter as tk
from time import *


window = tk.Tk()
window.title("Espresso")
window.attributes("-fullscreen", True)
window.config(cursor='none')


def exitProgram():
    window.quit()


def updateTime():
    topBar.config(text=strftime('%H:%M', localtime()))
    threading.Timer(1.0, updateTime).start()



topBar = tk.Label(window, width=0, height=0, takefocus=0)
topBar.grid(row=0, column=10, sticky="e")
exitButton = tk.Button(window, text='exit', command=exitProgram, height=2, width=12)
exitButton.grid(row=1, column=0)

updateTime()

tk.mainloop()
