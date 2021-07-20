import os
import socket
PORT  = 6022                           #将要连接的目标机器的端口
IP    = "192.168.31.245"                #将要连接的目标机器的IPv4地址
DATA  = "Test"                         #将要发送的文本
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:  #创建套接字
    s.connect((IP,PORT))
    s.sendall(DATA)
    reply = s.recv(1024)
    print(reply)        
