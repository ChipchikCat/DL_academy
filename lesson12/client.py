import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 1111))

flag = True
while flag:
    client.send(input("Я: ").encode("utf-8"))
    message = client.recv(1024).decode("utf-8")
    if message == "quit":
        flag = False
    else:
        print(message)

client.close()
