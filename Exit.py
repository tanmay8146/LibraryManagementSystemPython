import time;
from tkinter import *
import tkinter
from tkinter import messagebox;

class ex:
    def exitOnClick():
        exitCom = messagebox.askyesno("LibSys", "Do you really want to quit?")
        if exitCom>0:
            print("Quitting! Good Bye!")
            time.sleep(2)
            exit()
            return
        


        