import os
import win32gui, win32con
class terminal:
    global dbCLIVersionInfo
    dbCLIVersionInfo = 'v1.1beta'
    def dbCLI():

        os.system('start cmd /k python DBViewerCLI.py')

    def bookshelf():

        os.system('start cmd /k python booksManager.py')

    def bookshelfGUI():

        os.system('start cmd /k python bookShelfGUI.py')

if __name__ == "__main__":
    terminal.bookshelf()