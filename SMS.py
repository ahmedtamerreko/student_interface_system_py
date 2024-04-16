from tkinter import *
from tkinter import ttk
import ttkthemes

def regis():
    import Drop_Down_Menu


root = ttkthemes.ThemedTk()
root.title('Student Management System')
root.geometry('1174x680+0+0')
root.get_themes()
root.set_theme('kroc')
leftframe=Frame(root,bg='gold')
leftframe.place(x=0 , y=0,width=200,height=900)

Registerbutton = ttk.Button(leftframe,text='Register courses?',width=20,command=regis)
Registerbutton.grid(row = 10,column= 7,pady=30,padx=30)

#Regasterbutton = ttk.Button(leftframe,text='Regaster Course',width=20)
#Regasterbutton.grid(row = 20,column= 7,pady=30,padx=30)

#Editbutton = ttk.Button(leftframe,text=' Edit courses',width=20)
#Editbutton.grid(row = 30,column= 7,pady=30,padx=30)

#Choose_Groupbutton = ttk.Button(leftframe,text='Choose Group',width=20)
#Choose_Groupbutton.grid(row = 40,column= 7,pady=30,padx=30)

RightFrame=Frame(root,bg='black')
RightFrame.place(x=200,y=640,width=1300,height=1100)
#treeview=ttk.Treeview(RightFrame)
#treeview.place(x=0,y=0,width=1200,height=820)
Bottomframe=Frame(root,bg='red')
Bottomframe.place(x=200,y=0,width=1250,height=200)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
RightFrame=Frame(root,bg='black')
RightFrame.place(x=200,y=180)
text = Text(RightFrame, height=20,width=84,bg='light green',font=('Arial',20,'bold'))
text.pack(side=RIGHT,fill=Y)

# create a scrollbar widget and set its command to the text widget
scrollbar = ttk.Scrollbar(RightFrame, orient='vertical', command=text.yview)
scrollbar.pack(side=RIGHT,fill=Y)

#  communicate back to the scrollbar
text['yscrollcommand'] = scrollbar.set

# add sample text to the text widget to show the screen
position = f'{1}.0'
text.insert(position,'hey you\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nlook there\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nyou are good person')
