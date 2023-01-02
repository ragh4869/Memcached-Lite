# Packages
import socket
import json
import time
from multiprocessing import Process
from threading import Thread

# Defining Get function
def get_data(client_data, conn):
    
    with open('data.json') as f: # Open json file to read 
        data = json.load(f) # Convert json object to a dictionary

    # Checking for required number of inputs
    if len(client_data) != 2:
        conn.sendall('Invalid command inputs. Try Again!\r\nEND'.encode())
        return
    
    # Get Key value
    key_val = client_data[1]

    # Sending the key, value and bit count in required format
    if key_val in data.keys():
        bit_val = data[key_val]['Bits']
        data_val = data[key_val]['Data']
        output_val = f'VALUE {key_val} {bit_val} \r\n{data_val}\r\nEND\r\n'
        conn.sendall(output_val.encode())
    else:
        conn.sendall('Key value not available\r\nEND'.encode())


# Defining Set function
def set_data(client_data, conn):
    
    with open('data.json') as f: # Open json file to read
        data = json.load(f) # Convert json object to a dictionary
    
    # Checking for required number of inputs
    if len(client_data) != 4:
        conn.sendall('NOT-STORED\r\nInvalid command inputs. Try Again!\r\n'.encode())
        return
    
    # Get Key value
    key_val = client_data[1]

    # Checking if key is already present condition
    # if key_val in data.keys():
    #     print('Key already present')
    #     while True:
    #         task_val = input('Do you want to replace the key value? (Y/N): ')

    #         if task_val == 'Y':
    #             break
    #         elif task_val == 'N':
    #             conn.sendall('Enter a different key\r\n'.encode())
    #             return
    #         else:
    #             print('Invalid input. Try Again!')
    #         continue
    
    # Checking for correct bit value input
    try:
        bit_value = int(client_data[2])
    except:
        conn.sendall('NOT-STORED\r\nBit value is not an integer. Try Again!\r\n'.encode())
        return

    if bit_value == len(client_data[3]):
        pass
    else:
        conn.sendall('NOT-STORED\r\nBit value not specified correctly. Try Again!\r\n'.encode())
        return
    
    # Checking if the data is getting STORED or NOT-STORED
    try:
        data[key_val] = {'Bits':bit_value, 'Data':client_data[3]}
        
        with open('data.json', 'w') as f: # Open json file to write
            json.dump(data, f, indent=2) # Update the data in the json file
        
        conn.sendall('STORED\r\n'.encode())
    except:
        conn.sendall('NOT-STORED\r\n'.encode())


# Defining server program
def server_program():

    host = socket.gethostname() # Get hostname
    port = 8080  # Initiate port value greater than 1024

    # Get server instance for IPv4 address and TCP connection
    server_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    try:
        server_instance.bind((host, port))  # Binding host address and port to the server socket
    except socket.error as se:
        print(str(se)) # Printing socket error

    server_instance.listen() # Instance of server listening to clients 

    # act = True
    while True:
        conn, address = server_instance.accept()  # Accepting a new connection
        print("Connection from: " + str(address))

        client_data = conn.recv(1024) # Receive data from client
        resp = client_data.decode() # Decode the client data

        print(f'Command: {resp}') 

        # Check for empty data
        if not client_data:
            break

        cl_data = resp.split(maxsplit=3) 

        # Run the commands using Process 
        # if cl_data[0].lower() == 'set':
        #     # Start Set function process
        #     client_process = Process(target=set_data, args=(cl_data,conn,))
        #     client_process.start()
        # elif cl_data[0].lower() == 'get':
        #     # Start Get function process
        #     client_process = Process(target=get_data, args=(cl_data,conn,))
        #     client_process.start()
        # else:
        #     conn.sendall('Wrong Command. Try Again!\r\n'.encode())


        # Run the commands using Thread
        if cl_data[0].lower() == 'set':
            # Start Set function process
            client_thread = Thread(target=set_data, args=(cl_data,conn,))
            client_thread.start()
        elif cl_data[0].lower() == 'get':
            # Start Get function process
            client_thread = Thread(target=get_data, args=(cl_data,conn,))
            client_thread.start()
        else:
            conn.sendall('Wrong Command. Try Again!\r\n'.encode())


    conn.close()

if __name__ == '__main__':
    server_program()
