# Import required modules
import socket
import threading

HOST = 'localhost'
PORT = 6999
LISTENER_LIMIT = 5
active_clients = [] # List of all currently connected users
QUIT = 'quit'

"""
listen for upcoming messages from a client
"""
def listen_for_messages(client, username):

    while True:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)

        else:
            print(f"The message send from client {username} is empty")


"""
send message to a single client
"""
def send_message_to_client(client, message):

    client.sendall(message.encode())

"""
send message to all clients
"""
def send_messages_to_all(message):
    
    for user in active_clients:

        send_message_to_client(user[1], message)


"""handle client """
def client_handler(client):
    

    while True:

        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("Client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username, )).start()

"""
Main function
"""
def main():

    # create a socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind socket to a port
    try:
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    # Set server limit
    server.listen(LISTENER_LIMIT)

    # This while loop will keep listening to client connections
    while True:

        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

        threading.Thread(target=client_handler, args=(client, )).start()


if __name__ == '__main__':
    main()