# Socket COmmunication
- A socket is a programming interface used for network communication via an IP address and a port number.
- Each process can have multiple sockets.
* A port number is used to identify which application (process) the data should be delivered to.

## Structure
<img width="580" height="630" alt="image" src="https://github.com/user-attachments/assets/1f39edd5-bdc7-4f6a-ad69-c82cef16acec" />


The process is quite simple:
A client creates a socket and connects to the server using the server's IP address and port number.
If the server is listening on that port and the request matches, the connection is established.
After that, they can communicate with each other.

The server works similarly, but it must first call accept() to accept incoming client connections after listening on a port.

## Type
There are two main types of socket communication protocols:

### TCP (Transmission Control Protocol)

- Used when reliable and accurate communication is required
- Ensures data is delivered in order
- Checks for errors and retransmits lost data
- Slower but more reliable

### UDP (User Datagram Protocol)

- Does not guarantee delivery
- No error checking or retransmission
- Faster but less reliable


## Result
<img width="1450" height="290" alt="image" src="https://github.com/user-attachments/assets/c10f348e-7037-402f-b39f-1e33ab1f3824" />
