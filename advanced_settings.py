from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2

import threading
import datetime
#import imutils
import os

#from imutils.video import VideoStream
import argparse
import time


def advanced_settings():
    basicRoot=Tk()
    leftFrame = Frame(basicRoot, height = 500, width=400)
    leftFrame.pack(side=LEFT)
    rightFrame = Frame(basicRoot, height=500, width=200)
    rightFrame.pack(side=RIGHT, padx=50)

    show = True

    #define a function that takes you to make new
    def make_new_file(event):
        from Adv_Settings import sliders_settings
        global show
        show=False
        print("new file")
        leftFrame.master.destroy()
        cv2.destroyAllWindows()
        sliders_settings()


    titleLabel=Label(leftFrame, text="ADVANCED SETTINGS")
    titleLabel.pack(side=TOP)

    scrollFrame = Frame(rightFrame)
    scrollFrame.pack(pady=30, padx=10)
    #create the scroll bar for selection
    scrollbar = Scrollbar(scrollFrame)
    scrollbar.pack(side=RIGHT, fill=Y)
    settings=["Day","Evening","Short","Tall","other","other1","other3","other4","other5","other5","other6","other7", "other8"]
    mylist = Listbox(scrollFrame, yscrollcommand=scrollbar.set)
    for line in settings:
        mylist.insert(END, line)

    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)


    #the top will show the video
    imageFrame = Frame(leftFrame)
    imageFrame.pack(side=BOTTOM, padx=10, pady=10)

    def show_frame():
        if (show == True ):
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            cv2image = cv2.resize(cv2image, (500, 400))
            # in the future, loop to another function to adjust image from here
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(10, show_frame)

    # Capture video frames
    lmain = Label(imageFrame)
    lmain.pack()
    cap = cv2.VideoCapture(0)

    mkbtn= Button(rightFrame, text="MAKE NEW")
    buttonsFrame = Frame(rightFrame)
    from Adv_Settings import sliders_settings
    mkbtn.bind("<Button 1>", sliders_settings)

    img = "icons/house_2.png"
    img2 = Image.open(img)
    img3 = ImageTk.PhotoImage(image=img2)
    home = Button(buttonsFrame, image=img3)

    imgbk = "icons/back.png"
    imgbk2 = Image.open(imgbk)
    imgbk3 = ImageTk.PhotoImage(image=imgbk2)
    back = Button(buttonsFrame, image=imgbk3)


    mkbtn.pack(pady=10)
    buttonsFrame.pack()
    home.pack(side=LEFT, pady=10, padx=10)
    back.pack(pady=10, padx=10)

    show_frame()
    basicRoot.mainloop()
