# ROS
ROS is a robot middleware (meta operating system) that provides communication between processes, package management, and tools specialized for robot software development.
- Middleware : enables communication between processes
- Modularization : robot software can be divided into reusable modules
- Extensibility : easy to add and integrate new packages

## Consitituion
- Node : the smallest processing unit in ROS; each node performs a specific function.
- Package : the basic organizational unit containing nodes, messages, topics, and other resources.
- Message : a standardized data format used for communication between nodes.

  
## Difference between ROS1 and ROS2
- ROS1 : designed mainly for a single robot, Linux-only, limited real-time support, weaker security.
- ROS2 : uses DDS middleware, supports multi-robot systems, real-time capability, and improved security.
<img width="960" height="691" alt="image" src="https://github.com/user-attachments/assets/57dcb4e0-ee41-47ef-a76f-28fea81a1aca" />

## Main characteristics of ROS2

- Multiple workspaces : supports multiple development environments.
- No devel space / isolated build : cleaner and more stable build system.
- Client libraries : supports multiple programming languages.
- Component-based nodes : multiple nodes can run within a single process.
- Run / Launch system : flexible node execution and management.
- UDP communication : enables faster data transfer.
- DDS (Data Distribution Service) : data-centric communication middleware
 <img width="599" height="411" alt="image" src="https://github.com/user-attachments/assets/69b7682b-0982-41c0-a331-36fbd94a59b7" />

## Communication
- Topic (msg) : asynchronous one-way communication between publisher and subscriber.
- Service (srv) : synchronous request-response communication between client and server.
- Action (action) : bidirectional communication for long tasks with feedback and cancellation support.
- Parameter : allows external clients to read or modify node parameters.
<img width="1536" height="780" alt="image" src="https://github.com/user-attachments/assets/c410b3be-9775-49ce-966a-cce7df64746b" />
