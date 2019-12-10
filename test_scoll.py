
import os, sys
if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    #from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

top = Tk()
top.geometry("1000x800")
canvas=Canvas(top,scrollregion=(0,0,520,120),bg="red") #创建canvas
canvas.place(x = 75, y = 265,width=200,height=500) #放置canvas的位置
frame=Frame(canvas,bg="blue") #把frame放在canvas里
frame.place(width=180, height=180) #frame的长宽，和canvas差不多的
vbar=Scrollbar(canvas,orient=VERTICAL) #竖直滚动条
vbar.place(x = 180,width=20,height=180)
vbar.configure(command=canvas.yview)
hbar=Scrollbar(canvas,orient=HORIZONTAL)#水平滚动条
hbar.place(x =0,y=165,width=180,height=20)
hbar.configure(command=canvas.xview)
canvas.config(xscrollcommand=hbar.set,yscrollcommand=vbar.set) #设置
canvas.create_window(0,0, window=frame,width=180,height=280)  #create_window
top.mainloop()