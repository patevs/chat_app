import socket
import select


def run_server():
    """
    Start a server to facilitate the chat between clients.
    The server uses a single socket to accept incoming connections
    which are then added to a list (socket_list) and are listened to
    to recieve incoming messages. Messages are then stored in a database
    and are transmitted back out to the clients.
    """

    # Define where the server is running. 127.0.0.1 is the loopback address,
    # meaning it is running on the local machine.
    host = "127.0.0.1"
    port = 5000
  
    # Create a socket for the server to listen for connecting clients
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(10)

    # Create a list to manage all of the sockets
    socket_list = []
    # Add the server socket to this list
    socket_list.append(server_socket)


    # Start listening for input from both the server socket and the clients
    while True:

        # Monitor all of the sockets in socket_list until something happens
        ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [], 0)

        # When something happens, check each of the ready_to_read sockets
        for sock in ready_to_read:
            # A new connection request recieved
            if sock == server_socket:
                # Accept the new socket request
                sockfd, addr = server_socket.accept()
                # Add the socket to the list of sockets to monitor
                socket_list.append(sockfd)
                # Log what has happened on the server
                print ("Client (%s, %s) connected" % (addr[0],addr[1]))

            # A message from a client has been recieved
            else:
                pass
                # YOUR CODE HERE
                # Extract the data from the socket and iterate over the socket_list
                # to send the data to each of the connected clients.
                data = sock.recv(1024).decode()

                msg = ("%s" % (str(data)))
                for res_soc in socket_list:
                	if(res_soc != socket_list[0]):
                		res_soc.send(msg.encode())
                



     
if __name__ == '__main__':
    run_server()