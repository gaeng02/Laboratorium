import socket 

host, port = "localhost", 5000
address = (host, port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

while True :
    try :
        message = input("send: ")
        if (message == "Q") : break

        client_socket.send(message.encode())
    except ConnectionAbortedError : print("Socket Connection Error")


client_socket.close()
