# Lifecycle
A Lifecycle Node is used to manage the internal state of a node in a controlled way.
Unlike a basic node, it allows more predictable startup, shutdown, and recovery behavior, which is especially important for robot control systems.

## STAGE

<img width="544" height="339" alt="image" src="https://github.com/user-attachments/assets/55ee6ce0-1859-47da-a783-c93b4c201e3f" />

| State            | Description                                      | Key Characteristics                                                                                             |
| ---------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **Unconfigured** | The node is created but not yet initialized.     | - No resources allocated<br>- Parameters can be declared<br>- Cannot process data                               |
| **Inactive**     | The node is configured but not actively running. | - Publishers/Subscribers exist but do not process data<br>- Safe to set parameters<br>- No callbacks executed   |
| **Active**       | The node is fully operational.                   | - Processing data (publish/subscribe)<br>- Timers and callbacks are running<br>- Main functionality is executed |
| **Finalized**    | The node is shutting down or destroyed.          | - Used for cleanup and debugging<br>- Resources are released                                                    |



Between these main states, there are transition states, such as:

Configuring
Activating
Deactivating
Cleaning up
Shutting down

# Command
- get state
```
ros2 lifecycle get /node_name
```
- set state
```
ros2 lifecycle set /node_name configure
ros2 lifecycle set /node_name activate
ros2 lifecycle set /node_name deactivate
ros2 lifecycle set /node_name cleanup
ros2 lifecycle set /node_name shutdown
```

# Result

<img width="1920" height="1080" alt="Screenshot from 2026-03-26 10-20-01" src="https://github.com/user-attachments/assets/96951b7a-55ce-4911-ba4a-3aa06a16f790" />


