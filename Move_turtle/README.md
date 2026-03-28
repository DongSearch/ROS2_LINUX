# Move turtle with 3 positions
using Action, interfaces, we can automatically move turtle, and finally make them to one launch file, which allows to execute all node files in one terminal


[Screencast from 2026년 03월 28일 12시 20분 30초.webm](https://github.com/user-attachments/assets/19b1d095-fbf1-4f68-bc64-99b3fba63dc5)


# Trouble Shooting

- stuck in feedback -> Multithread
<img width="1426" height="536" alt="Screenshot from 2026-03-28 11-34-40" src="https://github.com/user-attachments/assets/b57513b8-445c-42b9-8458-8e5d0fe565ca" />
<img width="593" height="281" alt="Screenshot from 2026-03-28 11-36-01" src="https://github.com/user-attachments/assets/528edfa1-8adc-47ce-83af-44afd0e1bf7c" />

- after reaching the target, it just finish without getting next goal ->put send_goal() to result callback
<img width="509" height="73" alt="Screenshot from 2026-03-28 11-39-17" src="https://github.com/user-attachments/assets/10797aab-4609-4bdb-8184-b6db80bde2a0" />

- noramlize is essential to angle velocity(it should be range in -2pi to 2pi. otherwise, the velocity explodly increases
<img width="692" height="72" alt="Screenshot from 2026-03-28 12-08-21" src="https://github.com/user-attachments/assets/c16f3d9f-be05-466d-9a9c-ba0c52749920" />
<img width="492" height="478" alt="Screenshot from 2026-03-28 11-50-54" src="https://github.com/user-attachments/assets/9d8b2a9f-58bf-438b-8aa8-3cc677607b94" />


# Tip!!
when to make Launch file, TimeAction can help to control start excution time in script!!
