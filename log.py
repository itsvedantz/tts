from tkinter import *
import tkinter.messagebox as tmsg
from ttkthemes import themed_tk as tk
import mysql.connector as mysql
from tkinter import ttk
from PIL import ImageTk
import mysql.connector
from trans import trans 

root = tk.ThemedTk()
root.get_themes()
root.set_theme("yaru")
root.geometry("1600x900+0+0")
root.title("Login Form")

bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\Desktop\Final Year Project\project\reg_bg.jpg")
lbl_bg=Label(root,image=bg)
lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

frame=Frame(root,bg="black")
frame.place(x=610,y=170,width=340,height=450)

get_str=Label(frame,text="!!! LOGIN HERE !!!",font=("times new roman",20,"bold"),fg="white",bg="black")
get_str.place(x=50,y=20)

def fetch_data():
    if (txt_email.get() == "" or pas.get()==""):
        tmsg.showinfo("Fetch Status", "PLEASE FILL ALL DETAILS")
    else:
        con = mysql.connector.connect(host="DESKTOP-3IQJJ7D", user="root", password="root", database="register") 
        cursor = con.cursor()  
        cursor.execute("select * from registered where email = ('" + txt_email.get() + "')")
        rows = cursor.fetchall()

        for row in rows:
            if(txt_email.get()==row[2] and pas.get()==row[6]):
                tmsg.showinfo("Fetch Status", "YOU ARE LOGGED IN")
                root.destroy()  
                trans_window = Tk()  
                trans_page = trans(trans_window) 
                trans_window.mainloop() 
                break

            elif(txt_email.get()!=row[2] or pas.get()!=row[6]):
                tmsg.showinfo("Fetch Status", "EMAIL AND PASSWORD DO NOT MATCH")
        con.close()

def forgot_pass():
    def change_pass():
        if txt_email.get()=="" or npas.get()=="" or cpas=="":
            tmsg.showerror("Error","ALL FIELDS ARE REQUIRED !!!")
        elif cpas.get()!=npas.get():
            tmsg.showerror("Eror","PASSWORD AND CONFIRM PASSWORD MUST BE SAME")
        else:
            con = mysql.connector.connect(host="DESKTOP-3IQJJ7D", user="root", password="root", database="register")  
            cursor = con.cursor() 
            cursor.execute("select * from registered where email = ('" + txt_email.get() + "')")
            row=cursor.fetchone()
            if row==None:
                tmsg.showerror("error","enter correct answer")
            else:
                cursor.execute("update registered set password=%s where email=%s",(npas.get(), txt_email.get()))
                con.commit()
                con.close()
                tmsg.showinfo("info","your password has been reset")

    window=Toplevel()
    window.geometry("450x400+530+200")
    window.title('Forget Password')

    bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\Desktop\Final Year Project\project\BG.jpg")
    bg_lbl=Label(window,image=bg)
    bg_lbl.grid()

    get_str=Label(window,text="!!! CREATE NEW PASSWORD !!!",font=("times new roman",20,"bold"),fg="white",bg="black")
    get_str.place(x=20,y=20)

    email=Label(window,text="EMAIL ID",font=("times new roman",15,"bold"),bg="black",fg="white")
    email.place(x=180,y=110)
    txt_email=ttk.Entry(window,font=("times new roman",15,"bold"))
    txt_email.place(x=100,y=140,width=250)

    npassword=Label(window,text="NEW PASSWORD",font=("times new roman",15,"bold"),bg="black", fg="white")
    npassword.place(x=140,y=190)
    npas=ttk.Entry(window,show="*",font=("times new roman",15,"bold"))
    npas.place(x=100,y=220,width=250)

    cpassword=Label(window,text="CONFIRM NEW PASSWORD",font=("times new roman",15,"bold"),bg="black", fg="white")
    cpassword.place(x=100,y=270)
    cpas=ttk.Entry(window,show="*",font=("times new roman",15,"bold"))
    cpas.place(x=100,y=300,width=250)

    submit = Button(window, text="RESET", font=("italic", 10), relief=SUNKEN, bg="SKY BLUE", command=change_pass)
    submit.place(x=150,y=350,width=150)

    window.mainloop()

def new_page():
    root.destroy()
    import LogReg

email=Label(frame,text="EMAIL ID",font=("times new roman",15,"bold"),bg="black",fg="white")
email.place(x=50,y=110)
txt_email=ttk.Entry(frame,font=("times new roman",15,"bold"))
txt_email.place(x=50,y=140,width=250)

password=Label(frame,text="PASSWORD",font=("times new roman",15,"bold"),bg="black", fg="white")
password.place(x=50,y=190)
pas=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
pas.place(x=50,y=220,width=250)

forgot=Button(frame,command=forgot_pass,text="FORGOT PASSWORD",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="red",activeforeground="white",activebackground="black")
forgot.place(x=90,y=300,width=160)

submit = Button(frame, text="LOGIN", font=("italic", 10), relief=SUNKEN, bg="sky blue", command=fetch_data)
submit.place(x=95,y=350,width=150)

submit = Button(frame, text="REGISTER", font=("bolder", 10,),bg="black", fg="blue", bd="0", cursor="hand2", activebackground="white"
                ,activeforeground="blue",command=new_page)
submit.place(x=140,y=400)

root.mainloop()