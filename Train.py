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
import os
import numpy as np


class Train: #declare a class name F_rec_App
    def __init__(self,root):   #to call constructer
        self.root=root
        self.root.geometry("500x500+0+0")  #to set window size and position
        self.root.title("Attendance System")  #set title


        bg=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\5605216.jpg")
        bg=bg.resize((1920,1080),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(bg)

        f_img=Label(self.root,image=self.bgimg)
        f_img.place(x=0,y=0,width=1920,height=1080)

        b1_1=Button(f_img,text="Train Data",command=self.train_classifier,cursor="hand2",font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
        b1_1.place(x=100,y=280,width=240,height=40)

        title_lbl=Label(f_img,text="Train your Dataset",font=("poppins",30,"bold"),bg="dark blue",fg="yellow")
        title_lbl.place(x=10,y=100,width=450,height=50)


    def train_classifier(self):
        data_dir=("data")
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path :
            img=Image.open(image).convert('L')
            image_np=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training",image_np)
            cv2.waitKey(1)==13

        ids=np.array(ids)


        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("outcome","datasets are trained successfully")



if __name__ == "__main__":
    root=Tk()   #calling tool kit
    obj=Train(root)
    root.mainloop()