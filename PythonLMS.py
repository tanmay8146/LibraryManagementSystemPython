import datetime as dt;
from tkinter import *;
import ttk;
import mysql.connector;
from tkinter import messagebox;
import Exit;
import Creators;
import terminalOnDemand as dbTerminal;

class LibSys:
                    # Author @TanmayXD
    global mainVersionInfo
    mainVersionInfo = 'v1.0beta'

    def __init__(self, root):
        self.root = root;
        self.root.title("Library Management System %s by Team 64bit-Legions"%mainVersionInfo)
        self.root.geometry("1550x800+0+0")
        self.root.state('zoomed')

            #variables
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstName_var = StringVar()
        self.lastName_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postCode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookId_var = StringVar()
        self.bookTitle_var = StringVar()
        self.author_var = StringVar()
        self.dateBorrowed_var = StringVar()
        self.dateDue_var = StringVar()
        self.daysOnBook_var = StringVar()
        self.lateRetFine_var = StringVar()
        self.dateOverDue_var = StringVar()
        self.finalPrice_var = StringVar()
        self.memberType = StringVar()


        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6);
        lbltitle.pack(side=TOP, fill=X);

        frame = Frame(root, bd=12,relief=RIDGE, padx=20,bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # Frame// Library Memebership Info 
        DataFrameMem= LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=14, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameMem.place(x=0, y=5, width=800, height=365)

            #MemberType
        lblMem = Label(DataFrameMem, bg="powder blue", text="Member Type", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblMem.grid(row=0, column=0, stick=W)
                #combo box
        comMem = ttk.Combobox(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.member_var, width=27, state="readonly")
        comMem["value"]= ("Admin", "Student", "Lecturer", "Librarian")
        self.memberType.set(self.member_var)

        comMem.grid(row=0, column=1)

            #PRN
        lblPRN = Label(DataFrameMem, bg="powder blue", text="PRN No.", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblPRN.grid(row=1, column=0, stick=W)
                #EntryBox
        txt_PRN = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.prn_var, width=29)
        txt_PRN.grid(row=1, column=1)
        
            #ID No
        lblId = Label(DataFrameMem, bg="powder blue", text="ID No.", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblId.grid(row=2, column=0, stick=W)
                #EntryBox
        txt_Id = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.id_var, width=29)
        txt_Id.grid(row=2, column=1)
        
            #FirstName
        lblFn = Label(DataFrameMem, bg="powder blue", text="First Name", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblFn.grid(row=3, column=0, stick=W)
                #EntryBox
        txt_Fn = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.firstName_var, width=29)
        txt_Fn.grid(row=3, column=1)
        
            #LastName
        lblLn = Label(DataFrameMem, bg="powder blue", text="Last Name", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblLn.grid(row=4, column=0, stick=W)
                #EntryBox
        txt_Ln = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.lastName_var, width=29)
        txt_Ln.grid(row=4, column=1)
        
            #Address1
        lblAdd1 = Label(DataFrameMem, bg="powder blue", text="Address L1", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblAdd1.grid(row=5, column=0, stick=W)
                #EntryBox
        txt_Add1 = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.address1_var, width=29)
        txt_Add1.grid(row=5, column=1)
        
            #Address2
        lblAdd2 = Label(DataFrameMem, bg="powder blue", text="Address L2", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblAdd2.grid(row=6, column=0, stick=W)
                #EntryBox
        txt_Add2 = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.address2_var, width=29)
        txt_Add2.grid(row=6, column=1)
        
            #PINCode
        lblPin = Label(DataFrameMem, bg="powder blue", text="PIN Code", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblPin.grid(row=7, column=0, stick=W)
                #EntryBox
        txt_Pin = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.postCode_var, width=29)
        txt_Pin.grid(row=7, column=1)
        
            #Mobile
        lblCell = Label(DataFrameMem, bg="powder blue", text="Phone", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblCell.grid(row=8, column=0, stick=W)
                #EntryBox
        txt_Cell = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.mobile_var, width=29)
        txt_Cell.grid(row=8, column=1)

            #BookId
        lblBookId = Label(DataFrameMem, bg="powder blue", text="Book ID", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblBookId.grid(row=0, column=3, stick=W)
                #EntryBox
        txt_BookId = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.bookId_var, width=29)
        txt_BookId.grid(row=0, column=4)
        
            #BookTitle
        lblBookTitle = Label(DataFrameMem, bg="powder blue", text="Book Title", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblBookTitle.grid(row=1, column=3, stick=W)
                #EntryBox
        txt_BookTitle = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.bookTitle_var, width=29)
        txt_BookTitle.grid(row=1, column=4)
        
            #AuthorName
        lblAutName = Label(DataFrameMem, bg="powder blue", text="Author Name", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblAutName.grid(row=2, column=3, stick=W)
                #EntryBox
        txt_AutName = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.author_var, width=29)
        txt_AutName.grid(row=2, column=4)
        
            #DateBorrowed
        lblBorrowD = Label(DataFrameMem, bg="powder blue", text="Date Borrowed", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblBorrowD.grid(row=3, column=3, stick=W)
                #EntryBox
        txt_BorrowD = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.dateBorrowed_var, width=29)
        txt_BorrowD.grid(row=3, column=4)
        
            #DateDue
        lblDueD = Label(DataFrameMem, bg="powder blue", text="Date Due", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblDueD.grid(row=4, column=3, stick=W)
                #EntryBox
        txt_DueD = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.dateDue_var, width=29)
        txt_DueD.grid(row=4, column=4)
        
            #DaysOnBook
        lblDaysBook = Label(DataFrameMem, bg="powder blue", text="Days On Book", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblDaysBook.grid(row=5, column=3, stick=W)
                #EntryBox
        txt_DaysBook = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.daysOnBook_var, width=29)
        txt_DaysBook.grid(row=5, column=4)
        
            #BookId
        lblRetFine = Label(DataFrameMem, bg="powder blue", text="Late Return Fine", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblRetFine.grid(row=6, column=3, stick=W)
                #EntryBox
        txt_RetFine = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.lateRetFine_var, width=29)
        txt_RetFine.grid(row=6, column=4)
        
            #DateOverDue
        lblOverDueD = Label(DataFrameMem, bg="powder blue", text="Date Over Due", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblOverDueD.grid(row=7, column=3, stick=W)
                #EntryBox
        txt_OverDueD = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.dateOverDue_var, width=29)
        txt_OverDueD.grid(row=7, column=4)
        
            #ActualPrice
        lblPrice = Label(DataFrameMem, bg="powder blue", text="Actual Price", font=("times new roman", 12, "bold"), padx=2, pady=6);
        lblPrice.grid(row=8, column=3, stick=W)
                #EntryBox
        txt_Price = Entry(DataFrameMem, font=("times new roman", 12, "bold"), textvariable=self.finalPrice_var, width=29)
        txt_Price.grid(row=8, column=4)
        
        # Frame// Book Details
        DataFrameBook= LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=14, relief=RIDGE, font=("times new roman", 10, "bold"))
        DataFrameBook.place(x=870, y=5, width=600, height=365)

        self.txtBox=Text(DataFrameBook, font=("times new roman", 12, "bold"), width=48, height=20, padx=2, pady=6)
        self.txtBox.grid(row=0, column=3)

        listScrollBar = Scrollbar(DataFrameBook)
        listScrollBar.grid(row=0, column= 1, sticky= "ns")

        listBook = ['DBMS Concepts', 'Learn Python the Hard Way', 'Introduction to Machine Learning with Python', 'Head First C', 'Computer Fundamentals and Programming in C', 'Data Science For Dummies', 'Brief History of Time', 'Effective Java', 'Thinking in Java', 'Machine Learning for Dummies'];

        def selectBookOnClick(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if x == "DBMS Concepts":
                self.bookId_var.set("B000")
                self.bookTitle_var.set("DBMS Concepts")
                self.author_var.set("S Sudarshan")

                b0_d1 = dt.datetime.today()
                b0_d2 = dt.timedelta(days=15)
                b0_d3 = b0_d1+b0_d2

                self.dateBorrowed_var.set(b0_d1)
                self.dateDue_var.set(b0_d3)
                self.daysOnBook_var.set(15)
                self.lateRetFine_var.set("Rs.50")
                self.dateOverDue_var.set("NULL")
                self.finalPrice_var.set("Rs. 790")

            if x == "Learn Python the Hard Way":
                self.bookId_var.set("B001")
                self.bookTitle_var.set("Learn Python the Hard Way")
                self.author_var.set("Zed Shaw")

                b1_d1 = dt.datetime.today()
                b1_d2 = dt.timedelta(days=15)
                b1_d3 = b1_d1+b1_d2

                self.dateBorrowed_var.set(b1_d1)
                self.dateDue_var.set(b1_d3)
                self.daysOnBook_var.set(15)
                self.lateRetFine_var.set("Rs.48")
                self.dateOverDue_var.set("NULL")
                self.finalPrice_var.set("Rs. 1190")

            if x == "Introduction to Machine Learning with Python":
                self.bookId_var.set("B002")
                self.bookTitle_var.set("Introduction to Machine Learning with Python")
                self.author_var.set("Andreas Muller")

                b2_d1 = dt.datetime.today()
                b2_d2 = dt.timedelta(days=15)
                b2_d3 = b2_d1+b2_d2

                self.dateBorrowed_var.set(b2_d1)
                self.dateDue_var.set(b2_d3)
                self.daysOnBook_var.set(15)
                self.lateRetFine_var.set("Rs. 100")
                self.dateOverDue_var.set("NULL")
                self.finalPrice_var.set("Rs. 1000")
            if x == "Head First C":
                self.bookId_var.set("B003")
                self.bookTitle_var.set("Head First C")
                self.author_var.set("Dawn Griffiths")

                b3_d1 = dt.datetime.today()
                b3_d2 = dt.timedelta(days=15)
                b3_d3 = b3_d1+b3_d2

                self.dateBorrowed_var.set(b3_d1)
                self.dateDue_var.set(b3_d3)
                self.daysOnBook_var.set(15)
                self.lateRetFine_var.set("Rs. 29")
                self.dateOverDue_var.set("NULL")
                self.finalPrice_var.set("Rs. 1600")
            if x == "Computer Fundamentals and Programming in C":
                self.bookId_var.set("B004")
                self.bookTitle_var.set("Computer Fundamentals and Programming in C")
                self.author_var.set("Reema Thareja")

                b4_d1 = dt.datetime.today()
                b4_d2 = dt.timedelta(days=15)
                b4_d3 = b4_d1+b4_d2

                self.dateBorrowed_var.set(b4_d1)
                self.dateDue_var.set(b4_d3)
                self.daysOnBook_var.set(15)
                self.lateRetFine_var.set("Rs. 69")
                self.dateOverDue_var.set("NULL")
                self.finalPrice_var.set("Rs. 900")
            if x == "Data Science For Dummies":
                self.bookId_var.set("B005")
                self.bookTitle_var.set("Data Science For Dummies")
                self.author_var.set("Lillian Pierson")

                b5_d1 = dt.datetime.today()
                b5_d2 = dt.timedelta(days=15)
                b5_d3 = b5_d1 + b5_d2

                self.dateBorrowed_var.set(b5_d1)
                self.dateDue_var.set(b5_d3)
                self.daysOnBook_var.set(15)
                self.lateRetFine_var.set("Rs. 90")
                self.dateOverDue_var.set("NULL")
                self.finalPrice_var.set("Rs. 1100")

            if x == "Brief History of Time":
                self.bookId_var.set("B006")
                self.bookTitle_var.set("Brief History of Time")
                self.author_var.set("Stephen Hawking")

                b6_d1 = dt.datetime.today()
                b6_d2 = dt.timedelta(days=15)
                b6_d3 = b6_d1 + b6_d2

                self.dateBorrowed_var.set(b6_d1)
                self.dateDue_var.set(b6_d3)
                self.daysOnBook_var.set(15)
                self.lateRetFine_var.set("Rs. 150")
                self.dateOverDue_var.set("NULL")
                self.finalPrice_var.set("Rs. 2100")

            if x == "Effective Java":
                self.bookId_var.set("B007")
                self.bookTitle_var.set("Effective Java")
                self.author_var.set("Joshua Bloch")

                b7_d1 = dt.datetime.today()
                b7_d2 = dt.timedelta(days=15)
                b7_d3 = b7_d1 + b7_d2

                self.dateBorrowed_var.set(b7_d1)
                self.dateDue_var.set(b7_d3)
                self.daysOnBook_var.set(15)
                self.lateRetFine_var.set("Rs. 40")
                self.dateOverDue_var.set("NULL")
                self.finalPrice_var.set("Rs. 1700")

            if x == "Thinking in Java":
                self.bookId_var.set("B008")
                self.bookTitle_var.set("Thinking in Java")
                self.author_var.set("Bruce Eckel")

                b8_d1 = dt.datetime.today()
                b8_d2 = dt.timedelta(days=15)
                b8_d3 = b8_d1 + b8_d2

                self.dateBorrowed_var.set(b8_d1)
                self.dateDue_var.set(b8_d3)
                self.daysOnBook_var.set(15)
                self.lateRetFine_var.set("Rs. 50")
                self.dateOverDue_var.set("NULL")
                self.finalPrice_var.set("Rs. 1100")

            if x == "Machine Learning for Dummies":
                self.bookId_var.set("B009")
                self.bookTitle_var.set("Machine Learning for Dummies")
                self.author_var.set("John Paul Mueller")

                b8_d1 = dt.datetime.today()
                b8_d2 = dt.timedelta(days=15)
                b8_d3 = b8_d1 + b8_d2

                self.dateBorrowed_var.set(b8_d1)
                self.dateDue_var.set(b8_d3)
                self.daysOnBook_var.set(15)
                self.lateRetFine_var.set("Rs. 90")
                self.dateOverDue_var.set("NULL")
                self.finalPrice_var.set("Rs. 1900")






        listBox = Listbox(DataFrameBook, font=("arial", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", selectBookOnClick)
        listBox.grid(row=0, column=0, padx=4)
        listScrollBar.config(command=listBox.yview)

        for item in listBook:       #inserting books list on the ListBox
            listBox.insert(END, item)
        
        
        
        #Frame// Buttons
        frameButton = Frame(root, bd=12,relief=RIDGE, padx=20,bg="powder blue");
        frameButton.place(x=0, y=530, width=1530, height=70)
            #Button// Add Data
        btnAddData = Button(frameButton, command=self.addData, text="Add Data", font=("arial", 10, "bold"), width=22, bg= "blue", fg="white", padx= 1, pady= 10);
        btnAddData.grid(row= 0, column= 0)
        
            #Button// Show Data
        btnShowData = Button(frameButton, command=self.showData, text="Show Data", font=("arial", 10, "bold"), width=22, bg= "blue", fg="white", padx= 1, pady= 10);
        btnShowData.grid(row= 0, column= 1)
        
            #Button// Update
        btnUpdate = Button(frameButton, command=self.updateOnClick, text="Update", font=("arial", 10, "bold"), width=22, bg= "blue", fg="white", padx= 1, pady= 10);
        btnUpdate.grid(row= 0, column= 2)
        
            #Button// Delete
        btnDelete = Button(frameButton, command=self.deleteOnClick, text="Delete", font=("arial", 10, "bold"), width=22, bg= "blue", fg="white", padx= 1, pady= 10);
        btnDelete.grid(row= 0, column= 3)

            #Button// Bookshelf
        dbView = dbTerminal.terminal
        btnExit = Button(frameButton, command=dbView.bookshelfGUI, text="Bookshelf", font=("arial", 10, "bold"), width=22, bg= "blue", fg="white", padx= 1, pady= 10);
        btnExit.grid(row= 0, column=  5)
        
            #Button// Reset
        btnReset = Button(frameButton, command=self.resetOnClick, text="Reset", font=("arial", 10, "bold"), width=22, bg= "blue", fg="white", padx= 1, pady= 10);
        btnReset.grid(row= 0, column= 4)
        
            #Button// Credits
        creatorObj = Creators.Window
        btnCredits = Button(frameButton, command=creatorObj.creditsOnClick, text="Credits", font=("arial", 10, "bold"), width=22, bg= "blue", fg="white", padx= 1, pady= 10);
        btnCredits.grid(row= 0, column= 6)
        
            #Button// Exit
        exit = Exit.ex
        btnExit = Button(frameButton, command=exit.exitOnClick, text="Exit", font=("arial", 10, "bold"), width=22, bg= "blue", fg="white", padx= 1, pady= 10);
        btnExit.grid(row= 0, column= 7)


        
        
        
        
        
        

        #Frame// Information
            #Books
        frameInfo = Frame(self.root, bd=12,relief=RIDGE, padx=20,bg="powder blue");
        frameInfo.place(x=0, y=600, width=1530, height=195);
            #Transaction Details
        table_Frame = Frame(frameInfo,bd=6, relief=RIDGE,bg="powder blue")
        table_Frame.place(x=0, y= 2, width=1460, height=165)

        x_tableScroll = ttk.Scrollbar(table_Frame, orient=HORIZONTAL)
        y_tableScroll = ttk.Scrollbar(table_Frame, orient=VERTICAL)
        self.libTable = ttk.Treeview(table_Frame, column=("membertype", "prnno", "id", "firstname", "lastname", "address1", "address2", "postid", "mobile", "bookid", "booktitle", "author", "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"), xscrollcommand= x_tableScroll.set, yscrollcommand= y_tableScroll.set)
        x_tableScroll.pack(side=BOTTOM, fill=X)
        y_tableScroll.pack(side=RIGHT, fill=Y)
        x_tableScroll.config(command=self.libTable.xview)
        y_tableScroll.config(command=self.libTable.yview)

        self.libTable.heading("membertype", text="Member Type")
        self.libTable.heading("prnno", text="PRN No.")
        self.libTable.heading("id", text="ID No.")
        self.libTable.heading("firstname", text="First Name")
        self.libTable.heading("lastname", text="Last Name")
        self.libTable.heading("address1", text="Address L1")
        self.libTable.heading("address2", text="Address L2")
        self.libTable.heading("postid", text="Post ID")
        self.libTable.heading("mobile", text="Mobile")
        self.libTable.heading("bookid", text="Book ID")
        self.libTable.heading("booktitle", text="Book Title")
        self.libTable.heading("author", text="Author")
        self.libTable.heading("dateborrowed", text="Date of Borrowed")
        self.libTable.heading("datedue", text="Date Due")
        self.libTable.heading("days", text="Days On Book")
        self.libTable.heading("latereturnfine", text="LateReturnFine")
        self.libTable.heading("dateoverdue", text="DateOverDue")
        self.libTable.heading("finalprice", text="Final Price")

        self.libTable["show"] = "headings"
        self.libTable.pack(fill=BOTH, expand=1)

        self.fetchData()
        self.libTable.bind("<ButtonRelease-1>", self.getCursor)

        
    def addData(self):
        
        conn = mysql.connector.connect(host="localhost", username="tanmayxd", password="1818", database="libsysdb")
        cursor = conn.cursor()
        #datausers
        dataVariables = (self.member_var.get(), self.prn_var.get(), self.id_var.get(), self.firstName_var.get(), self.lastName_var.get(), self.address1_var.get(), self.address2_var.get(), self.postCode_var.get(), self.mobile_var.get(), self.bookId_var.get(), self.bookTitle_var.get(), self.author_var.get(), self.dateBorrowed_var.get(), self.dateDue_var.get(), self.daysOnBook_var.get(), self.lateRetFine_var.get(), self.dateOverDue_var.get(), self.finalPrice_var.get())

        #sqlcommand
        addDataCommand = ("INSERT INTO LIB" "(member, prn_id, id, f_name, l_name, address_one, address_two, post_code, mobile_no, book_id, book_title, author, date_borrowed, date_due, days_on_book, late_return_fine, date_overdue, final_price)" "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        
        addConfirm = messagebox.askyesnocancel("Add entry?", "Do you really want to add entry?")
        if addConfirm >0:
            cursor.execute(addDataCommand, dataVariables)
            conn.commit()

        conn.close()
        
        print("Successfully added data to the database!")
        nowTime = dt.datetime.now()
        dataTime = nowTime.strftime("%H:%M:%S")
        messagebox.showinfo("Success", "Data has been inserted successfully at  %s"%dataTime)

        self.fetchData()
        self.showData()
        self.resetOnClick()

        # dbconn = mysql.connector.connect(host="localhost", username="tanmayxd", password="1818", database="libsysdb")
        # dbCur = dbconn.cursor()

    def fetchData(self):
        conn = mysql.connector.connect(host="localhost", username="tanmayxd", password="1818", database="libsysdb")
        cursor = conn.cursor()
        q_fetch = "select * from lib"
        cursor.execute(q_fetch)
        rows = cursor.fetchall()

        if len(rows) != 0:
            self.libTable.delete(*self.libTable.get_children())
            for i in rows:
                self.libTable.insert("",END,values=i)
            conn.commit()
        conn.close()

    def updateOnClick(self):
        conn = mysql.connector.connect(host="localhost", username="tanmayxd", password="1818", database="libsysdb")
        cursor = conn.cursor()

        q_update = ("update lib set member=%s, id=%s, f_name=%s, l_name=%s, address_one=%s, address_two=%s, post_code=%s, mobile_no=%s, book_id=%s, book_title=%s, author=%s, date_borrowed=%s, date_due=%s, days_on_book=%s, late_return_fine=%s, date_overdue=%s, final_price=%s" " where prn_id=%s")
        q_dataUpdate = (self.member_var.get(), self.id_var.get(), self.firstName_var.get(), self.lastName_var.get(), self.address1_var.get(), self.address2_var.get(), self.postCode_var.get(), self.mobile_var.get(), self.bookId_var.get(), self.bookTitle_var.get(), self.author_var.get(), self.dateBorrowed_var.get(), self.dateDue_var.get(), self.daysOnBook_var.get(), self.lateRetFine_var.get(), self.dateOverDue_var.get(), self.finalPrice_var.get(), self.prn_var.get())

        updateConfirm = messagebox.askyesnocancel("Confirm update?", "Do you really want to update member data?")
        if updateConfirm > 0:
            cursor.execute(q_update, q_dataUpdate)
            conn.commit()
        
        self.fetchData()
        self.showData()
        self.resetOnClick()
        print("updated!")
        conn.close()

    def getCursor(self, event=""):
        cursorRow = self.libTable.focus()
        content = self.libTable.item(cursorRow)
        row = content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstName_var.set(row[3])
        self.lastName_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postCode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookId_var.set(row[9])
        self.bookTitle_var.set(row[10])
        self.author_var.set(row[11])
        self.dateBorrowed_var.set(row[12])
        self.dateDue_var.set(row[13])
        self.daysOnBook_var.set(row[14])
        self.lateRetFine_var.set(row[15])
        self.dateOverDue_var.set(row[16])
        self.finalPrice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END, "Member Type: \t\t"+self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No: \t\t"+self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No: \t\t"+self.id_var.get() + "\n")
        self.txtBox.insert(END, "First Name: \t\t"+self.firstName_var.get() + "\n")
        self.txtBox.insert(END, "Last Name: \t\t"+self.lastName_var.get() + "\n")
        self.txtBox.insert(END, "Address Line 1: \t\t"+self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address Line 2: \t\t"+self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Post Code: \t\t"+self.postCode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No: \t\t"+self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID: \t\t"+self.bookId_var.get() + "\n")
        self.txtBox.insert(END, "Book Title: \t\t"+self.bookTitle_var.get() + "\n")
        self.txtBox.insert(END, "Author Name: \t\t"+self.author_var.get() + "\n")
        self.txtBox.insert(END, "Borrow Date: \t\t"+self.dateBorrowed_var.get() + "\n")
        self.txtBox.insert(END, "Date Due: \t\t"+self.dateDue_var.get() + "\n")
        self.txtBox.insert(END, "Max Days on Book: \t\t"+self.daysOnBook_var.get() + " days\n")
        self.txtBox.insert(END, "Late Return Fine: \t\t"+self.lateRetFine_var.get() + "\n")
        self.txtBox.insert(END, "Date Over Due: \t\t"+self.dateOverDue_var.get() + "\n")
        self.txtBox.insert(END, "Final Price: \t\t"+self.finalPrice_var.get() + "\n")

    def resetOnClick(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstName_var.set("")
        self.lastName_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postCode_var.set("")
        self.mobile_var.set("")
        self.bookId_var.set("")
        self.bookTitle_var.set("")
        self.author_var.set("")
        self.dateBorrowed_var.set("")
        self.dateDue_var.set("")
        self.daysOnBook_var.set("")
        self.lateRetFine_var.set("")
        self.dateOverDue_var.set("")
        self.finalPrice_var.set("")
        self.txtBox.delete("1.0",END)

    def deleteOnClick(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error!", "Select the member first :(")
        else:
            conn = mysql.connector.connect(host="localhost", username="tanmayxd", password="1818", database="libsysdb")
            cursor = conn.cursor()

            q_delete = "delete from lib where prn_id=%s"
            q_value = (self.prn_var.get(),)

            deleteConfirm = messagebox.askyesnocancel("Confirm delete?", "Do you really want to delete?\nOnce entry is deleted can not be recovered.")
            if deleteConfirm > 0:
                cursor.execute(q_delete, q_value)
                conn.commit()

            self.fetchData()
            self.showData()
            self.resetOnClick()
            print("Deleted!")
            conn.close()
            messagebox.showinfo("Success", "Entry has been deleted!")
