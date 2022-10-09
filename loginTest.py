from tkinter import *;
from tkinter import messagebox;
import mysql.connector as msql
import PythonLMS as Lms
from time import sleep;
import os;

class Login():
    global conn 
    conn = msql.connect(host="localhost", user="tanmayxd", password="1818", database="libsysdb")
    global cursordb 
    cursordb= conn.cursor()

    def loginOnClick():
        global root2
        root2 = Toplevel(root)
        root2.title("<==Admin Login==>")
        root2.geometry("450x300")
        root2.config(bg="white")

        global userVerify
        global passwordVerify

        Label(root2, text="Enter Account Details", bd=5, font=('arial', 12, 'bold'), relief="groove", fg="white", bg="powder blue", width=300).pack()

        userVerify = StringVar()
        passwordVerify = StringVar()

        Label(root2, text="").pack()
        Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=userVerify).pack()
        Label(root2, text="").pack()
        Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=passwordVerify, show="*").pack()
        Label(root2, text="").pack()
        Button(root2, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=Login.loginOnLogIn).pack()
        Label(root2, text="")

        print("LOGIN SUCCESS")
    
    def loggedDestroy():
        loggedMessage.destroy()
        root2.destroy()

    def failedDestroy():
        failedMessage.destroy()

    def logged():
        global loggedMessage
        loggedMessage = Toplevel(root2)
        loggedMessage.title("WELCOME :)")
        loggedMessage.geometry("500x100")
        Label(loggedMessage, text="Login Success! User: {}".format(userVerify.get()), fg="green", font="bold").pack()
        Label(loggedMessage, text="").pack()
        Button(loggedMessage, text="Logout", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=Login.loggedDestroy).pack()
        sleep(2)
        root2.destroy()
                    #====Starting the app====
        os.system("cls")
        print("<===Library Management System by Team 64bit-Legions===>")
        lms = Lms.LibSys
        root.destroy()
        r = Tk();
        obj = lms(r)
        messagebox.showinfo("Team 64bit-Legions", "Welcome to Library Management System :)")
        r.mainloop()
        
        

    def failed():
        global failedMessage
        failedMessage = Toplevel(root2)
        failedMessage.title("Invalid Message")
        failedMessage.geometry("500x100")
        Label(failedMessage, text="Invalid Username or Password", fg="red", font="bold").pack()
        Button(failedMessage, text="Ok", bg="powder blue", fg="white", relief="groove", font=('arial', 12, 'bold'), command=Login.failedDestroy).pack()


    def loginOnLogIn():
        userVerify1 = userVerify.get()
        passwordVerify1 = passwordVerify.get()

        q_verification = "select * from dbcli_login where login_id = %s and password = %s"
        cursordb.execute(q_verification, [(userVerify1), (passwordVerify1)])
        result = cursordb.fetchall()
        if result:
            for i in result:
                Login.logged()
                break
        else:
            Login.failed()


    def exitOnClick():
        wayOut = messagebox.askyesnocancel("Team 64bit-Legions", "Do you want to exit LibSys?")
        if wayOut > 0:
            root.destroy()
            return

    def mainDisplay():
        global root
        root = Tk()
        root.config(bg="powder blue")
        root.title("LibSys Login")
        root.geometry("500x500")
        Label(root, text="TEAM 64bit-LEGIONS LOGIN", bd=15, font=('arial', 20, 'bold'), relief="groove", fg="powder blue", bg="white", width=300).pack()
        Label(root, text="").pack()
        Button(root, text='Log In', height="1", width="20", bd=4, font=('arial', 12, 'bold'), relief="groove", fg="white", bg="powder blue", command=Login.loginOnClick).pack()
        Label(root, text="").pack()
        Button(root, text='Exit', height="1", width="20", bd=4, font=('arial', 12, 'bold'), relief="groove", fg="white", bg="powder blue", command=Login.exitOnClick).pack()
        Label(root, text="").pack()
Login.mainDisplay()
root.mainloop()
