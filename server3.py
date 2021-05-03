# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:39:11 2021

@author: johnn
"""

import socket
HOST = '192.168.0.152'
PORT = 3939

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Set TCP socket
server.bind((HOST, PORT)) #To bind the Host and Port
server.listen(10)         #Set the max value of client socket
# a = []
while True:

    conn, addr = server.accept()  # connect to the client
    clientMessage = str(conn.recv(1024), encoding='utf-8')  #Get the message from client

    print('Client message is:', clientMessage)
    # for i in clientMessage:
    #     a.append(i)
    String2List = clientMessage.split()  
    
    list_sort = sorted(int(e) for e in String2List)
    
    List2String = ' '.join(str(i) for i in list_sort)
    
    serverMessage = List2String
   
    conn.sendall(serverMessage.encode())   #Send the message to client
   
    
conn.close()