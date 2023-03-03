import socket
import time

def client_program():

    host = socket.gethostname() # as both code is running on same pc
    port = 4040 #initiae port


    client_socket = socket.socket() #instancetiate

    client_socket.connect((host,port)) # connect to the server

    #take input
    message = input(" --> ")

    while message.lower().strip() != 'bye':

        try:
            #strip method removes spaces at the beginning and end of a string

            #In a TCP/IP socket connection, if you want to send a string,
            #you must first convert the string to a byte string.
            #This can be done using the encode method
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode() # receive response

            print(f'Received from server: {data} ') #show in terminal

            message = input(" --> ") #again take input

        except KeyboardInterrupt:
            break

    #close the connection
    client_socket.close()


if __name__ == "__main__":
    client_program()