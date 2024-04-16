from tkinter import *
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('1174x680+0+0')
root.title("Scrollbar Widget Example")

# apply the grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
RightFrame=Frame(root,bg='black')
RightFrame.place(x=200,y=0,width=1300,height=1100)
text = tk.Text(RightFrame, height=20,width=10 ,bg='lightblue')
text.pack(side=TOP,fill=X)

# create a scrollbar widget and set its command to the text widget
scrollbar = ttk.Scrollbar(RightFrame, orient='vertical', command=text.yview)
scrollbar.pack(side=RIGHT,fill=Y)

#  communicate back to the scrollbar
text['yscrollcommand'] = scrollbar.set

# add sample text to the text widget to show the screen
position = f'{1}.0'
text.insert(position,'f''hey man\n'f'that is life\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n''hey jdfdkdd[fplpyou')

root.mainloop()