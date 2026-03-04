import socket

def server_chat():
    host ="0.0.0.0" 
    port = 12345

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen(1)

    con,address = server_socket.accept()
    print(f"Connection from: {address}")

    while True :
        client_message = con.recv(1024).decode()
        if client_message.lower() =='bye':
            print("terminate chat by the client")
            break
        print(f"Message from client : {client_message}")

        server_message = input("say something")
        con.send(server_message.encode())
        if server_message.lower() == "bye":
            print("Connection closed by the server")
            break

    
    con.close()
    server_socket.close()

if __name__ == '__main__':
    server_chat()
