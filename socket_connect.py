import socket

# 创建一个socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 主动去连接局域网内IP为192.168.2.143，端口为2000的进程
client.connect(('192.168.2.143', 2000))

while True:
    # '{"relay1":"on","relay2":"on","relay3":"on","relay4":"on","relay5":"on","relay6":"on","relay7":"on","relay8":"on"}' #设置设备状态
    # '{"get":"relayStatus"}' #查询当前状态
    # '{"name":"hello python"}' #修改设备名称
    # '{"get":"name"}' #获取设备名称
    # '{"ipaddr":"192.168.1.10","gateway":"192.168.1.1","netmask":"255.255.255.0","port":"2000"}' #设置网络信息
    #  '{"get":"netconfig"}' #获取网络配置信息
    # '{"get":"version"}' #获取网络版本
    # '{"485addr":"22"}' #设置485地址
    # '{"get":"485addr"}' #获取485地址
    # '{"baudrate":"9600"}' #设置波特率
    # '{"get":"baudrate"}' #获取波特率
    # '{"dhcp":"on"}' #设置DHCP状态
    # '{"get":"dhcp"}' #获取DHCP状态
    # '{"reboot":"1"}' #重启
    # '{"cmd":"test"}' #示例

    # 接受控制台的输入
    print("请输入一个命令:(输入quit则退出...)")
    data = input()
    # 对数据进行编码格式转换，不然报错
    data = data.encode('utf-8')
    # 如果输入quit则退出连接
    if data == b'quit':
        print(b'connect quit.')
        break
    else:
        # 发送数据
        client.sendall(data)
        # 接收服务端的反馈数据
        rec_data = client.recv(1024)
        print(b'form server receive:' + rec_data)
        # 将返回的字符串转换为字典用于返回值的条件判断
        dict_info = eval(rec_data[0:len(rec_data)-1])

        #可在此进行条件判断,例如:
        # if dict_info['resp'] == "ok":
        #     print("开灯成功！")
# 发送数据告诉服务器退出连接
client.sendall(b'quit')
client.close()
