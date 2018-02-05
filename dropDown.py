from tkinter import *


def do_nothing():
    print("ok ok i wont...")

if __name__ == '__main__':
    root=Tk()
    myMenu = Menu(root)
    root.config(menu=myMenu,)
    
    root.mainloop()