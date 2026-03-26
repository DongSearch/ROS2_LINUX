# Security
ROS2 Security (SROS2) is used to ensure secure communication between nodes.
It provides:

Authentication (only trusted nodes can communicate)
Encryption (data is protected from eavesdropping)
Access Control (nodes can only access allowed topics/services)

## How does it work?
ROS 2 security is based on:

- DDS Security
- Uses certificates, keys, and permissions files

Each node is assigned an enclave, which defines its identity and permissions.

## how to use
generate folder to contain security key
```
ros2 security create_keystore keystore_path
```
generate key
```
ros2 security create_enclave keysotre_path enclave_name
```
configure environment
```
export ROS_SECURITY_KEYSTORE=~/sros2_demo/demo_keystore
export ROS_SECURITY_ENABLE=true
export ROS_SECURITY_STRATEGY=Enforce
```

| Variable                  | Description                    |
| ------------------------- | ------------------------------ |
| **ROS_SECURITY_KEYSTORE** | Path to the keystore directory |
| **ROS_SECURITY_ENABLE**   | Enables security (true/false)  |
| **ROS_SECURITY_STRATEGY** | Behavior when security fails   |


| Strategy       | Meaning                                         |
| -------------- | ----------------------------------------------- |
| **Enforce**    | Only secure communication is allowed (strict)   |
| **Permissive** | Allows both secure and non-secure communication |


# Result
* you can't check it with just topic list
<img width="648" height="503" alt="Screenshot from 2026-03-26 10-55-18" src="https://github.com/user-attachments/assets/4e2e3800-6485-4a87-bff2-3211ebb420e7" />
<img width="836" height="968" alt="Screenshot from 2026-03-26 10-39-14" src="https://github.com/user-attachments/assets/46187008-9891-4aa8-a54f-0340528044b8" />

