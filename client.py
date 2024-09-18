import socket

HOST = 'localhost'
PORT = 5999
QUIT = 'quit'


def main(): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    done = False
    while not done:
        client_msg = input("Message: ")
        
        # If the client types "quit", exit the loop
        if client_msg == QUIT:
            done = True
            client.send(QUIT.encode('utf-8'))  # Send "quit" to the server
            print("Exiting chat...")
            break  # Exit the loop after sending quit message
        
        client.send(client_msg.encode('utf-8'))
        
        # Receive the server's message
        server_msg = client.recv(1024).decode('utf-8')
        # If the server sends "quit", exit the loop
        if server_msg == QUIT:
            done = True
            print("Server closed the connection. Exiting chat...")
        else:
            print(server_msg)

    print("Connection closed")
    client.close()

if __name__ == '__main__':
    main()