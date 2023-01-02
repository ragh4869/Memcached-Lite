# Packages
import socket

# Defing parse function to parse text file into a list of commands
def parse(filename):

    with open(filename) as f:
        lines = f.readlines()
    
    command_list = []
    i=0
    
    while i < len(lines):
        lines[i] = lines[i].replace('\n','')
        
        if lines[i].split()[0].lower() == 'set':
            if i == len(lines)-1:
                break
            lines[i+1] = lines[i+1].replace('\n','')
            if lines[i+1].split()[0].lower in ('set','get'):
                i += 1
                continue
            command_list.append(' '.join(lines[i:i+2]))
            i += 1
        else:
            command_list.append(lines[i])
        
        i += 1
    
    return command_list

# Defining client function
def client_program():
    
    host = socket.gethostname() # Get hostname
    port = 8080  # Initiate port value greater than 1024
    
    filename = 'client_input_2.txt' # Name of file
    command_list = parse(filename) # Get the command list from the text file

    while len(command_list)!= 0:
        
        # Get client instance for IPv4 address and TCP connection
        client_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_instance.connect((host, port))  # Connect to the server
        except socket.error as se:
            print(str(se)) # Printing socket error 

        comm = command_list.pop(0)  # Take command from text file
        client_instance.sendall(comm.encode())  # Send command to server

        response_data = client_instance.recv(1024).decode()  # Receive response from server
        print(response_data)  # Server Response

        client_instance.close()  # Close the connection 

 
if __name__ == '__main__':
    client_program()