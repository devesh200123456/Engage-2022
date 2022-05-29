from tkinter import*  #will import tkinter library
from tkinter import ttk
from tkinter.messagebox import askyesno #will import ttk some fascinating designs
from PIL import Image,ImageTk #import pillow
from Student import Student
import tkinter
from Train import Train
from face_recognition import face_recognition
import os

class F_rec_App: #declare a class name F_rec_App
    def __init__(self,root):   #to call constructer
        self.root=root
        self.root.geometry("1920x1080+0+0")  #to set window size and position
        self.root.title("Attendance System")  #set title

        bg=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\5605216.jpg")
        bg=bg.resize((1920,1080),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(bg)

        f_img=Label(self.root,image=self.bgimg)
        f_img.place(x=0,y=0,width=1920,height=1080)


        # vect=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\10.jpg")
        # vect=vect.resize((240,180),Image.ANTIALIAS)
        # self.vecimg=ImageTk.PhotoImage(vect)

        # v_img=Label(self.root,image=self.vecimg)
        # v_img.place(x=0,y=0,width=240,height=180)

        # vect1=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\13202.jpg")
        # vect1=vect1.resize((240,180),Image.ANTIALIAS)
        # self.vecimg1=ImageTk.PhotoImage(vect1)

        # v_img1=Label(self.root,image=self.vecimg1)
        # v_img1.place(x=260,y=0,width=240,height=180)

        # vect2=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\2.jpg")
        # vect2=vect2.resize((240,180),Image.ANTIALIAS)
        # self.vecimg2=ImageTk.PhotoImage(vect2)

        # v_img2=Label(self.root,image=self.vecimg2)
        # v_img2.place(x=500,y=0,width=240,height=180)

        # vect3=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\1.jpg")
        # vect3=vect3.resize((240,180),Image.ANTIALIAS)
        # self.vecimg3=ImageTk.PhotoImage(vect3)

        # v_img3=Label(self.root,image=self.vecimg3)
        # v_img3.place(x=750,y=0,width=240,height=180)

        # vect4=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\3.jpg")
        # vect4=vect4.resize((240,180),Image.ANTIALIAS)
        # self.vecimg4=ImageTk.PhotoImage(vect4)

        # v_img4=Label(self.root,image=self.vecimg4)
        # v_img4.place(x=1000,y=0,width=240,height=180)

        title_lbl=Label(f_img,text="Attendance System Application Using Face Recognition",font=("poppins",30,"bold"),bg="dark blue",fg="yellow")
        title_lbl.place(x=10,y=10,width=1250,height=50)


#button 1
        vect4=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\3.jpg")
        vect4=vect4.resize((240,180),Image.ANTIALIAS)
        self.vecimg4=ImageTk.PhotoImage(vect4)

        b1=Button(f_img,image=self.vecimg4,command=self.std_detailsbtn,cursor="hand2")
        b1.place(x=100,y=100,width=240,height=180)

        b1_1=Button(f_img,text="Student Details",command=self.std_detailsbtn,cursor="hand2",font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
        b1_1.place(x=100,y=280,width=240,height=40)



#button 2
        vect7=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\1.jpg")
        vect7=vect7.resize((240,180),Image.ANTIALIAS)
        self.vecimg5=ImageTk.PhotoImage(vect7)

        b2=Button(f_img,image=self.vecimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=240,height=180)

        b2_1=Button(f_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
        b2_1.place(x=500,y=280,width=240,height=40)



#button 3

        vect8=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\2.jpg")
        vect8=vect8.resize((240,180),Image.ANTIALIAS)
        self.vecimg6=ImageTk.PhotoImage(vect8)

        b3=Button(f_img,image=self.vecimg6,cursor="hand2")
        b3.place(x=900,y=100,width=240,height=180)

        b3_1=Button(f_img,text="Attendance",cursor="hand2",font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
        b3_1.place(x=900,y=280,width=240,height=40)


#button 4
        vect9=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\3.jpg")
        vect9=vect9.resize((240,180),Image.ANTIALIAS)
        self.vecimg7=ImageTk.PhotoImage(vect9)

        b5=Button(f_img,image=self.vecimg7,cursor="hand2",command=self.open_img)
        b5.place(x=100,y=400,width=240,height=180)

        b5_1=Button(f_img,text="Photos",cursor="hand2",command=self.open_img,font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
        b5_1.place(x=100,y=580,width=240,height=40)



#button 5
        vect10=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\1.jpg")
        vect10=vect10.resize((240,180),Image.ANTIALIAS)
        self.vecimg8=ImageTk.PhotoImage(vect10)

        b5=Button(f_img,image=self.vecimg8,cursor="hand2",command=self.train_data)
        b5.place(x=500,y=400,width=240,height=180)

        b5_1=Button(f_img,text="Train Data",cursor="hand2",command=self.train_data,font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
        b5_1.place(x=500,y=580,width=240,height=40)



#button 6

        vect11=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\2.jpg")
        vect11=vect11.resize((240,180),Image.ANTIALIAS)
        self.vecimg9=ImageTk.PhotoImage(vect11)

        b6=Button(f_img,image=self.vecimg9,cursor="hand2",command=self.iExit)
        b6.place(x=900,y=400,width=240,height=180)

        b6_1=Button(f_img,text="Exit",cursor="hand2",command=self.iExit,font=("poppins",12,"bold"),bg="dark blue",fg="yellow")
        b6_1.place(x=900,y=580,width=240,height=40)


    def open_img(self):
        os.startfile("Data")



    def std_detailsbtn(self):
        self.new_window=Toplevel(self.root)
        self.appopen=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.appopen=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.appopen=face_recognition(self.new_window)


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition Application","Are you Sure to Exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return 






if __name__ == "__main__":
    root=Tk()   #calling tool kit
    obj=F_rec_App(root)
    root.mainloop()