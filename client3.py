# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:39:00 2021

@author: johnn
"""

import socket

HOST = '192.168.0.152'
PORT = 3939
count = 0
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Set TCP socket
client.connect((HOST, PORT)) #Connect to the server port

list1 = []
how_many = int(input("請問你想排序多少個數字?"))
count = 1


while count <= how_many :
    print("input",count,"num")
    list1.append(input())
    count += 1

List2String = ' '.join(list1)

clientMessage = List2String
client.sendall(clientMessage.encode()) #Send message to server


serverMessage = str(client.recv(1024), encoding='utf-8')
String2List = serverMessage.split()

print(str(count),'Server:', String2List)

client.close()

