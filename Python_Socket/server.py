import socket

host, port = "", 5000
address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(address)
server_socket.listen()

print(f"Serving on localhost:{port}")

while True :
    
    client_socket, client_address = server_socket.accept()
    
    message = ''

    while True :
        chunk = client_socket.recv(1024)
        
        packet = chunk.decode('utf-8')
        print(packet)
        if (packet == "$") : break
        
        message += packet
        
    print(message)
    
    index_html = """\
HTTP/1.1 200 OK

Hello world! using Python socket 
"""
    
    client_socket.sendall(index_html.encode())
    
    client_socket.close()
