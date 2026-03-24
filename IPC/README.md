# Intra Process Communication
ROS2 supports intra-process communication to optimize communication between nodes in the same process.
Instead of going through DDS, messages are directly passed, reducing serialization and memory copies.

*
Zero-copy communication allows publisher and subscriber to share the same memory buffer without copying data,
minimizing latency and memory usage.



