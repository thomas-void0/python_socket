from tkinter import *
top = Tk()
top.title("New England")
top.geometry('600x300')
# 创建一个label标签
lableBox = Label(top, text="协议示例数据列表",font=16)
lableBox.grid(row=0,column=0,rowspan=1,padx=(100,0))
yscroll = Scrollbar(top, orient=VERTICAL)
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
    '"get":"dhcp"}',
    '重启：',
    '{"reboot":"1"}',
    '示例：',
    '{"cmd":"test"}'
]
conOFlstNE = StringVar()
lstNE = Listbox(top,width=60,height=8,listvariable=conOFlstNE,yscrollcommand=yscroll.set)
lstNE.grid(row=1,column=0,rowspan=4,padx=(100,0),pady=5)
conOFlstNE.set(tuple(statesList))
yscroll["command"] = lstNE.yview
top.mainloop()