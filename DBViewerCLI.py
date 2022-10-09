import subprocess
import mysql.connector as msql;
import os;
from tkinter import *;
from time import sleep;
import getpass;

class ViewDB:
            # Author @TanmayXD
    global dbCLIVersionInfo
    dbCLIVersionInfo = 'v1.1beta'
    
    def cuiOnClick():
        conn = msql.connect(host="localhost", username="tanmayxd", password="1818", database="libsysdb")
        curShow = conn.cursor()

        q_showDB = "select * from lib"
        q_showStudentsOnly = "select * from lib where member='student'"
        q_showLecturersOnly = "select * from lib where member='lecturer'"
        q_showAdminsOnly = "select * from lib where member='admin'"
        q_showLibrarianOnly = "select * from lib where member='librarian'"

        q_showAdmins = "select f_name, id from admins"
        q_showLibrarians = "select f_name, libr_id, lib_dept from librarians"
        q_showStudents = "select f_name, st_id, dept from students"
        q_showLecturers = "select f_name, l_name, tch_id from lecturers"

        
        ViewDB.loginCLI()


        while True:
            

            print("<===============64bit-Legions===============>")
            print("<==========Library-Database-Viewer==========>")
            print("-> INPUT 0 TO SHOW ALL ENTRIES.")
            print("-> INPUT 1 TO SHOW ALL ENTRIES OF STUDENTS")
            print("-> INPUT 2 TO SHOW ALL ENTRIES OF LECTURERS")
            print("-> INPUT 3 TO SHOW ALL ENTRIES OF ADMINS ")
            print("-> INPUT 4 TO SHOW ALL ENTRIES OF LIBRARIANS")
            print("-> INPUT 5 TO RETRIEVE ALL ADMINS NAMES")
            print("-> INPUT 6 TO RETRIEVE ALL LIBRARIANS NAMES")
            print("-> INPUT 7 TO RETRIEVE ALL STUDENTS NAMES")
            print("-> INPUT 8 TO RETRIEVE ALL LECTURERS NAMES")
            print("-> INPUT 9 TO ABORT LIBSYS CLI.")
            print("-> INPUT 11 FOR CUSTOM QUERY.")
            print("-> INPUT -1 TO EXIT LIBSYS")
            print("<===========Created by TanmayXD===========>")
            print("<================%s================>"%dbCLIVersionInfo)


            ch = int(input("Enter your choice: "))

            os.system('cls')

            print("==============================")
            if ch == 0:
                print("Showing all entries...")
                print("==============================")
                curShow.execute(q_showDB)
            if ch == 1:
                print("Showing Student entries...")
                print("==============================")
                curShow.execute(q_showStudentsOnly)
            if ch == 2:
                print("Showing Lecturer entries...")
                print("==============================")
                curShow.execute(q_showLecturersOnly)
            if ch == 3:
                print("Showing Admin entries...")
                print("==============================")
                curShow.execute(q_showAdminsOnly)
            if ch == 4:
                print("Showing Librarian entries...")
                print("==============================")
                curShow.execute(q_showLibrarianOnly)
            if ch == 5:
                print("All Admins are listed below...")
                print("==============================")
                curShow.execute(q_showAdmins)
            if ch == 6:
                print("All Librarians are listed below...")
                print("==============================")
                curShow.execute(q_showLibrarians)
            if ch == 7:
                print("All Students are listed below...")
                print("==============================")
                curShow.execute(q_showStudents)
            if ch == 8:
                print("All Lecturers are listed below...")
                print("==============================")
                curShow.execute(q_showLecturers)
            if ch == 9:
                print("->Aborting...")
                sleep(2)
                break
            if ch == -1:
                print("->Exiting Library Management System...")
                sleep(2)
                print("Bye have great time! :)")
                exit()
            if ch == 10:
                print("AVAILABLE TABLES\n-> admins\n-> dbcli_login\n-> lecturers\n-> lib\n-> librarians\n->students")
                customQueryInput = input("Enter query: ")
                query = "%s"%customQueryInput
                curShow.execute(query)


            for x in curShow:
                print("->",x)
            print("\nReinitiating...")
            sleep(1)    
        print("LibSysDB CLI Aborted...")
        sleep(1)
        os.system("cls")
        print("<===Library Management System by Team 64bit-Legions===>")

    def loginCLI():
        conn = msql.connect(host="localhost", username="tanmayxd", password="1818", database="libsysdb")
        curLogin = conn.cursor()

        userName = input("Enter your login ID: ")
        password = getpass.getpass()
        os.system('cls')

        q_login = ("select * from dbcli_login where username = %s and password = %s")
        q_data = (userName, password)
        curLogin.execute(q_login, q_data)

        result = curLogin.fetchall()
        if result:
            for i in result:
                if userName == "tanmayxd":
                    print("LOGIN SUCCESS! xD")
                    print("Welcome <-TanmayXD->")
                elif userName == "priyamrug":
                    print("LOGIN SUCCESS! ♥")
                    print("Welcome <-Priya->")
                elif userName == "anujghosh":
                    print("LOGIN SUCCESS! :)")
                    print("Welcome <-Anuj->")
                else:
                    print("LOGIN SUCCESS! ;)")
                    print("Welcome <-Meghdeep->")

                sleep(1)
                break
        else:
            print("Invalid login details! Aborting CLI and LibSys...")
            sleep(1)
            exit()
    
    def newTerminal():

        os.system('start cmd /k python DBViewerCLI.py')

if __name__ == "__main__":
    ViewDB.cuiOnClick()