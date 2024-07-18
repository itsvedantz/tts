from tkinter import *
import tkinter.messagebox as tmsg
from ttkthemes import themed_tk as tk
import mysql.connector as mysql
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector

root = tk.ThemedTk()
root.get_themes()
root.set_theme("yaru")
root.geometry("1600x900+0+0")
root.title('REGISTRATION')

bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\Desktop\Final Year Project\project\reg_bg.jpg")
bg_lbl=Label(root,image=bg)
bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

bg1=ImageTk.PhotoImage(file=r"C:\Users\Admin\Desktop\Final Year Project\project\reg_left.png")
left_lbl=Label(root,image=bg1)
left_lbl.place(x=50,y=100,width=500,height=550)

frame=Frame(root,bg="white")
frame.place(x=550,y=100,width=800,height=550)

register_lbl=Label(frame,text="REGISTER HERE", font=("times new roman",15,"bold"),fg="green")
register_lbl.place(x=15,y=15)

def submit_data():
    fname = ffname_entry.get()
    lname = llname.get()
    email = txt_email.get()
    contact = phone.get()
    question = combo_question.get()
    answer = ans.get()
    password = pas.get()
    confirm = conf.get()


    if(fname=="" or lname=="" or contact=="" or email=="" or question=="" or answer=="" or password==""):
        tmsg.showinfo("Submit Status", "All fields are required")
    elif pas.get()!=conf.get():
        tmsg.showerror("Submit Status","PASSWORD AND CONFIRM PASSWORD DOES NOT MATCH")

    else:
        con = mysql.connector.connect(host="DESKTOP-3IQJJ7D", user="root", password="root", database="register") 
        cursor = con.cursor() 
        cursor.execute("insert into registered values('"+ fname +"', '"+ lname +"','"+ email +"', '"+ contact +"','"+ question +"', '"+ answer +"', '"+ password +"' )")
        cursor.execute("commit");

        ffname_entry.delete(0, 'end')
        llname.delete(0, 'end')
        txt_email.delete(0,'end')
        phone.delete(0, 'end')
        combo_question.delete(0, 'end')
        ans.delete(0, 'end')
        pas.delete(0, 'end')
        tmsg.showinfo("Submit Status", "Data Inserted Successfully")
        con.close();
        root.destroy()
        import log

def next_page():
    root.destroy()
    import log

fname=Label(frame, text="FIRST NAME",font=("times new roman",15,"bold"),bg="white")
fname.place(x=50,y=100)
ffname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
ffname_entry.place(x=50,y=130,width=250)

lname=Label(frame,text="LAST NAME",font=("times new roman",15,"bold"),bg="white")
lname.place(x=500,y=100)
llname=ttk.Entry(frame,font=("times new roman",15,"bold"))
llname.place(x=500,y=130,width=250)

email=Label(frame,text="EMAIL ID",font=("times new roman",15,"bold"),bg="white")
email.place(x=50,y=180)
txt_email=ttk.Entry(frame,font=("times new roman",15,"bold"))
txt_email.place(x=50,y=210,width=250)

contact=Label(frame,text="CONTACT",font=("times new roman",15,"bold"),bg="white")
contact.place(x=500,y=180)
phone=ttk.Entry(frame,font=("times new roman",15,"bold"))
phone.place(x=500,y=210,width=250)

question=Label(frame,text="SELECT SECURITY QUESTION",font=("times new roman",15,"bold"),bg="white")
question.place(x=50,y=260)
combo_question=ttk.Combobox(frame,font=("times new roman",15,"bold"),state="readonly")
combo_question["values"]=("Select","Your birth place","Your nickname","Your favourite movie")
combo_question.place(x=50,y=290,width=250)
combo_question.current(0)

answer=Label(frame,text="SECURITY ANSWER",font=("times new roman",15,"bold"),bg="white")
answer.place(x=500,y=260)
ans=ttk.Entry(frame,font=("times new roman",15,"bold"))
ans.place(x=500,y=290,width=250)

password=Label(frame,text="PASSWORD",font=("times new roman",15,"bold"),bg="white")
password.place(x=50,y=340)
pas=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
pas.place(x=50,y=370,width=250)

confirm=Label(frame,text="CONFIRM PASSWORD",font=("times new roman",15,"bold"),bg="white")
confirm.place(x=500,y=340)
conf=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
conf.place(x=500,y=370,width=250)

var_check=IntVar()
check=Checkbutton(frame,variable= var_check ,text="I Agree The Terms And Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
check.place(x=50,y=420)

submit = Button(frame, text="SUBMIT", font=("bolder", 10), relief=SUNKEN, bg="green", command=submit_data)
submit.place(x=50,y=480,width=150)

login= Label(frame, text="Already registered?",font=("times new roman",12,"bold"))
login.place(x=500, y=460)
submit = Button(frame, text="LOGIN", font=("bolder", 10,),bg="white", fg="blue", bd="0", cursor="hand2", activebackground="white"
                ,activeforeground="blue",command=next_page)
submit.place(x=500,y=480)

root.mainloop()