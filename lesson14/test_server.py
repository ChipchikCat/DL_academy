import socket


def test__Chat_server(cls):
    cls = "test"
    assert test__Chat_server(cls) == "Test_server"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 1111))

    server.listen()
    client, address = server.accept()

    flag = True

    while flag:
        message = client.recv(1024).decode("utf-8")
        if message == "quit":
            flag = False
        else:
            print(message)
        client.send(input("Server: ").encode("utf-8"))

    client.close()
    server.close()