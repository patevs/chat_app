import sys
import socket
import select

def run_client():
    """
    Run the client. This should listen for input text from the user
    and send messages to the server. Responses from the server should
    be printed to the console.
    """
    # Specify where the server is to connect to
    server_address = '127.0.0.1'
    port = 5000
    
    # Create a socket and connect to the server
    client_socket = socket.socket()
    client_socket.connect((server_address, port))
    socket_list = [sys.stdin, client_socket]

    # Log that it has connected to the server
    print ('Connected to chat server.')
    print ('Type here to send messages:')

    # Start listening for input and messages from the server
    while True:        
        # Listen to the sockets (and command line input) until something happens
        ready_to_read, ready_to_write, in_error = select.select(socket_list , [], [], 0)
     
        # When one of the inputs are ready, process the message
        for sock in ready_to_read:            
            # The server has sent a message
            if sock == client_socket:
                pass
                # YOUR CODE HERE:
                # decode the data coming from the socket and print it out to the console
                msg = sock.recv(1024).decode()
                if(len(msg) > 0):
                	print("RECV: %s \n" % (str(msg)))               
            else:
                # The user entered a message
                msg = sys.stdin.readline()
                # Send the message to the server
                client_socket.send(msg.encode())
                print("SENT: %s \n" % (str(msg)))   

        
if __name__ == '__main__':
    run_client()