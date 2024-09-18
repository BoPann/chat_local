import socket 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5999))
server.listen(1)  # Listening for 1 connection

client, addr = server.accept()

done = False
while not done:
    # Receive the client's message
    msg = client.recv(1024).decode('utf-8')
    
    if msg == 'quit':
        print("Client left")
        done = True  # Exit the loop after client sends 'quit'
    else:
        print(msg)
        
    # If the client didn't quit, allow the server to send a message
    if not done:
        server_message = input("Message: ")
        
        if server_message == 'quit':
            done = True  # Exit the loop after server sends 'quit'
        client.send(server_message.encode('utf-8'))
        
print("Connection closed")
client.close()  # Close the connection after the loop
server.close()  # Close the server
