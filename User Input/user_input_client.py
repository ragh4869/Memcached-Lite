# Packages
import socket

# Defining client function
def client_program():
    
    host = socket.gethostname() # Get hostname
    port = 8080  # Initiate port value greater than 1024 

    # Get client instance for IPv4 address and TCP connection
    client_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_instance.connect((host, port))  # Connect to the server
    except socket.error as se:
        print(str(se)) # Printing socket error

    comm = 'Yes'
    while len(comm)!= 0:
        response_data = client_instance.recv(1024).decode()  # Receive response from server
        print(response_data)  # Server Response

        comm = input("Command: ")  # Take user input
        client_instance.sendall(comm.encode())  # Send command to server

    client_instance.close()  # Close the connection  

 
if __name__ == '__main__':
    client_program() 