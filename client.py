import socket
import threading

HOST = 'localhost'
PORT = 6999
QUIT = 'quit'

def listen_message_from_server(client):

    while True:
        msg = client.recv(2048).decode('utf-8')
        if msg != '':
            username, msg = msg.split('~')
            print(f"[{username}] {msg}")

def send_message_to_server(client):
    while True:
        msg = input("Message: ")
        if msg != '':
            client.sendall(msg.encode())
        

def communicate_to_server(client):

    username = input("Input your username: ")
    if username != '':
        # send the message to server with username
        client.sendall(username.encode())
    else:
        print("Username can't be empty!")
        exit(0)

    threading.Thread(target=listen_message_from_server, args=(client, )).start()
    send_message_to_server(client)

def main(): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # assign port to socekt
    try:
        client.connect((HOST, PORT))
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    communicate_to_server(client)
        
    """
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
    """
    print("Connection closed")
    client.close()

if __name__ == '__main__':
    main()