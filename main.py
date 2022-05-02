from tkinter import *
from MyWindow import *


def main():
    root_window = Tk()
    root_window.iconbitmap("key.ico")
    mywindow = MyWindow(root_window)
    root_window.config(padx=50, pady=50)
    root_window.withdraw()
    root_window.title("Password Manager")
    root_window.deiconify()
    root_window.mainloop()

if __name__ == "__main__":
    main()



