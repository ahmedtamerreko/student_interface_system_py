from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk
def login():
    if IDentry.get() =='' or passwordentry.get() =='':
        messagebox.showerror('Error', 'Please Fill the Empty Fields')
    elif IDentry.get() == '1' and passwordentry.get() =='1':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import SMS
    else:
        messagebox.showerror('Error','Sorry maybe Your Username or Passward is Uncorrect')




window = Tk()
window.title('Student Management System')
window.geometry('1480x1280+0+0')

BackgroundImage=ImageTk.PhotoImage(file='student.jpg')
BackgroundLabel=Label(window,image=BackgroundImage)
BackgroundLabel.place(x=0, y=0)

frame=Frame(window,bg='gold')
frame.place(x=150 , y=100)

logo=PhotoImage(file='studentlogo.png')
logolabel=Label(frame,image=logo)
logolabel.grid(row=0,column=1,columnspan=2,pady=10)
usernameimage =PhotoImage(file='id-card.png')
usernamelabel = Label(frame,image=usernameimage,text='ID',font=('times new roman',20,'bold'),bg='gold',compound=LEFT)
usernamelabel.grid(row=2,column=0,pady=10)
password=PhotoImage(file = 'padlock.png')
Passwordlabel=Label(frame,image=password,text='Password',font=('times new roman',20,'bold'),bg='gold',compound=LEFT)
Passwordlabel.grid(row=5,column=0,pady=10,padx=50)
IDentry=Entry(frame,font=('times new roman', 20,'bold'),bd=2,fg='royalblue')
IDentry.grid(row=2 , column=1)
passwordentry=Entry(frame,font=('times new roman', 20,'bold'),bd=2,fg='royalblue')
passwordentry.grid(row= 5,column=1,pady=10,padx=50)
loginbutton=Button(frame,text='Login',font=('Arial',25,'italic bold'),bg='lightgreen',width=10,activebackground='green',cursor='hand2',command=login)
loginbutton.grid(row=6,column = 1,padx=10,pady=10)
window.mainloop()
