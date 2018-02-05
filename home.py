from tkinter import *
from tkinter import ttk
import cv2
from tkinter import PhotoImage
import tkinter as tk
import tkinter
from PIL import Image, ImageTk
from Basic_Settings import basic_settings
import time


def main_screen():
    # Capture video frames

    #left and right frames


    width, height=500,400
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)



    root= Tk()

    root.title("Home")
    root.geometry('700x500')

    vidFrame = Frame(root)
    vidFrame.pack(side=LEFT)
    title= Label(vidFrame, text="Home",justify=LEFT)

    title.grid(row=0, column=0, pady=10, padx=10)



    lmain=tk.Label(vidFrame, relief=SUNKEN)
    lmain.grid(row=1, column=0, pady=0, padx=(10,0), rowspan=2, sticky=S)
    #cap=cv2.VidepCapture(0)
    #buttonsFrame = Frame (root)
    #buttonsFrame.pack(side=RIGHT)



    #images
    settimg=ImageTk.PhotoImage(Image.open("icons/set.png"))
    powerimg=ImageTk.PhotoImage(Image.open("icons/powerw.png"))

    show = True

    #define a function that shuts down the program
    def exitProgram(event):
        print("Exiting")
        vidFrame.master.destroy()
        cv2.destroyAllWindows()

    def change_basic(event):
        global show
        show = False
        print("change")
        vidFrame.master.destroy()
        cv2.destroyAllWindows()
        basic_settings()

    #buttons
    settings =Button(vidFrame, width=64, height=64, image=settimg,bg= "gray")
    power =Button(vidFrame, width=64, height=64, image=powerimg,bg="gray")
    power.bind("<Button 1>", exitProgram) #connect button to shutdown
    settings.bind("<Button 1>", change_basic)
    power.bind("<Button 1>", )

    power.grid(row=1, column=1, padx=(10,45),pady=(30,50))
    settings.grid(row=1, column=1,padx=(10,45),pady=(150,0))



    def show_frame():
        if (show == True):
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            cv2image=cv2.resize(cv2image,(590,440))
            #in the future, loop to another function to adjust image from here
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(10, show_frame)

    show_frame()
    root.mainloop()

main_screen()


