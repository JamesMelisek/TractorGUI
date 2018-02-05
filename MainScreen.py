from tkinter import *
from PIL import Image
from PIL import ImageTk
import threading
import datetime
import imutils
import cv2
import os

from imutils.video import VideoStream
import argparse
import time




def main_screen():
    root = Tk()
    root.wm_title("MAIN SCREEN")
    #the top will show the video
    imageFrame = Frame(root)
    imageFrame.pack()


    # Capture video frames
    lmain = Label(imageFrame)
    lmain.grid(row=0, column=0)
    cap = cv2.VideoCapture(0)

    def show_frame():
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2image=cv2.resize(cv2image,(600,500))
        #in the future, loop to another function to adjust image from here
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

    buttonsFrame = Frame(root)
    buttonsFrame.pack(side=BOTTOM)

    def go_basic(event):
        print("going basic")
        buttonsFrame.master.destroy()
        cap.release()
        time.sleep(2)
        basic_settings()

    def exitProgram(event):
        print("Exiting")
        buttonsFrame.master.destroy()
        cv2.destroyAllWindows()


    # the bottom has some buttons the user can click
    settingsButton=Button(buttonsFrame, text="Settings")
    settingsButton.bind("<Button 1>", go_basic)
    settingsButton.grid(row=0, column=0, sticky=E, padx=30)

    shutdownButton=Button(buttonsFrame, text="Shut Down")
    shutdownButton.bind("<Button 1>", exitProgram)
    shutdownButton.grid(row=0, column=1, stick=W, padx=30)

    show_frame()
    root.mainloop()

def basic_settings():
    basicRoot=Tk()
    leftFrame = Frame(basicRoot, height = 500, width=400)
    leftFrame.pack(side=LEFT)

    currentSettingsLabel=Label(leftFrame, text="Current Setting: MAKE GLOBAL VAR")
    currentSettingsLabel.pack(side=TOP)

    scrollFrame = Frame(leftFrame)
    scrollFrame.pack(pady=50)
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
    imageFrame.pack(side=BOTTOM)


    # Capture video frames
    lmain = Label(imageFrame)
    lmain.pack()
    cap = cv2.VideoCapture(0)

    def show_frame():
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2image=cv2.resize(cv2image,(300,200))
        #in the future, loop to another function to adjust image from here
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)


    rightFrame = Frame(basicRoot, height=500, width=200)
    rightFrame.pack(side=RIGHT, padx=50)

    advancedSettings= Button(rightFrame, text="Advanced Settings")
    apply=Button(rightFrame, text="Apply")
    back=Button(rightFrame, text="Go Back")

    advancedSettings.pack(pady=50)
    apply.pack(pady=50)
    back.pack(pady=50)

    show_frame()
    basicRoot.mainloop()

def advanced_settings():

    advancedRoot=Tk()

    topFrame=Frame(advancedRoot)
    videoFrame = Frame(topFrame)
    trackbarFrame=Frame(topFrame)
    bottomFrame=Frame(advancedRoot)

    topFrame.pack(side=TOP)
    videoFrame.pack(side=LEFT)
    trackbarFrame.pack(side=RIGHT)
    bottomFrame.pack(side=BOTTOM)

    #the top will show the video
    imageFrame = Frame(videoFrame)
    imageFrame.pack(side=BOTTOM)


    # Capture video frames
    lmain = Label(imageFrame)
    lmain.pack()
    cap = cv2.VideoCapture(0)

    def show_frame():
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2image=cv2.resize(cv2image,(400,400))
        #in the future, loop to another function to adjust image from here
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

    ##Trackbars
    # LABEL H
    label00 = Label(trackbarFrame, text='Hue', width=7, height=2)
    label00.pack()

    # SLIDER H MINIMO
    Hmin = StringVar()
    w1 = Scale(trackbarFrame, from_=0, to=255, orient=HORIZONTAL, variable=Hmin, width=15)
    w1.pack()

    # SLIDER H MAXIMO
    Hmax = StringVar()
    w2 = Scale(trackbarFrame, from_=0, to=255, orient=HORIZONTAL, variable=Hmax, width=15)
    w2.pack()

    # LABEL S
    label11 = Label(trackbarFrame, text='Saturation', width=7, height=2)
    label11.pack()

    # SLIDER S MINIMO
    Smin = StringVar()
    w3 = Scale(trackbarFrame, from_=0, to=255, orient=HORIZONTAL, variable=Smin, width=15)
    w3.pack()

    # SLIDER S MAXIMO
    Smax = StringVar()
    w4 = Scale(trackbarFrame, from_=0, to=255, orient=HORIZONTAL, variable=Smax, width=15)
    w4.pack()

    # LABEL V
    label11 = Label(trackbarFrame, text='Value', width=7, height=2)
    label11.pack()

    # SLIDER V MINIMO
    Vmin = StringVar()
    w5 = Scale(trackbarFrame, from_=0, to=255, orient=HORIZONTAL, variable=Vmin, width=15)
    w5.pack()

    # SLIDER V MAXIMO
    Vmax = StringVar()
    w6 = Scale(trackbarFrame, from_=0, to=255, orient=HORIZONTAL, variable=Vmax, width=15)
    w6.pack()

    ##Trackbars

    back=Button(bottomFrame, text="Go Back")
    save=Button(bottomFrame, text="Save")
    back.pack(side=LEFT,padx=50)
    save.pack(side=RIGHT, padx=50)


    show_frame()
    advancedRoot.mainloop()

def save_settings():
    saveSettings=Tk()

    enterFrame= Frame(saveSettings)
    enterFrame.pack(pady=25)

    nameLabel=Label(enterFrame,text="Name:")
    entry=Entry(enterFrame)
    nameLabel.grid(row=0,column=0)
    entry.grid(row=0, column=1)

    videoFrame=Frame(saveSettings)
    videoFrame.pack()

    bottomFrame=Frame(saveSettings)
    bottomFrame.pack()

    # the top will show the video
    imageFrame = Frame(videoFrame)
    imageFrame.pack(side=BOTTOM)

    # Capture video frames
    lmain = Label(imageFrame)
    lmain.pack()
    cap = cv2.VideoCapture(0)

    def show_frame():
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2image = cv2.resize(cv2image, (700, 400))
        # in the future, loop to another function to adjust image from here
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

    back = Button(bottomFrame, text="Go Back")
    save = Button(bottomFrame, text="Save")
    back.pack(side=LEFT, padx=50)
    save.pack(side=RIGHT, padx=50)

    show_frame()
    saveSettings.mainloop()

save_settings()
