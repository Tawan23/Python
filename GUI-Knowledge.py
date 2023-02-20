
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('700x500')


L1 = Label(GUI,text='โปรแกรมบันทึกข้อมูลของตะวัน',font=('Angsana New', 30),fg='green')
L1.place(x=30,y=20)

###########

def Button1():
    text = 'ชอบเขียนโปรแกรม'
    messagebox.showinfo('วิชาเรียนวันที่ 10/20/2023', text)
    
FB1 = LabelFrame(GUI, text='Button')
FB1.place(x=100,y=80)
B1 = ttk.Button(FB1,text='กดเพื่อเช็ข้อมูลส่วนตัว', command=Button1)
B1.pack(ipadx=20, ipady=20)

###########


###########

def Button2():
    text = 'Python 101, Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10/20/2023', text)

FB1 = LabelFrame(GUI, text='Button')
FB1.place(x=100,y=180)
B2 = ttk.Button(FB1,text='บทเรียน Python 101', command=Button2)
B2.pack(ipadx=20, ipady=20)

###########


###########

def Button3():
    text = 'บทเรียน Js'
    messagebox.showinfo('วิชาเรียนวันที่ 10/20/2023', text)
    
FB3 = LabelFrame(GUI, text='Button')
FB3.place(x=100,y=80)
B3 = ttk.Button(FB1,text='เขียนโปรแกรมด้วย Js', command=Button3)
B3.pack(ipadx=20, ipady=20)

###########


###########

def Button4():
    text = 'บทเรียน Css'
    messagebox.showinfo('วิชาเรียนวันที่ 10/20/2023', text)

FB4 = LabelFrame(GUI, text='Button')
FB4.place(x=100,y=180)
B4 = ttk.Button(FB1,text='ทำหน้าตาด้วน Css ', command=Button4)
B4.pack(ipadx=20, ipady=20)

###########

GUI.mainloop()
