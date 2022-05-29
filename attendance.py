from tkinter import*  #will import tkinter library
from tkinter import ttk
# from cProfile import label
# from curses.panel import bottom_panel
# from platform import release
# from turtle import width #will import ttk some fascinating designs
from PIL import Image,ImageTk #import pillow
from tkinter import messagebox
import mysql.connector
import cv2

class Student: #declare a class name F_rec_App
    def __init__(self,root):   #to call constructer
        self.root=root
        self.root.geometry("1920x1080+0+0")  #to set window size and position
        self.root.title("Attendance System")  #set title


        bg=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\5605216.jpg")
        bg=bg.resize((1920,1080),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(bg)

        f_img=Label(self.root,image=self.bgimg)
        f_img.place(x=0,y=0,width=1920,height=1080)

        title_lbl=Label(f_img,text="Attendance Sheet",font=("poppins",30,"bold"),bg="dark blue",fg="yellow")
        title_lbl.place(x=10,y=10,width=1250,height=50)


        m_frame=Frame(f_img,bd=2)
        m_frame.place(x=10,y=70,width=1250,height=600)

        l_frame=LabelFrame(m_frame,bd=2,bg="white",relief=GROOVE,text="Enter Student Details",font=("lemonmilk",10,"italic"))
        l_frame.place(x=30,y=10,width=550,height=550)


        r_frame=LabelFrame(m_frame,bd=2,bg="white",relief=GROOVE,text="Attendance Details",font=("lemonmilk",10,"italic"))
        r_frame.place(x=640,y=10,width=580,height=550)

if __name__ == "__main__":
    root=Tk()   #calling tool kit
    obj=Student(root)
    root.mainloop()