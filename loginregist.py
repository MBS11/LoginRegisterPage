from tkinter import *
from tkinter import messagebox as mb

import pymysql
n=pymysql.connect(host='localhost',user='root',password='',db='log')

window=Tk()
window.title("v")
a=Label(window,text="New Account? Register/Sign Up",width=30,font=("bold",20))
a.place(x=20,y=20)
b=Label(window,text="Existing User? Login",width=40,font=("bold",20))
b.place(x=520,y=20)

name=Label(window,text="Enter Name",width=10,font=("bold",10))
name.place(x=100,y=100)
c=Entry(window,bd=5)
c.place(x=200,y=100)
name1=Label(window,text="Enter Name",width=10,font=("bold",10))
name1.place(x=700,y=100)
c1=Entry(window,bd=5)
c1.place(x=800,y=100)

p=Label(window,text="Password",width=10,font=("bold",10))
p.place(x=100,y=150)
p1=Label(window,text="Password",width=10,font=("bold",10))
p1.place(x=700,y=150)
d=Entry(window,bd=5,show='*')
d.place(x=200,y=150)
d1=Entry(window,bd=5,show='*')
d1.place(x=800,y=150)

def reg():
    A=c.get()
    B=d.get()
    if(A=='' or B==''):
        if  mb.askyesno('Error','No Input Provided, Enter Again?'):
            mb.showinfo('Yes','Please Enter')
            
        else:
            mb.showwarning('No','Not Yet Implemented')
            window.destroy()
    else:
        m=n.cursor()
        sql="INSERT INTO `rg`(`Name`, `Password`) VALUES (%s,%s)"
        gg=(A,B)
        o=m.execute(sql,gg)
        mb.showinfo("Success","Registered Successfully")
        n.commit()
        c.delete(0,'end')
        d.delete(0,'end')
        
def sup():
    A=c1.get()
    B=d1.get()
    C=((A,B),)
    m=n.cursor()
    sql='SELECT * FROM `rg` WHERE `Name` LIKE %s AND `Password` LIKE %s'
    gg=(A,B)
    o=m.execute(sql,gg)
    r=m.fetchall()
    c1.delete(0,'end')
    d1.delete(0,'end')
    if r==C:
        mb.showinfo("Success","Login Successfull")
        win=Tk()
        win.title("Home")
        j=Label(win,text="Welcome",width=10,fg='blue',font=("bold",20))
        j.place(x=10,y=10)
        win.mainloop()   
    else:
        mb.showinfo("Login Failed","Incorrect Input")
        if  mb.askyesno('Error','Wrong Input Provided, Enter Again?'):
            mb.showinfo('Yes','Please Enter')
            
        else:
            mb.showwarning('No','Not Yet Implemented')
            window.destroy()
    n.commit
    
    
        
    
Button(window,text="Sign Up",bd=5,padx=10,command=reg).place(x=200,y=210)
Button(window,text="Log In",bd=5,padx=10,command=sup).place(x=800,y=210)






window.mainloop()
