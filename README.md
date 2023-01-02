# Memcached-Lite

## Objective: 

In this project, the objective is to design a key-value store which is implemented by creating a server those stores and retrieves data from multiple clients. The key-value store is mimicking the Memcached client protocol.

## Functionalities:

* **TCP- socket server:** Server listens to all incoming clients and stores the keys and values
* **Set:** Store a key and value by sending the data from the client to server
* **Get:** Retrieve key and value by sending the request from client to server
* **Concurrency:** Server must be concurrent and accept multiple client requests

## Design:

