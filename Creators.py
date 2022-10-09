import os
from tkinter import messagebox;
import ttk;
from tkinter import *;

class Profiles:
        # Author @TanmayXD
    def TanmaySarkar():
        pass
    def PriyaMrug():
        pass
    def MeghdeepDutta():
        pass
    def AnujGhosh():
        pass

class Window:
    global mainVersionInfo
    mainVersionInfo = 'v1.0beta'

    def creditsOnClick():
        
        os.system('cls')
        messagebox.showinfo("<====64bitLegions====>", "Too much interest in us, eh? Bad joke xD \nLet's introduce ourselves :)")
        print("Showing Credits...")
        messagebox.showinfo("LibSys by 64bit-Legions", "Library Management System \nVersion: %s"%mainVersionInfo)
        print("Library Management System %s"%mainVersionInfo)
        messagebox.showinfo("64bitLegion/TanmayXD", "Tanmay Sarkar\n->Project Team Lead\n->GUI & Backend\n->Database CLI")
        print("<====Tanmay Sarkar====>\na.k.a TanmayXD \nProject Team Lead\n->GUI & Backend")
        messagebox.showinfo("64bitLegion/Priya Mrug ♥", "Priya Mrug\n->Associate Team Lead\n->GUI Designer\n")
        print("<====Priya Mrug====>\nAssociate Team Lead \nGUI Designer")
        messagebox.showinfo("64bitLegion/CRXMegh", "Meghdeep Dutta\n->Backend\n")
        print("<====Meghdeep Dutta====>\na.k.a CRXMegh\nBackend")
        messagebox.showinfo("64bitLegion/Anuj Ghosh", "Anuj Ghosh\n->Database\n")
        print("<====Anuj Ghosh====>\nDatabase")

        print("That's who we are! Return to main window?")

        #credWin.mainloop()

if __name__ == "__main__":
    Window.creditsOnClick();