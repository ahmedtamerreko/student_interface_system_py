
from tkinter import *
from tkinter import ttk

Droproot=Tk()
Droproot.resizable(False,False)
dropdownmenuframe=Frame(Droproot,bg='red')
dropdownmenuframe.place(x=0,y=0)
groupchoices=['A','B']
subjectschoices=['Math 0','Math 1','Math 2','Technical Report Writing','Computer Science','Electronics','Creative Thinking','OOP','English','None']
Grouptextlabel=Label(Droproot,text='Choose your Group',font=('Arial',20,'italic bold'))
Grouptextlabel.pack(padx=10)
GroupMenu=ttk.Combobox(Droproot,values=groupchoices)
GroupMenu.pack(padx=10)
Grouptextlabel1=Label(Droproot,text='Choose your Courses',font=('Arial',20,'italic bold'))
Grouptextlabel1.pack(padx=10)
GroupMenu1=ttk.Combobox(Droproot,values=subjectschoices)
GroupMenu1.pack(padx=10)
GroupMenu2=ttk.Combobox(Droproot,values=subjectschoices)
GroupMenu2.pack(padx=10)
GroupMenu3=ttk.Combobox(Droproot,values=subjectschoices)
GroupMenu3.pack(padx=10)
GroupMenu4=ttk.Combobox(Droproot,values=subjectschoices)
GroupMenu4.pack(padx=10)
GroupMenu5=ttk.Combobox(Droproot,values=subjectschoices)
GroupMenu5.pack(padx=10)
GroupMenu6=ttk.Combobox(Droproot,values=subjectschoices)
GroupMenu6.pack(padx=10)
GroupMenu7=ttk.Combobox(Droproot,values=subjectschoices)
GroupMenu7.pack(padx=10)

SubmitButton=Button(Droproot,text='Submit',bg='light green',font=('Arial',20,'italic bold'))
SubmitButton.pack(padx=10,pady=10)




Droproot.mainloop()