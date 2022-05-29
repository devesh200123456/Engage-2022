
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


        self.var_dep=StringVar()
        self.var_prog=StringVar()
        self.var_sem=StringVar()
        self.var_admno=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_cont=StringVar()




        bg=Image.open(r"C:\Users\Devesh Ranjan\Desktop\pythonn\New folder\5605216.jpg")
        bg=bg.resize((1920,1080),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(bg)

        f_img=Label(self.root,image=self.bgimg)
        f_img.place(x=0,y=0,width=1920,height=1080)

        title_lbl=Label(f_img,text="Enter & Manage Student Details",font=("poppins",30,"bold"),bg="dark blue",fg="yellow")
        title_lbl.place(x=10,y=10,width=1250,height=50)


        m_frame=Frame(f_img,bd=2)
        m_frame.place(x=10,y=70,width=1250,height=600)


        l_frame=LabelFrame(m_frame,bd=2,bg="white",relief=GROOVE,text="Enter Student Details",font=("lemonmilk",10,"italic"))
        l_frame.place(x=30,y=10,width=550,height=550)

        c_frame=LabelFrame(l_frame,bd=2,bg="white",relief=GROOVE,text="Enter Your Course Details",font=("lemon milk",10,"italic"))
        c_frame.place(x=40,y=10,width=450,height=150)

        dep_label=Label(c_frame,text="Department",font=("lemonmilk",10,"italic"),bg="white")
        dep_label.grid(row=0,column=0,padx=5,pady=10)

        dep_combo=ttk.Combobox(c_frame,textvariable=self.var_dep,font=("lemonmilk",10,"italic"),width=25,state='readonly',)
        dep_combo["values"]=("Select Department","Petroleum Engineering","Computer Science and Engineering","Electronics and Communication Engineering","Electrical Engineering","Mechanical Engineering","Civil Engineering","Chemical Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        prog_label=Label(c_frame,text="Programme",font=("lemonmilk",10,"italic"),bg="white")
        prog_label.grid(row=1,column=0,padx=5,pady=10)

        prog_combo=ttk.Combobox(c_frame,textvariable=self.var_prog,font=("lemonmilk",10,"italic"),width=25,state='readonly',)
        prog_combo["values"]=("Select Programme","Bachelor of Technology","Master of Technology","Bachelor of Engineering")
        prog_combo.current(0)
        prog_combo.grid(row=1,column=1,padx=5,pady=10)

        sem_label=Label(c_frame,text="Semester",font=("lemonmilk",10,"italic"),bg="white")
        sem_label.grid(row=2,column=0,padx=5,pady=10)

        sem_combo=ttk.Combobox(c_frame,textvariable=self.var_sem,font=("lemonmilk",10,"italic"),width=25,state='readonly',)
        sem_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=2,column=1,padx=5,pady=10)



        student_frame=LabelFrame(l_frame,bd=2,bg="white",relief=GROOVE,text="Student Information",font=("lemon milk",10,"italic"))
        student_frame.place(x=40,y=180,width=450,height=330)

        admno_label=Label(student_frame,text="Admission Number",font=("lemonmilk",10,"italic"),bg="white")
        admno_label.grid(row=0,column=0,padx=5,pady=15)

        admno_entry=ttk.Entry(student_frame,textvariable=self.var_admno,width=25,font=("lemonmilk",10,"italic"))
        admno_entry.grid(row=0,column=1,padx=5,pady=15)

        name_label=Label(student_frame,text="Name",font=("lemonmilk",10,"italic"),bg="white")
        name_label.grid(row=1,column=0,padx=5,pady=15)

        name_entry=ttk.Entry(student_frame,textvariable=self.var_name,width=25,font=("lemonmilk",10,"italic"))
        name_entry.grid(row=1,column=1,padx=5,pady=15)

        email_label=Label(student_frame,text="Email",font=("lemonmilk",10,"italic"),bg="white")
        email_label.grid(row=2,column=0,padx=5,pady=15)

        email_entry=ttk.Entry(student_frame,textvariable=self.var_email,width=25,font=("lemonmilk",10,"italic"))
        email_entry.grid(row=2,column=1,padx=5,pady=15)

        mobno_label=Label(student_frame,text="Contact Number",font=("lemonmilk",10,"italic"),bg="white")
        mobno_label.grid(row=3,column=0,padx=5,pady=15)

        mobno_entry=ttk.Entry(student_frame,textvariable=self.var_cont,width=25,font=("lemonmilk",10,"italic"))
        mobno_entry.grid(row=3,column=1,padx=5,pady=15)


        
        self.var_rdb1=StringVar()
        rdb1=ttk.Radiobutton(student_frame,text="Take a photo sample",variable=self.var_rdb1,value="Yes")
        rdb1.grid(row=4,column=0,padx=5,pady=0)


        rdb2=ttk.Radiobutton(student_frame,text="Take a photo sample",variable=self.var_rdb1,value="No")
        rdb2.grid(row=4,column=1,padx=5,pady=0)

        btn_frame=Frame(student_frame,bd=2,relief=GROOVE,bg="white")
        btn_frame.place(x=0,y=230,width=446,height=40)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=11,font=("lemonmilk",10,"italic"),bg="black",fg="white")
        save_btn.grid(row=0,column=0,padx=5,pady=2)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=11,font=("lemonmilk",10,"italic"),bg="black",fg="white")
        update_btn.grid(row=0,column=1,padx=5,pady=2)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=11,font=("lemonmilk",10,"italic"),bg="black",fg="white")
        delete_btn.grid(row=0,column=2,padx=5,pady=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=11,font=("lemonmilk",10,"italic"),bg="black",fg="white")
        reset_btn.grid(row=0,column=3,padx=5,pady=2)

        btn1_frame=Frame(student_frame,bd=2,relief=GROOVE,bg="white")
        btn1_frame.place(x=0,y=275,width=446,height=35)

        take_img_btn=Button(btn1_frame,command=self.generate_dataset,text="Take Image Sample",width=25,font=("lemonmilk",10,"italic"),bg="black",fg="white")
        take_img_btn.grid(row=0,column=0,padx=5,pady=2)

        Update_btn=Button(btn1_frame,text="Update Image",width=25,font=("lemonmilk",10,"italic"),bg="black",fg="white")
        Update_btn.grid(row=0,column=1,padx=5,pady=2)
        



        r_frame=LabelFrame(m_frame,bd=2,bg="white",relief=GROOVE,text="Student Details",font=("lemonmilk",10,"italic"))
        r_frame.place(x=640,y=10,width=580,height=550)


        detail_frame=LabelFrame(r_frame,bd=2,bg="white",relief=GROOVE,text="Search Your Details",font=("lemonmilk",10,"italic"))
        detail_frame.place(x=40,y=10,width=500,height=70)

        detail_label=Label(detail_frame,text="Search Using",font=("lemonmilk",10,"italic"),bg="white")
        detail_label.grid(row=0,column=0,padx=5,pady=15)

        search_combo=ttk.Combobox(detail_frame,font=("lemonmilk",10,"italic"),width=10,state='readonly')
        search_combo["values"]=("Select","Admission No.","Mobile No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)


        search_entry=ttk.Entry(detail_frame,width=17,font=("lemonmilk",10,"italic"))
        search_entry.grid(row=0,column=2,padx=5,pady=15)
        
        search_btn=Button(detail_frame,text="Search",width=7,font=("lemonmilk",10,"italic"),bg="black",fg="white")
        search_btn.grid(row=0,column=3,padx=5,pady=2)

        showall_btn=Button(detail_frame,text="Show All",width=7,font=("lemonmilk",10,"italic"),bg="black",fg="white")
        showall_btn.grid(row=0,column=4,padx=5,pady=2)


        tbl_frame=Frame(r_frame,bd=2,bg="white",relief=GROOVE)
        tbl_frame.place(x=40,y=90,width=500,height=320)


        scroll_x=ttk.Scrollbar(tbl_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tbl_frame,orient=VERTICAL)

        self.std_table=ttk.Treeview(tbl_frame,columns=("dep","prog","sem","admno","name","email","cont"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.std_table.xview)
        scroll_y.config(command=self.std_table.yview)



        self.std_table.heading("dep",text="Department")
        self.std_table.heading("prog",text="Programme")
        self.std_table.heading("sem",text="Semester")
        self.std_table.heading("admno",text="Admission No.")
        self.std_table.heading("name",text="Name")
        self.std_table.heading("email",text="Email")
        self.std_table.heading("cont",text="Contact")

        self.std_table.column("dep",width=100)
        self.std_table.column("prog",width=100)
        self.std_table.column("sem",width=100)
        self.std_table.column("admno",width=100)
        self.std_table.column("name",width=100)
        self.std_table.column("email",width=100)
        self.std_table.column("cont",width=100)
        
        self.std_table.pack(fill=BOTH,expand=1)
        self.std_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_prog.get()=="Select Programme" or self.var_sem.get()=="Select Semester" or self.var_admno.get()=="" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_cont.get()=="" :
            messagebox.showerror("Error", "Please fill all options",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@2001Devesh",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Student Value(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                        self.var_dep.get(),
                                                                                        self.var_prog.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_admno.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_cont.get()
                                                                        
                                                                                    ))
                conn.commit()
                self.fetch()
                conn.close
                messagebox.showinfo("Success","Student Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@2001Devesh",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from Student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.std_table.delete(*self.std_table.get_children())
            for i in data:
                self.std_table.insert("",END,value=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_focus=self.std_table.focus()
        content=self.std_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_prog.set(data[1])
        self.var_sem.set(data[2])
        self.var_admno.set(data[3])
        self.var_name.set(data[4])
        self.var_email.set(data[5])
        self.var_cont.set(data[6])

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_prog.get()=="Select Programme" or self.var_sem.get()=="Select Semester" or self.var_admno.get()=="" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_cont.get()=="" :
            messagebox.showerror("Error", "Please fill all options",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this Student Details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="@2001Devesh",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Prog=%s,Sem=%s,Name=%s,Email=%s,Contact=%s where Admno=%s",(
                                                                                                                                            self.var_dep.get(),
                                                                                                                                            self.var_prog.get(),
                                                                                                                                            self.var_sem.get(),
                                                                                                                                            self.var_name.get(),
                                                                                                                                            self.var_email.get(),
                                                                                                                                            self.var_cont.get(),
                                                                                                                                            self.var_admno.get()
                                                                                                                                        ))
                else:
                    if not Update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Updated Successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_admno.get()=="":
            messagebox.showerror("Error","Student id must be Required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="@2001Devesh",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from Student List where Admno=%s"
                    val=(self.var_admno.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted Student",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_sem.set("Select Semester")
        self.var_prog.set("Set Programme")
        self.var_admno.set("")
        self.var_email.set("")
        self.var_name.set("")
        self.var_cont.set("")
            



    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_prog.get()=="Select Programme" or self.var_sem.get()=="Select Semester" or self.var_admno.get()=="" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_cont.get()=="" :
            messagebox.showerror("Error", "Please fill all options",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@2001Devesh",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    my_cursor.execute("update student set Dep=%s,Prog=%s,Sem=%s,Name=%s,Email=%s,Contact=%s where Admno=%s",(
                                                                                                                                            self.var_dep.get(),
                                                                                                                                            self.var_prog.get(),
                                                                                                                                            self.var_sem.get(),
                                                                                                                                            self.var_name.get(),
                                                                                                                                            self.var_email.get(),
                                                                                                                                            self.var_cont.get(),
                                                                                                                                            self.var_admno.get()==id+1
                                                                                                                            ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    face_classifier=cv2.CascadeClassifier("C:\\Users\\Devesh Ranjan\\Desktop\\pythonn\\haarcascade_frontalface_default.xml")
                    
                    def face_crop(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)

                        for(x,y,w,h) in faces:
                            face_crop=img[y:y+h,x:x+w]
                            return face_crop
                        
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if  face_crop(my_frame) is not None:
                            img_id+=1
                        face=cv2.resize(face_crop(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_TRIPLEX,2,(255,0,0),2)
                        cv2.imshow("Your Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Data sets generated")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                




if __name__ == "__main__":
    root=Tk()   #calling tool kit
    obj=Student(root)
    root.mainloop()