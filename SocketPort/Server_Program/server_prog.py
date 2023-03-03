import socket


def server_program():

    # get the hostname
    #Return a string containing the hostname of the machine where the Python interpreter is currently executing.
    host = socket.gethostname()
    port = 4040 #initiae port

    #socket.AF_INET => IP address socket
    #socket.SOCK_STREAM => Type the TCP communication
    server_socket = socket.socket()

    #look closely. The bind() function takes tuple as argument => Bind the socket to address
    server_socket.bind((host,port)) # bind host address and port together

    #configure how many client the server can listen simultaneously
    server_socket.listen(2)

    conn,address = server_socket.accept() #accept a connection

    print("Connection from: " + str(address))

    while 1==1:

        try:
            #receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()

            if not data:
                #if data is not received break
                break
            print(f"from connected user: {str(data)}")
            data = input(" --> ")
            conn.send(data.encode()) #send data to the client

        except KeyboardInterrupt:
            break

    # close the connection
    conn.close()


if __name__ == "__main__":
    server_program()
