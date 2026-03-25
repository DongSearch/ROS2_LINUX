# PyQt

PyQt is a GUI framework for Python based on an event-driven architecture.

## Terminology
Signal    
→ An event notification emitted when something happens    
Slot      
→ A function that is executed in response to a signal    
connect()   
→ A method used to connect a signal to a slot     


# RQt 
rqt is a GUI framework in ROS that provides various tools and interfaces in the form of plugins.   

| Type          | Package Name         | Description                                         |
| ------------- | -------------------- | --------------------------------------------------- |
| Core / Meta   | `rqt`                | Main entry point and meta-package including plugins |
| Core          | `rqt_gui`            | Core GUI framework                                  |
| Core          | `rqt_gui_py`         | Python-based GUI implementation                     |
| Visualization | `rqt_graph`          | Visualizes node-topic connections                   |
| Visualization | `rqt_plot`           | Plots topic data in real-time                       |
| Debugging     | `rqt_console`        | Displays ROS logs                                   |
| Debugging     | `rqt_logger_level`   | Change logger levels dynamically                    |
| Introspection | `rqt_topic`          | Inspect topics and publish messages                 |
| Introspection | `rqt_service_caller` | Call ROS services manually                          |
| Introspection | `rqt_action`         | Interact with action servers                        |
| Introspection | `rqt_msg`            | View message definitions                            |
| Utility       | `rqt_reconfigure`    | Dynamic parameter tuning                            |
| Utility       | `rqt_py_console`     | Embedded Python console                             |
| Utility       | `rqt_shell`          | Terminal inside rqt                                 |
| Utility       | `rqt_bag`            | Record and play rosbag files                        |

# How to make Plugin(ament_cmake)
| File                | Role                             |
| ------------------- | -------------------------------- |
| `plugin.xml`        | Declares the plugin to rqt       |
| `package.xml`       | Package metadata + plugin export |
| `CMakeLists.txt`    | calls files into `share/`    |
| `__init__.py`       | Marks Python package             |
| `example.py`        | Plugin entry point (main class)  |
| `example_widget.py` | UI logic                         |
| `example.ui`        | GUI layout (Qt Designer)         |
| `launch.py`         | Optional execution script        |


## Order
1. create package
2. plugin code(inherit Plugin)
3. UI FIle
4. plugin.xml(Plugin Registration)
5. package.xml(Export Plugin)
6. CMakeLists.txt(Install Step)
7. RUN


