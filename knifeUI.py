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
        self.master.geometry('880x380')
        self.createWidgets()
 
    def createWidgets(self):
        self.top = self.winfo_toplevel()
 
        self.style = Style()
 
        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0.022, rely=0.062, relwidth=0.956, relheight=0.876)
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

        self.Tab2SubFrameList = []
        self.Tab2LabelList = []
        self.Tab2SubSubFrameList = []
        self.Tab2ButtonList = []
        self.Tab2strvarlist = []
        self.Tab2lalalist = ["*"," "," "," ","*","*","*","*","*","*","└","┘","└","┘","*","└",
                    "┘","└","┘","*","*","*","*","└","┘","└","─","─","┘","└","─","┘"]
        # bits keyboard frm
        self.Tab2frm = Frame(self.Tab2)

        for FrmCnt in range(32/4):  # totalBitNum = 32

            self.Tab2SubFrameList.append(Frame(self.Tab2frm, padding = '2 2 4 4'))  

            for i in range(4):

                self.Tab2SubSubFrameList.append(Frame(self.Tab2SubFrameList[FrmCnt]))

                self.Tab2LabelList.append(Label(self.Tab2SubSubFrameList[4*FrmCnt + i],text=str(31-(4*FrmCnt + i)),font='Times 9 normal'))
                #LabelList[FrmCnt].config()
                self.Tab2LabelList[4*FrmCnt + i].pack(side=TOP)

                #Buttons and their string vars
                self.Tab2strvarlist.append(StringVar())
                self.Tab2strvarlist[4*FrmCnt + i].set('0')
                self.Tab2ButtonList.append(Button(self.Tab2SubSubFrameList[4*FrmCnt + i], textvariable=self.Tab2strvarlist[4*FrmCnt + i], width = 2))
                
                self.Tab2ButtonList[4*FrmCnt + i].pack()

                Label(self.Tab2SubSubFrameList[4*FrmCnt + i], text = self.Tab2lalalist[4*FrmCnt + i], font='Times 13 normal').pack(side=BOTTOM)

                self.Tab2SubSubFrameList[4*FrmCnt + i].pack(side=LEFT)

            self.Tab2SubFrameList[FrmCnt].pack(side=LEFT)

        self.Tab2frm.pack()

        self.Tab2frm2 = Frame(self.Tab2)
        self.Tab2frm2Sub1 = Frame(self.Tab2frm2)
        #16进制文字框
        self.Tab2e = Entry(self.Tab2frm2Sub1)
        self.Tab2e.pack(side=LEFT)
        #Confirm Button
        self.Tab2Confirm_Button = Button(self.Tab2frm2Sub1,text="确认")
        self.Tab2Confirm_Button.pack(side=LEFT)
        #Clear Button
        self.Tab2Clear_Button = Button(self.Tab2frm2Sub1,text="清零")
        self.Tab2Clear_Button.pack(side=RIGHT)
        self.Tab2frm2Sub1.pack(side=TOP)
        #Option image
        self.Tab2frm2Sub2 = Frame(self.Tab2frm2)
        self.pic = PhotoImage(file = 'option.gif')
        Label(self.Tab2frm2Sub2,image=self.pic,width=800).pack()
        self.Tab2frm2Sub2.pack(side=BOTTOM)

        self.Tab2frm2.pack()

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

        self.Tab3Text = Text(self.Tab3, height = 16)
        self.Tab3Text.pack()

        self.Tab3frm2 = Frame(self.Tab3)
        self.Tab3ButtonMerge = Button(self.Tab3frm2, text = "确认合并")#.grid(row = 0, column = 0)
        self.Tab3ButtonMerge.pack()
        self.Tab3frm2.pack(side=BOTTOM)
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
        self.TabXLbl.pack()#place(relx=0.4,rely=0.5)
        self.TabXLb2 = Label(self.TabX, text="ver 1.3.0")
        self.TabXLb2.pack()#place(relx=0.5,rely=0.6)
        self.TabStrip1.add(self.TabX, text='About')
        
 #about tab end

if __name__ == "__main__":
    top = Tk()
    Application_ui(top).mainloop()