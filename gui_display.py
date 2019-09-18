import socket
from tkinter import *
import tkinter.messagebox

# 创建一个socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#发起socket连接
def connectSocket():
    # 主动去连接局域网内IP为192.168.2.143，端口为2000的进程
    client.connect(('192.168.2.143', 2000))
    # 显示是否连接成功
    tkinter.messagebox.showinfo("connect flag...", "connect success!")

# 关闭socket连接
def closeSocket():
    client.sendall(b'quit')
    client.close()
    # 显示是否关闭成功
    tkinter.messagebox.showinfo("close flag...", "close success!")
# 发送数据
def sendData():
    data = textBox.get()
    # 对数据进行编码格式转换，不然报错
    data = data.encode('utf-8')
    # 发送数据
    client.sendall(data)
    # 接收服务端的反馈数据
    rec_data = client.recv(1024)
    # 显示返回的数据
    tkinter.messagebox.showinfo("back data...", rec_data)

#创建gui
top = Tk()
top.title('socket...')
top.geometry('600x300')
#创建示例列表
lableBox = Label(top, text="协议示例数据列表",font=16)
lableBox.grid(row=0,column=0,rowspan=1,padx=(100,0))
yscroll = Scrollbar(top, orient=VERTICAL,bg='#0099FF')
yscroll.grid(row=1,column=2,rowspan=4,padx=(0,100),pady=5,sticky=NS)
statesList = [
    '设置设备状态：',
    '{"relay1":"on","relay2":"on","relay3":"on","relay4":"on","relay5":"on","relay6":"on","relay7":"on","relay8":"on"}' ,
    '查询当前状态：',
    '{"get":"relayStatus"}',
    '修改设备名称：',
    '{"name":"hello python"}',
    '获取设备名称：',
    '{"get":"name"}',
    '设置网络信息：',
    '{"ipaddr":"192.168.1.10","gateway":"192.168.1.1","netmask":"255.255.255.0","port":"2000"}',
    '获取网络配置信息：',
    '{"get":"netconfig"}',
    '获取网络版本：',
    '{"get":"version"}',
    '设置485地址：',
    '{"485addr":"22"}'
    '获取485地址：',
    '{"get":"485addr"}',
    '设置波特率：',
    '{"baudrate":"9600"}',
    '获取波特率：',
    '{"get":"baudrate"}',
    '设置DHCP状态：',
    '{"dhcp":"on"}',
    '获取DHCP状态：',
    '{"get":"dhcp"}',
    '重启：',
    '{"reboot":"1"}',
    '示例：',
    '{"cmd":"test"}'
]
conOFlstNE = StringVar()
lstNE = Listbox(top,width=60,height=8,listvariable=conOFlstNE,yscrollcommand=yscroll.set,bg='#FFFFFF')
lstNE.grid(row=1,column=0,rowspan=4,padx=(100,0),pady=5)
conOFlstNE.set(tuple(statesList))
yscroll["command"] = lstNE.yview

# 创建一个label标签
lableBox = Label(top, text="输入数据:")
lableBox.grid(row=7,column=0,rowspan=1,padx=(100,0),pady=5,sticky=W)
# 创建一个输入框标签
textBox = Entry(top, bd =2,width=49,bg='#FFFFFF')
textBox.grid(row=7,column=0,rowspan=1,padx=(170,0),pady=5,sticky=W)
# 创建连接按钮
btnConnect = Button(top, text="发起连接", command=connectSocket,width=18,bg="#0099FF",fg="#FFFFFF",bd=0)
btnConnect.grid(row=8,column=0,rowspan=1,padx=(100,0),pady=5,sticky=W)
# 创建发送数据按钮
btnSend = Button(top, text="发送数据", command=sendData,width=18,bg="#0099FF",fg="#FFFFFF",bd=0)
btnSend.grid(row=8,column=0,rowspan=1,padx=(240,0),pady=5,sticky=W)
#创建关闭连接按钮
btnClose = Button(top, text="关闭连接",command=closeSocket,width=18,bg="#0099FF",fg="#FFFFFF",bd=0)
btnClose.grid(row=8,column=0,rowspan=1,padx=(380,0),pady=5,sticky=W)

top.mainloop()