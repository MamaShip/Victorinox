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
        self.master.geometry('880x400')
        self.createWidgets()
 
    def createWidgets(self):
        self.top = self.winfo_toplevel()
 
        self.style = Style()
 
        self.MyNotebook = Notebook(self.top)
        self.MyNotebook.place(relx=0.022, rely=0.062, relwidth=0.956, relheight=0.876)
 #first tab
        self.TabStrip1__Tab1 = Frame(self.MyNotebook)
        self.Tab1TotalFrm = Frame(self.TabStrip1__Tab1)
        # title : page <-> WL
        self.TabStrip1__Tab1Title = Label(self.Tab1TotalFrm,\
                                text='Page             <--->             WL  ',font='Times 12 normal')
        self.TabStrip1__Tab1Title.pack(side=TOP)

        self.TabStrip1__Tab1frm = Frame(self.Tab1TotalFrm)

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

        self.TabStrip1__Tab1Lbl = Label(self.Tab1TotalFrm)
        self.TabStrip1__Tab1Lbl.pack()#place(relx=0.45,rely=0.5)

        self.Tab1TotalFrm.place(relx=0.3,rely=0.3)
        self.MyNotebook.add(self.TabStrip1__Tab1, text=' Page_WL ')
 #first tab end
 #second tab
        self.Tab2 = Frame(self.MyNotebook)

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

        self.MyNotebook.add(self.Tab2, text='Option Checker')
 #second tab end
 #third tab
        self.Tab3 = Frame(self.MyNotebook)

        self.Tab3Lbl1 = Label(self.Tab3, text = "用选择按钮，依次选择需要link的文件。通过确认按钮将其加入下方list，最后按合并")#.grid(row = 0, column = 0)
        self.Tab3Lbl1.pack(side=TOP)

        self.Tab3frm = Frame(self.Tab3)
        
        self.Tab3Lbl2 = Label(self.Tab3frm,text = "目标路径:")#.grid(row = 1, column = 0)
        self.Tab3Lbl2.pack(side=LEFT)
        self.Tab3pathEntry = Entry(self.Tab3frm)#.grid(row = 1, column = 1)
        self.Tab3pathEntry.pack(side=LEFT)
        self.Tab3ButtonSelect = Button(self.Tab3frm, text = "选择文件")#.grid(row = 1, column = 2)
        self.Tab3ButtonSelect.pack(side=LEFT)
        self.Tab3ButtonConfirm = Button(self.Tab3frm, text = "确认")#.grid(row = 1, column = 3)
        self.Tab3ButtonConfirm.pack(side=LEFT)
        self.Tab3frm.pack(side=TOP)

        self.Tab3Text = Text(self.Tab3, height = 16)
        self.Tab3Text.pack()

        self.Tab3frm2 = Frame(self.Tab3)
        self.Tab3ButtonMerge = Button(self.Tab3frm2, text = "合并")#.grid(row = 0, column = 0)
        self.Tab3ButtonMerge.pack()
        self.Tab3frm2.pack(side=BOTTOM)
        self.MyNotebook.add(self.Tab3, text='File Linker')
 #third tab end
 #fourth tab
        self.Tab4 = Frame(self.MyNotebook)
        self.Tab4Lbl1 = Label(self.Tab4,text = "bin file:")#.grid(row = 1, column = 0)
        self.Tab4Lbl1.pack()
        self.Tab4pathEntry = Entry(self.Tab4)#.grid(row = 1, column = 1)
        self.Tab4pathEntry.pack()
        self.Tab4ButtonSelect = Button(self.Tab4, text = "Select")#.grid(row = 1, column = 2)
        self.Tab4ButtonSelect.pack()
        self.Tab4ButtonConfirm = Button(self.Tab4, text = "Read")#.grid(row = 1, column = 3)
        self.Tab4ButtonConfirm.pack(side=BOTTOM)
        self.MyNotebook.add(self.Tab4, text='Binary Reader')
 #fourth tab end
 #fifth tab
        self.Tab5 = Frame(self.MyNotebook)
        self.Tab5TotalFrm = Frame(self.Tab5)
        self.Tab5frm1 = Frame(self.Tab5TotalFrm)
        # PAA address part
        self.Tab5Lbl1 = Label(self.Tab5frm1,text = "PAA addr:")
        self.Tab5Lbl1.pack(side=LEFT)
        self.Tab5paa = Entry(self.Tab5frm1)
        self.Tab5paa.pack(side=LEFT)
        #Confirm Button
        self.Tab5Confirm_Button = Button(self.Tab5frm1, text = "确认")
        self.Tab5Confirm_Button.pack(side=LEFT)
        self.Tab5frm1.pack()
        # translate addr part
        self.Tab5frm2 = Frame(self.Tab5TotalFrm)
        self.Tab5SubFrameList = []
        self.Tab5LabelList = []
        self.Tab5LabelContent = ['BLK','page','LUN','CE','CH','plane','frag']
        self.Tab5AdrrEntryList = []
        # 7 sub frame : 'blk','page','LUN','CE','CH','plane','frag'
        for FrmCnt in range(7):  
            self.Tab5SubFrameList.append(Frame(self.Tab5frm2, padding = '2 2 4 4'))
            # label 
            self.Tab5LabelList.append(Label(self.Tab5SubFrameList[FrmCnt],text=self.Tab5LabelContent[FrmCnt], font = 'Times 9 normal'))
            self.Tab5LabelList[FrmCnt].pack()
            # entry
            self.Tab5AdrrEntryList.append( Entry(self.Tab5SubFrameList[FrmCnt], width = 4) )
            self.Tab5AdrrEntryList[FrmCnt].pack()

            self.Tab5SubFrameList[FrmCnt].pack(side=LEFT)
        self.Tab5frm2.pack()
        # row address part
        self.Tab5frm3 = Frame(self.Tab5TotalFrm)
        self.Tab5Lbl2 = Label(self.Tab5frm3,text = "row addr:")
        self.Tab5Lbl2.pack(side=LEFT)
        self.Tab5row = Entry(self.Tab5frm3)
        self.Tab5row.pack(side=LEFT)
        self.Tab5frm3.pack()

        self.Tab5TotalFrm.place(relx=0.32,rely=0.3)

        self.MyNotebook.add(self.Tab5, text='  PAA  ')
 #fifth tab end
 #sixth tab
        self.Tab6 = Frame(self.MyNotebook)
        self.Tab6frm = Frame(self.Tab6, padding = '2 10 2 2')

        # description
        self.Tab6Lbl1 = Label(self.Tab6frm,text = "输入log筛选规则：以*代替数据位，？代替忽略位，其余为必要位")
        self.Tab6Lbl1.pack(side=TOP)

        self.Tab6subfrm1 = Frame(self.Tab6frm)
        # insert item entry
        self.Tab6item = Entry(self.Tab6subfrm1, width = 60)
        self.Tab6item.pack(side=LEFT)
        # Insert Button
        self.Tab6Insert_Button = Button(self.Tab6subfrm1, text = "加入规则")
        self.Tab6Insert_Button.pack(side=LEFT)
        self.Tab6subfrm1.pack()

        self.Tab6subfrm2 = Frame(self.Tab6frm)
        # Listbox to show existing rules
        self.Tab6ListBox = Listbox(self.Tab6subfrm2, width = 60)#, selectmode = MULTIPLE)
        for i in ['rules here']:
            self.Tab6ListBox.insert(END,i)
        self.Tab6ListBox.pack(side = LEFT)

        self.Tab6ListButtonFrm = Frame(self.Tab6subfrm2)
        # Delete Button
        self.Tab6Delete_Button = Button(self.Tab6ListButtonFrm, text = "删除该项")
        self.Tab6Delete_Button.pack()
        # Clear Button
        self.Tab6Clear_Button = Button(self.Tab6ListButtonFrm, text = "清除全部")
        self.Tab6Clear_Button.pack()
        self.Tab6ListButtonFrm.pack(side=LEFT)

        self.Tab6subfrm2.pack()

        self.Tab6subfrm3 = Frame(self.Tab6frm, padding = '2 2 2 10')
        self.Tab6Lbl2 = Label(self.Tab6subfrm3,text = "待解析文件:")
        self.Tab6Lbl2.pack(side=LEFT)
        self.Tab6pathEntry = Entry(self.Tab6subfrm3)
        self.Tab6pathEntry.pack(side=LEFT)
        self.Tab6ButtonSelect = Button(self.Tab6subfrm3, text = "选择文件")
        self.Tab6ButtonSelect.pack(side=LEFT)

        self.Tab6subfrm3.pack()

        self.Tab6ButtonStart = Button(self.Tab6frm, text = "执行")
        self.Tab6ButtonStart.pack()

        self.Tab6frm.pack()

        self.MyNotebook.add(self.Tab6, text='Log Finder')
 #sixth tab end
 #about tab
        self.TabX = Frame(self.MyNotebook)
        self.TabXfrm = Frame(self.TabX)
        self.TabXLbl = Label(self.TabXfrm, text="Listen's Swiss Army knife")
        self.TabXLbl.pack()
        self.TabXLb2 = Label(self.TabXfrm, text="ver 1.5.0")
        self.TabXLb2.pack()
        self.TabXLb3 = Label(self.TabXfrm, text="Powered by Python Tkinter")
        self.TabXLb3.pack()
        self.TabXfrm.place(relx=0.4,rely=0.4)
        self.MyNotebook.add(self.TabX, text=' About ')
        
 #about tab end

if __name__ == "__main__":
    top = Tk()
    Application_ui(top).mainloop()