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




def basic_settings():
    basicRoot=Tk()
    leftFrame = Frame(basicRoot, height = 500, width=400)
    leftFrame.pack(side=LEFT)
    rightFrame = Frame(basicRoot, height=500, width=200)
    rightFrame.pack(side=RIGHT, padx=60)

    titleLabel=Label(leftFrame, text="BASIC SETTINGS")
    titleLabel.pack(side=TOP)

    topbtns = Frame(rightFrame)
    topbtns.pack()
    rightbtns = Frame(topbtns)
    leftbtns = Frame(topbtns)
    leftbtns.pack(side=LEFT, pady=20)
    rightbtns.pack(pady=20)

    imgsun = "icons/sun.png"
    imgsun2 = Image.open(imgsun)
    imgsun3 = ImageTk.PhotoImage(image=imgsun2)
    sunBtn=Button(leftbtns, image=imgsun3)

    imgcld = "icons/cloud.png"
    imgcld2 = Image.open(imgcld)
    imgcld3 = ImageTk.PhotoImage(image=imgcld2)
    cloudBtn = Button(rightbtns, image=imgcld3)
    sunBtn.pack(side=TOP, pady=10, padx=10)
    cloudBtn.pack(side=TOP, pady=10, padx=10)

    imgevening = "icons/evening.png"
    imgevening2 = Image.open(imgevening)
    imgevening3 = ImageTk.PhotoImage(image=imgevening2)
    eveningBtn = Button(leftbtns, image=imgevening3, pady=10, padx=10)

    imgraining = "icons/rain.png"
    imgraining2 = Image.open(imgraining)
    imgraining3 = ImageTk.PhotoImage(image=imgraining2)
    rainyBtn = Button(rightbtns, image=imgraining3, pady=10, padx=10)
    eveningBtn.pack()
    rainyBtn.pack()

    #the top will show the video
    imageFrame = Frame(leftFrame)
    imageFrame.pack(side=BOTTOM, padx=10, pady=10)



    # Capture video frames
    lmain = Label(imageFrame)
    lmain.pack()
    cap = cv2.VideoCapture(0)



    advancedSettings= Button(rightFrame, text="ADVANCED SETTINGS")
    buttonsFrame = Frame(rightFrame)

    img = "icons/house_2.png"
    img2 = Image.open(img)
    img3 = ImageTk.PhotoImage(image=img2)
    home = Button(buttonsFrame, image=img3)

    imgbk = "icons/back.png"
    imgbk2 = Image.open(imgbk)
    imgbk3 = ImageTk.PhotoImage(image=imgbk2)
    back = Button(buttonsFrame, image=imgbk3)

    advancedSettings.pack(pady=10)
    buttonsFrame.pack()

    home.pack(side=LEFT, pady=10, padx=10)
    back.pack(pady=10, padx=10)

    def show_frame():
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

    show_frame()
    basicRoot.mainloop()

basic_settings()