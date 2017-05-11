#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from tkinter import *
# import os
# top = Tk()
# # 进入消息循环
# top.mainloop()


# from tkinter import *
# import tkinter.messagebox as messagebox


# class Application(Frame):

#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()

#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)

# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()
#
from tkinter import *           # 导入 Tkinter 库


def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())
root = Tk()                     # 创建窗口对象的背景色
# 创建两个列表
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = Listbox(root)  # 创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0, item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0, item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()
