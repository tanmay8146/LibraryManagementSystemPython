from tkinter import *;
from tkinter import messagebox;
import mysql.connector as msql;
import PythonLMS as Lms;
from time import sleep;
import os;
import terminalOnDemand;

class Login():
            # Author @TanmayXD
    global conn 
    conn = msql.connect(host="localhost", user="tanmayxd", password="1818", database="libsysdb")
    global cursordb
    cursordb= conn.cursor()

    global mainVersionInfo
    mainVersionInfo = 'v2.0beta'
    global dbCLIVersionInfo
    dbCLIVersionInfo = 'v1.1beta'
    global booksManagerVersion
    booksManagerVersion = 'v2.0alpha'

    def loginOnClick():
        global root2
        root2 = Toplevel(root)
        root2.title("<==Admin Login==>")
        root2.geometry("450x300")
        root2.config(bg="white")
        root2.resizable(width=False, height=False)

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
        Entry(root2, textvariable=passwordVerify, show="x").pack()
        Label(root2, text="").pack()
        Button(root2, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=Login.loginOnLogIn).pack()
        Label(root2, text="")
    
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
        print("LOGIN SUCCESS!")
        sleep(2)
        root2.destroy()
                    #====Starting the app====
        os.system("cls")
        print("<===Library Management System %s by Team 64bit-Legions===>"%mainVersionInfo)
        print("Welcome, admin ->{}".format(userVerify.get()))
        lms = Lms.LibSys
        root.destroy()
        r = Tk();
        obj = lms(r)
        messagebox.showinfo("Team 64bit-Legions", "Welcome to Library Management System %s :)"%mainVersionInfo)
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

        q_verification = "select * from dbcli_login where username = %s and password = %s"
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
            exit()
            return
    
    def DBTerminalOnClick():
        terminal = terminalOnDemand.terminal
        terminal.dbCLI()
        print("Database Viewer!")

    def BooksManagerOnClick():
        terminal = terminalOnDemand.terminal
        terminal.bookshelf()
        print("Bookshelf")

    def mainDisplay():
        global root
        root = Tk()
        root.config(bg="powder blue")
        root.title("LibSys Login")
        root.geometry("500x500")
        root.resizable(width=False, height=False)
        Label(root, text="Team 64bit-LEGION", bd=15, font=('arial', 20, 'bold'), relief="groove", fg="powder blue", bg="white", width=300).pack()
        Label(root, text="").pack()
            #login button
        Button(root, text='Log In', height="1", width="20", bd=4, font=('arial', 12, 'bold'), relief="groove", fg="white", bg="powder blue", command=Login.loginOnClick).pack()
        Label(root, text="").pack()

            #Bookshelf GUI button
        Button(root, text='Database Viewer %s(admins only)'%dbCLIVersionInfo, height="1", width="32", bd=4, font=('arial', 12, 'bold'), relief="groove", fg="white", bg="powder blue", command=Login.DBTerminalOnClick).pack()
        Label(root, text="").pack()

            #Books Manager button
        Button(root, text='Bookshelf %s'%booksManagerVersion, height="1", width="25", bd=4, font=('arial', 12, 'bold'), relief="groove", fg="white", bg="powder blue", command=Login.BooksManagerOnClick).pack()
        Label(root, text="").pack()

            #exit button
        Button(root, text='Exit', height="1", width="20", bd=4, font=('arial', 12, 'bold'), relief="groove", fg="white", bg="powder blue", command=Login.exitOnClick).pack()
        Label(root, text="").pack()
Login.mainDisplay()
root.mainloop()
