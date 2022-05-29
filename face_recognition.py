from tkinter import*  #will import tkinter library
from tkinter import ttk #will import ttk some fascinating designs
from PIL import Image,ImageTk
# from cv2 import VideoCapture #import pillow
import mysql.connector
from time import strftime
from datetime import datetime
import os
from skimage import io
import numpy as np
import cv2


class face_recognition: #declare a class name F_rec_App
    def __init__(self,root):   #to call constructer
        self.root=root
        self.root.geometry("1920x1080+0+0")  #to set window size and position
        self.root.title("Attendance System")  #set title

        bg=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\56401.jpg")
        bg=bg.resize((1300,900),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(bg)

        f_img=Label(self.root,image=self.bgimg)
        f_img.place(x=0,y=0,width=1300,height=900)

        title_lbl=Label(f_img,text="Face Recognition",font=("poppins",30,"bold"),bg="dark blue",fg="orange")
        title_lbl.place(x=400,y=10,width=450,height=50)

        b1_1=Button(f_img,text="SCAN",cursor="hand2",command=self.face_recog,font=("poppins",12,"bold"),bg="dark blue",fg="orange")
        b1_1.place(x=162,y=602,width=240,height=40)




    def mark_attendance(self,i,j,k,l):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
                
            if((i not in name_list) and (j not in name_list) and (k not in name_list) and (l not in name_list)  ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.write(f"\n{i},{j},{k},{l},{dtString},{d1},Present")




    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            grey_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(grey_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                id,predict=clf.predict(grey_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))


                conn=mysql.connector.connect(host="localhost",username="root",password="@2001Devesh",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("Select Name from student where Admno="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("Select Dep from student where Admno="+str(id))
                j=my_cursor.fetchone()
                j="+".join(j)

                my_cursor.execute("Select Sem from student where Admno="+str(id))
                k=my_cursor.fetchone()
                k="+".join(k)

                my_cursor.execute("Select Admno from student where Admno="+str(id))
                l=my_cursor.fetchone()
                l="+".join(l)

                if confidence>75:
                    cv2.putText(img,f"Admno:{i}",(x,y-75),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"Name:{i}",(x,y-55),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"Dep:{j}",(x,y-30),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"Sem:{k}",(x,y-5),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.8,(255,0,0),3)
                    self.mark_attendance(i,j,k,l)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.8,(255,0,0),3)

                coord=[x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,0,0),"Face",clf)
            return img

        

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face is Recognizing",img)


            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()










if __name__ == "__main__":
    root=Tk()   #calling tool kit
    obj=face_recognition(root)
    root.mainloop()