import socket

# 创建 socket 对象
s = socket.socket()


# 链接服务器
s.connect(("localhost",6666))
print (s.recv(1024))
s.close()