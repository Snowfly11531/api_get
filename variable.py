#!/usr/bin/env python
#-*- coding:utf-8 -*-

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

class VariableFrame_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        print(type(master))
        self.sb=Scrollbar(self.frame)
        self.sb.pack(side=RIGHT,fill=Y)
        self.frame=Frame(master,bg="red",yscrollcommand= self.sb.set)
        print(type(self.frame))
        super().__init__(master)
        self.createWidgets()
        self.frame.place(relx=0.5,rely=0.5,width=100,height=50)



    def createWidgets(self):

        print("haha")
        #self.style = Style()
        self.Label1Var = StringVar(value='Label1')
        #self.style.configure('TLabel1.TLabel', anchor='w', font=('宋体',9))
        self.Label1 = Label(self.frame, text='Label1', textvariable=self.Label1Var)
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(x=0,y=0,width=30)



        self.sb=Scrollbar(self.frame)
        self.sb.pack(side=RIGHT,fill=Y)

        # self.Text1Var = StringVar(value='Text1')
        # self.Text1 = Entry(self.frame, textvariable=self.Text1Var, font=('宋体',9),width=10)
        # self.Text1.setText = lambda x: self.Text1Var.set(x)
        # self.Text1.text = lambda : self.Text1Var.get()
        # self.Label1.place(x=13,y=13)
        #
        # self.Command1Var = StringVar(value='Command1')
        # #self.style.configure('TCommand1.TButton', font=('宋体',9))
        # self.Command1 = Button(self.frame, text='Command1', textvariable=self.Command1Var, command=self.Command1_Cmd,width=10,height=2)
        # self.Command1.setText = lambda x: self.Command1Var.set(x)
        # self.Command1.text = lambda : self.Command1Var.get()
        # self.Label1.place(x=26,y=13)


class VariableFrame(VariableFrame_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        super().__init__(master)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    top.geometry("400x300")
    frame1=VariableFrame(top)
    top.mainloop()

