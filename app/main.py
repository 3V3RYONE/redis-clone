def main():

    import socket
    s = socket.create_server(("localhost", 6379), reuse_port=True)
    clientsocket, address = s.accept()
    
    while True:
        clientsocket.recv(4)
        clientsocket.send(bytes("+PONG\r\n","utf-8"))


if __name__ == "__main__":
    main()
