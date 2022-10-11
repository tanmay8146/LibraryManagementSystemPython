import mysql.connector as msql;
import os;
import getpass;

global versionInfo
versionInfo = "v2.0alpha"

global terminalComm
terminalComm = os.system;
global dbConn
dbConn = msql.connect(host="localhost", user="librarian", password="root", database="libsysdb");


class Book:
    def __init__(self, bookId, bookName, authorName, bookEdition) -> None:
        self.bookName = bookName;
        self.authorName = authorName;
        self.bookEdition = bookEdition;
        self.bookId = bookId;

    def addBookToDB(self):
        adder = dbConn.cursor()

        queryAdd = ("insert into bookshelf" "(bookid, bookname, authorname, edition)" "values(%s, %s, %s, %s)")
        booksDetails = (self.bookId, self.bookName, self.authorName, self.bookEdition)

        adder.execute(queryAdd, booksDetails)
        dbConn.commit()
        
    
    def removeBookFromDB(self):
        adder = dbConn.cursor()
        queryRemove = ("DELETE FROM bookshelf WHERE bookid = %s")
        bookDetails = (self.bookId)

        adder.execute(queryRemove, [bookDetails])
        dbConn.commit()

if __name__ == "__main__":
    userName = input("Enter your librarian username: ")
    password = getpass.getpass()

    if userName == 'librarian' and password == 'root':
        while True:
            os.system('cls')

            print("<-------Books-Manager-%s------->"%versionInfo)

            print("-> 1. Add book.")
            print("-> 2. Remove book.")
            ch = int(input())

            if ch == 1:
                os.system('cls')
                print("======Add a BOOK======")
                bId = input("Enter BOOK ID: ")
                bName = input("Enter BOOK NAME: ")
                bAuthor = input("Enter AUTHOR: ")
                bEditon = input("Enter EDITION: ")

                book = Book(bookId=bId, bookName=bName, authorName=bAuthor, bookEdition=bEditon)

                Book.addBookToDB(book)
                print("Added--<")
            if ch == 2:
                os.system('cls')
                
                adder = dbConn.cursor()
                print("<< Books available >>")
                adder.execute("select bookid, bookname from bookshelf")
                for x in adder:
                    print("->",x)

                print("======Remove a BOOK======")
                bId = input("Enter BOOK ID to delete: ")

                book = Book(bookId=bId, bookEdition='', bookName='', authorName='')

                Book.removeBookFromDB(book)
                print("Removed-->") 
    else:
        exit()
    
    