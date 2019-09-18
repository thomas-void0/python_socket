
from tkinter import *
import tkinter.messagebox
top = Tk()
top.title('socket...')
top.geometry('300x150')
lableBox = Label(top, text="输入数据:")
lableBox.pack()
textBox = Entry(top, bd =2)
textBox.pack()
def helloCallBack():
    tkinter.messagebox.showinfo("Hello Python",textBox.get())

def connectSocket():
    print("xxxxxxxx")
def closeSocket():
    pass
btnConnect = Button(top, text="发起连接", command=connectSocket)
btnConnect.pack()
btnSend = Button(top, text="发送数据", command=helloCallBack)
btnSend.pack()
btnClose = Button(top, text="关闭连接", command=closeSocket)
btnClose.pack()
top.mainloop()