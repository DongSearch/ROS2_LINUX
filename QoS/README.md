# QoS(Quality of Service)

QoS refers to a set of communication policies that control how data is delivered between nodes,
ensuring that each message meets its intended reliability, timing, and delivery requirements.

In ROS2, QoS is implemented on top of DDS, which can use different transport protocols

# Item
there are 22 policies, but the following 6 are the most commonly used

| QoS Policy      | Available Options             | Description                                                                                                    |
| --------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Reliability** | `Reliable`, `Best Effort`     | `Reliable`: ensures all messages are delivered (retransmission)<br>`Best Effort`: may drop messages but faster |
| **Durability**  | `Volatile`, `Transient Local` | `Volatile`: only delivers new messages<br>`Transient Local`: stores last messages for late subscribers         |
| **History**     | `Keep Last`, `Keep All`       | `Keep Last`: store only recent N messages<br>`Keep All`: store all messages (limited by resources)             |
| **Depth**       | Integer (e.g., 10, 100)       | Queue size when using `Keep Last`                                                                              |
| **Deadline**    | Duration (e.g., 100ms)        | Maximum expected time between messages; violation triggers event                                               |
| **Lifespan**    | Duration (e.g., 500ms)        | Message expires after this time and is discarded                                                               |
<img width="640" height="207" alt="image" src="https://github.com/user-attachments/assets/2a14a3af-0bef-416f-8ef5-77f7960d2d0c" />

# Dependencies between Policies
when to design QoS, Relation between different policies is quite important
(Transicent and Best-effort has colision)
