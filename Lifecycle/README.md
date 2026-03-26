# Lifecycle
Lifecycle is used to manage node status, which allow to handle them more delicately and control movement of robot more sophisticately compared basic node

## STAGE

<img width="544" height="339" alt="image" src="https://github.com/user-attachments/assets/55ee6ce0-1859-47da-a783-c93b4c201e3f" />

it has 4 main status
- unconfigured : that is state that node is just created, it can be adjusted
- inactivate : it is a state that still not activated, but here you can register parameter, publish or subscript, you can do all of job before activation
- activate : that is a state ongoing status
- finalized : checking the debugging or internal diagnosis before destroying the node


