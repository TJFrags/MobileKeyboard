import socket
import Input


input = Input.Input()
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


# get local machine name
host = socket.gethostname()                           

port = 4444

try:

    # bind to the port
    serversocket.bind((host, port))                                  

    # queue up to 5 requests
    serversocket.listen(5)                                           

    while True:
        print("waiting for connection")
        clientsocket,addr = serversocket.accept()  
        print("connection received")
        print("Got a connection from %s" % str(addr))

        while True:
            clientsocket,addr = serversocket.accept()

            received_message = clientsocket.recv(1024).decode()
            print(received_message)
except Exception as E:
    clientsocket.close()
