from tkinter import *
from tkinter import ttk
import cv2
from tkinter import PhotoImage
import tkinter as tk
import Tkinter
from PIL import Image, ImageTk



# Capture video frames

#left and right frames



cap = cv2.VideoCapture(0)


def sliders_settings():

    root= Tk()

    #title
    root.title("Advanced Settings")
    root.geometry('700x500')




    #video frame
    vidFrame = Frame(root)
    vidFrame.pack(side=LEFT)
    title= Label(vidFrame, text="Advanced Settings",justify=LEFT)
    title.grid(row=0, column=0,pady=(0,0), padx=10, sticky=W)
    lmain=tk.Label(vidFrame, relief=SUNKEN)
    lmain.grid(row=3, column=0, pady=(0,0), padx=(10,0),sticky=S+E+W)

    #slider frame
    slideFrame = Frame(root)
    slideFrame.pack(side=RIGHT)

    #entry
    name_label=Label(vidFrame, text="Name")
    name_entry= Entry(vidFrame)
    name_label.grid(row=1,column=0,sticky=W,padx=(10,0),pady=(20,0))
    name_entry.grid(row=2, column=0,sticky=W+E,padx=(10,200),pady=(0,0),columnspan=2)

    #images
    saveimg=ImageTk.PhotoImage(Image.open("save2.png"))
    homeimg=ImageTk.PhotoImage(Image.open("home.png"))
    backimg=ImageTk.PhotoImage(Image.open("back.png"))

    #buttons

    save=Button(vidFrame, width=32, height=32, image=saveimg, bg="gray")
    save.grid(row=2,column=0,padx=(225,0),pady=(0,20), sticky=W)

    home=Button(slideFrame,width=45, height=45, image=homeimg, bg="gray")
    home.grid(row=6,column=0,padx=(0,150),pady=(40,0),sticky=E)

    back=Button(slideFrame,width=45, height=45, image=backimg, bg="gray")
    back.grid(row=6,column=0,padx=(150,70),pady=(40,0), sticky=E)

    #sliders
    slide1= Scale(slideFrame, from_=0, to=255, orient=HORIZONTAL, label="Saturation", length=200)
    slide1.grid(row=0,column=0, sticky=N+E, padx=(0,30),pady=0)

    slide2= Scale(slideFrame, from_=0, to=255, orient=HORIZONTAL, label="Hue", length=200)
    slide2.grid(row=1,column=0, sticky=N+E, padx=(0,30),pady=0)

    slide3= Scale(slideFrame, from_=0, to=255, orient=HORIZONTAL, label="Brightness", length=200)
    slide3.grid(row=2,column=0, sticky=N+E, padx=(0,30),pady=0)

    slide4= Scale(slideFrame, from_=0, to=255, orient=HORIZONTAL, label="Convolution", length=200)
    slide4.grid(row=3,column=0, sticky=N+E, padx=(0,30),pady=0)


    slide5= Scale(slideFrame, from_=0, to=255, orient=HORIZONTAL, label="etc1", length=200)
    slide5.grid(row=4,column=0, sticky=N+E, padx=(0,30),pady=0)

    slide6= Scale(slideFrame, from_=0, to=255, orient=HORIZONTAL, label="etc2", length=200)
    slide6.grid(row=5,column=0, sticky=N+E, padx=(0,30),pady=0)





    def show_frame():
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2image=cv2.resize(cv2image,(400,350))
        #in the future, loop to another function to adjust image from here
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

    show_frame()
    root.mainloop()

sliders_settings()






