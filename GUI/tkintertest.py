#!/usr/bin/env python
from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        # ipadx=设置宽度，ipady设置高度，视图内所有控件均可使用这两个属性
        # padx=110, pady=110主窗口设置则是距离屏幕的距离
        self.grid(ipadx=250, ipady=140)
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = Button(self, text='Quit', command=self.quit)
        # padx,pady设置这个控件距离边的位置，设定值只能为正数
        # row=3, column=2, rowspan=4, columnspan=5设置没有看到效果
        self.quitButton.grid(ipadx=12, ipady=4, padx=2, pady=2)
app = Application()
app.master.title('test')
app.mainloop()
