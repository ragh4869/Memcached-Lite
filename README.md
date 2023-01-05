<h1 align="center">
Memcached-Lite
</h1>

## Objective: 

In this project, the objective is to design a key-value store which is implemented by creating a server those stores and retrieves data from multiple clients. The key-value store is mimicking the Memcached client protocol.

## Functionalities: 

* **TCP- socket server:** Server listens to all incoming clients and stores the keys and values
* **Set:** Store a key and value by sending the data from the client to server
* **Get:** Retrieve key and value by sending the request from client to server
* **Concurrency:** Server must be concurrent and accept multiple client requests

## How to run? :

* Open a command prompt window and run the user_input_server.py
* Open an another command prompt window and run the user_input_client.py

## Design: 

![Design](https://user-images.githubusercontent.com/96961381/210283611-703993f6-8101-4ae7-af6c-ee579b1ca193.jpeg)

The above image illustrates the design of the implemented client-server architecture. 

Python scripts are implemented to host the server and multiple clients. Two scripts are created which is the server script and client script. Let us understand the design of each of the scripts.

### Server:

In the server script, three functions are defined which are:

* server_program: The main function to host the server
* set_data: To store the key and value data sent from the client
*	get_data: To retrieve the key and value data requested by the client

#### server_program:

In the server_program function, the host is initialized using socket.gethostname() and the port is initialized with a port number greater than 1024 (port used here is 8080).

A server instance is then initiated for IPv4 address and TCP connection. This server instance is then bound to the host and port after which the server is listening to any open connections.

A while loop is set after the above process so that it accepts multiple clients and also so that it does not close after just 1 connection. It then starts accepting clients and receives the data from the accepted client. The data is decoded and split into a list of maximum of 4 strings. This is done for the below:
*	Set instruction: set key bit_value value
*	Get instruction: get key

The first string is read and if it is ‘set’ the set_data function is called. Similarly, if the first string is ‘get’, the get function is called. Else, it sends a wrong command error .

#### set_data:

In the set_data function, the data.json file (file holding the stored key and value data) is read and retrieved as a dictionary. The command is then processed and the key, value are added to the dictionary  accordingly. The dictionary is then updated in the data.json file.

#### get_data:

In the get_data function, the data.json file (file holding the stored key and value data) is read and retrieved as a dictionary. The requested key is retrieved and the key, bit_value and value is then sent back to the client.

### Client:

In the client script, three functions are defined which are:
*	client_program: The main function to host the client
*	parse: To parse the text file into a list of commands

#### client_program:

In the client_program function, the host is initialized using socket.gethostname() and the port is initialized with a port number greater than 1024 (port used here is 8080).

A while loop is started until all commands are sent and processed to the server, and a client instance is then initiated for IPv4 address and TCP connection. This client instance is then bound to the host and port after which the connects to any server listening to any clients trying to connect.

The command then gets sent one by one and receives the appropriate response.

### Test Cases & Exceptional Handling:

![client_input_1 - Test Case](https://user-images.githubusercontent.com/96961381/210282578-59ae0dd0-4985-42ad-9f0e-e92040abc753.JPG)
![client_input_2 - Test Case](https://user-images.githubusercontent.com/96961381/210282579-3eb46e4c-978d-4c5d-a916-c0331ac9f59a.JPG)

In the above two images, the test cases for the files **client_input_1.txt** and **client_input_2.txt** run respectively by the scripts **client.py** and **client_2.py**.

Let us decode and understand the test cases along with their output. The formats observed with their output is shown below:

#### Set:

Output - STORED

* set Hotel 5 Wyatt
* set Destination 7 Chicago
* set Name 6 Raghav
* Set Course 27 Engineering Cloud Computing
* set Food 6 Apples

In the above examples, it can be observed that all the inputs are correctly sent from the client, hence, the output returned is STORED.

#### Get:

Output format – 

VALUE  key  bit_value

value

END
 
* get Hotel
* get Name
* Get Course
* get Food

In the above examples, it can be observed that all the inputs are correctly sent from the client, hence, the output returned is the output format shown above.

#### Interesting Cases:

**get Location:** Here the Location is not present in the data stored, hence, the output returned is – 

Key value not available

END 

**set Name Raghav**

**get Name yes**

In the above two examples, it can be observed that the command inputs are not in the right format, hence, the output returned is – Invalid command inputs. Try Again!

**not get File:** The first string word is neither get nor set, hence, the output returned is –

Wrong Command. Try Again!

**set Country Yes USA:** In the bit value, it is a string Yes instead of an integer value, hence, the output returned is – 

Bit value is not an integer. Try Again!

**set Country 2 USA:** The bit value specified is the wrong number of bits for the Value, hence, the output returned is – 

Bit value not specified correctly. Try Again!

### Experimental Evaluation:

The server is tested for performance and number of concurrent clients.

#### Performance:

The performance of the server is tested by running the input text file 1000 and 10000 times for Thread and Process. By looking into the Evaluation Testing file, it can be clealy seen that the time taken for the Thread tasks to run is much lesser than the Process tasks. 

**Thread:**
* Tasks – 1000; Time Taken: 124.437 seconds
* Tasks – 10000; Time Taken: 1080.286 seconds

**Process:**
* Tasks – 1000; Time Taken: 659.892 seconds
* Tasks – 10000; Time Taken: Took a lot of time(> 1hr to run)

#### Number of Concurrent Clients:

The ThreadPoolExecutor was run multiple max_workers – 100, 200, 500. Although this might not be a good test to run as max_workers is the maximum number of threads which can be used, thus, the function could use lesser threads to run too.

Taking the assumption that the max threads was used, the server can handle around 100 clients concurrently as the server is crashing above this value.

### Future Scope:

*	The performance of the server can be significantly improved.
*	Since the server can handle just around 200 clients concurrently, the concurrency can be improved.

### Appendix: User Input

In addition to the text input where the input is got through the text, I have also done a client-server interface to take the user input. 

Multiple clients can be connected to the servers and any values stored through one client can be accessed with another client as shown below:

![UseCase](https://user-images.githubusercontent.com/96961381/210282602-0ed2da00-c5d8-4f3a-a682-93b9c52e462d.JPG)

The user inputs the key and value as described in the text input.
