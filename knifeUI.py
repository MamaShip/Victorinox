#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #from tkinter.filedialog import askopenfilename
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #from tkinter.filedialog import askopenfilename
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()


class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Listen's Victorinox")
        self.master.geometry('589x339')
        self.createWidgets()
 
    def createWidgets(self):
        self.top = self.winfo_toplevel()
 
        self.style = Style()
 
        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0.062, rely=0.071, relwidth=0.887, relheight=0.876)
 #first tab
        self.TabStrip1__Tab1 = Frame(self.TabStrip1)

        self.TabStrip1__Tab1Lbl = Label(self.TabStrip1__Tab1)
        self.TabStrip1__Tab1Lbl.place(relx=0.1,rely=0.5)

        self.TabStrip1__Tab1Title = Label(self.TabStrip1__Tab1,text='page                         wl',font='Times 12 normal')
        self.TabStrip1__Tab1Title.pack(side=TOP)

        self.TabStrip1__Tab1frm = Frame(self.TabStrip1__Tab1)

        self.TabStrip1__Tab1PageNum = Entry(self.TabStrip1__Tab1frm)#, bd = 5,relief=SUNKEN)
        self.TabStrip1__Tab1PageNum.pack(side=LEFT)

        self.TabStrip1__Tab1frmB = Frame(self.TabStrip1__Tab1frm)
        # Page to WL
        self.TabStrip1__Tab1WL_Button = Button(self.TabStrip1__Tab1frmB,text=" → ")#,bd = 5,relief=RIDGE)
        self.TabStrip1__Tab1WL_Button.pack(side=TOP)
        # WL to Page
        self.TabStrip1__Tab1Page_Button = Button(self.TabStrip1__Tab1frmB,text=" ← ")#,bd = 5,relief=RIDGE)
        self.TabStrip1__Tab1Page_Button.pack(side=TOP)

        self.TabStrip1__Tab1frmB.pack(side=LEFT)

        self.TabStrip1__Tab1WLNum = Entry(self.TabStrip1__Tab1frm)#, bd = 5,relief=SUNKEN)
        self.TabStrip1__Tab1WLNum.pack(side=LEFT)

        self.TabStrip1__Tab1frm.pack(side=TOP)

        self.TabStrip1.add(self.TabStrip1__Tab1, text='Page_WL')
 #first tab end
 #second tab
        self.Tab2 = Frame(self.TabStrip1)
        self.Tab2ButtonRun = Button(self.Tab2, text = "Run")
        self.Tab2ButtonRun.place(relx=0.4,rely=0.5)
        self.TabStrip1.add(self.Tab2, text='Option Checker')
 #second tab end
 #third tab
        self.Tab3 = Frame(self.TabStrip1)

        self.Tab3Lbl1 = Label(self.Tab3, text = "依次选择需要link的文件(确认)，最后按合并")#.grid(row = 0, column = 0)
        self.Tab3Lbl1.pack(side=TOP)

        self.Tab3frm = Frame(self.Tab3)
        
        self.Tab3Lbl2 = Label(self.Tab3frm,text = "目标路径:")#.grid(row = 1, column = 0)
        self.Tab3Lbl2.pack(side=LEFT)
        self.Tab3pathEntry = Entry(self.Tab3frm)#.grid(row = 1, column = 1)
        self.Tab3pathEntry.pack(side=LEFT)
        self.Tab3ButtonSelect = Button(self.Tab3frm, text = "文件选择")#.grid(row = 1, column = 2)
        self.Tab3ButtonSelect.pack(side=LEFT)
        self.Tab3ButtonConfirm = Button(self.Tab3frm, text = "确认文件")#.grid(row = 1, column = 3)
        self.Tab3ButtonConfirm.pack(side=LEFT)
        self.Tab3frm.pack(side=TOP)

        self.Tab3frm2 = Frame(self.Tab3)
        self.Tab3ButtonMerge = Button(self.Tab3frm2, text = "确认合并")#.grid(row = 0, column = 0)
        self.Tab3ButtonMerge.pack()
        self.Tab3frm2.pack(side=TOP)
        self.TabStrip1.add(self.Tab3, text='File Linker')
 #third tab end
 #fourth tab
        self.Tab4 = Frame(self.TabStrip1)
        self.Tab4Lbl1 = Label(self.Tab4,text = "bin file:")#.grid(row = 1, column = 0)
        self.Tab4Lbl1.pack()
        self.Tab4pathEntry = Entry(self.Tab4)#.grid(row = 1, column = 1)
        self.Tab4pathEntry.pack()
        self.Tab4ButtonSelect = Button(self.Tab4, text = "Select")#.grid(row = 1, column = 2)
        self.Tab4ButtonSelect.pack()
        self.Tab4ButtonConfirm = Button(self.Tab4, text = "Read")#.grid(row = 1, column = 3)
        self.Tab4ButtonConfirm.pack(side=BOTTOM)
        self.TabStrip1.add(self.Tab4, text='Binary Reader')
 #fourth tab end
 #about tab
        self.TabX = Frame(self.TabStrip1)
        self.TabXLbl = Label(self.TabX, text="Listen's Swiss Army knife")
        self.TabXLbl.place(relx=0.1,rely=0.5)
        self.TabStrip1.add(self.TabX, text='About')
        
 #about tab end

if __name__ == "__main__":
    top = Tk()
    Application_ui(top).mainloop()