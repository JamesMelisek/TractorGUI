from tkinter import *


class kajalsButtons:
    def __init__(self, master):
        frame=Frame(master,width=300, height=250)
        frame.pack()

        self.printButton=Button(frame,text="print",command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton=Button(frame,text="quit",command=frame.master.destroy)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Print this message")

if __name__ == '__main__':
    root = Tk()
    button = kajalsButtons(root)
    root.mainloop()
