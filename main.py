import cv2
import sys
from tkinter import *


def simple_window():
    # create a window
    root = Tk()

    topFrame = Frame(root) #this is like a container
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)


    #add widgets to the frames
    button1 = Button(topFrame, text="button1") #parent is the top frame
    button2 = Button(topFrame, text="button2")
    button3 = Button(topFrame, text="button3")

    button4 = Button(bottomFrame, text="button4")


    button1.pack(side=LEFT)
    button2.pack(side=LEFT)
    button3.pack(side=LEFT)
    button4.pack(side=RIGHT)

    root.mainloop()


def fit_widgets():
    root = Tk()

    one = Label(root, text= "label1", bg="green")
    two = Label(root, text="label2")
    three = Label(root, text="label3")

    one.pack(side=LEFT, fill=X)
    two.pack(side=LEFT)
    three.pack(fill=Y)

    root.mainloop()


def fit_grid():
     root = Tk()
     label1= Label(root, text="Name")
     label2= Label(root, text="Password")
     entry1 = Entry(root)
     entry2 = Entry(root)
     checkbox = Checkbutton(root, text="keep me logged in")

     label1.grid(row=0, column= 0, sticky=E) #NESW (compass)
     label2.grid(row=1, column=0)
     entry1.grid(row=0, column=1)
     entry2.grid(row=1, column=1)
     checkbox.grid(row=2, columnspan=2)
     root.mainloop()

def interact():
    root = Tk()
    button1= Button(root, text="click me",command=fit_grid)
    button1.pack()
    root.mainloop()

def interact1():
    root = Tk()
    button1= Button(root, text="click me")
    button1.bind("<Button 1>", fit_grid)
    button1.pack()
    root.mainloop()

def mouse_events():
    root = Tk()
    frame = Frame(root, width=300, height=250)
    frame.bind("<Button 1>", left_click)
    frame.bind("<Button 2>", right_click)
    frame.pack();
    button1=Button(root, text="click me")

    root.mainloop()

def left_click(event):
    print("left")

def right_click(event):
    print("right")

def middle_click(event):
    print("middle")

mouse_events()