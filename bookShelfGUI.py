from tkinter import * 
import booksManager as dbBook; 
  
global VersionInfo
VersionInfo = 'v2.0alpha'


class Bookshelf:
    def guiOnClick():
        base = Tk()  
        
        base.geometry("550x550")  
        
        base.title('Bookshelf %s'%VersionInfo)  
        base.config(bg="powder blue")
        
        lbl_0 = Label(base, text="Bookshelf %s"%VersionInfo, bg="powder blue", width=20,font=("bold",20))  
        lbl_0.place(x=110,y=15)  

        lbl1 = Label(base, text="Choose Action", bg="powder blue", width=20,font=("bold",10))  
        lbl1.place(x=80,y=90)    
                
        vars = IntVar() 

        def AddButton():
            def Reset():
                bookId.set("")
                bookName.set("")
                authorName.set("")
                edition.set("")
            def AddDataOnClick():
                data = dbBook.Book
                bookDataSet = data(bookId=bookId.get(), bookName=bookName.get(), authorName= authorName.get(), bookEdition=edition.get())
                data.addBookToDB(bookDataSet)
                print("added success")
                Reset()

            bookId = StringVar()
            bookName = StringVar()
            authorName = StringVar()
            edition = StringVar()
                #Bookid
            lblBookId = Label(base, text="Enter Book ID", bg="powder blue", width="20", font=("bold",10))
            lblBookId.place(x=80, y=120)
            enter_1 = Entry(base, textvariable=bookId, width=40)  
            enter_1.place(x=240,y=120)  
                # Book name
            lblBookName = Label(base, text="Enter Book Name", bg="powder blue", width="20", font=("bold",10))
            lblBookName.place(x=80, y=150)
            enter_2 = Entry(base, textvariable=bookName, width=40)  
            enter_2.place(x=240,y=150) 
                # Author name
            lblBookName = Label(base, text="Enter Author Name", bg="powder blue", width="20", font=("bold",10))
            lblBookName.place(x=80, y=180)
            enter_2 = Entry(base, textvariable=authorName, width=40)  
            enter_2.place(x=240,y=180) 
                # Edition
            lblBookName = Label(base, text="Enter Edition", bg="powder blue", width="20", font=("bold",10))
            lblBookName.place(x=80, y=210)
            enter_2 = Entry(base, textvariable=edition, width=40)  
            enter_2.place(x=240,y=210)
                #submit button
            submitbtn = Button(base, text='Submit' , width=20, bg="black",fg='white', command=AddDataOnClick)
            submitbtn.place(x=230,y=250) 

            
        def RemoveButton():
            bookId = StringVar()
            def Reset():
                bookId.set("")
                
            def RemoveDataOnClick():
                data = dbBook.Book
                bookDataSet = data(bookId=bookId.get(), bookEdition="", bookName="", authorName="")
                data.removeBookFromDB(bookDataSet)
                print("remove success")
                Reset()
                
            lblBookId = Label(base, text="Enter Book ID", bg="powder blue", width="20", font=("bold",10))
            lblBookId.place(x=80, y=120)
            enter_1 = Entry(base, textvariable=bookId, width=40)  
            enter_1.place(x=240,y=120) 
                #submit button
            submitbtn = Button(base, text='Submit' , width=20, bg="black",fg='white', command=RemoveDataOnClick)
            submitbtn.place(x=230,y=250)    

        rbtn1 = Radiobutton(base, text="Add Book", padx= 5, bg="powder blue", variable= vars, value=1, command=AddButton)
        rbtn1.place(x=235, y=90)  
        rbtn2 = Radiobutton(base, text="Remove Book", padx= 20, bg="powder blue", variable= vars, value=2, command=RemoveButton)
        rbtn2.place(x=315,y=90)  


        base.mainloop()

if __name__ == "__main__":
    import win32gui, win32con
    # =========Remove this comment before building exe
    # hide = win32gui.GetForegroundWindow()
    # win32gui.ShowWindow(hide , win32con.SW_HIDE)
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++
    Bookshelf.guiOnClick()