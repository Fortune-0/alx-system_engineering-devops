Author: Fortune Peter
Email: fortunepeterspc07@gmail.com


Resources
Read or watch:

Linux PID
Linux process
Linux signal
Process management in linux
man or help:

ps
pgrep
pkill
kill
exit
trap



PID Definition


A PID (i.e., process identification number) is an identification number that is automatically assigned to each process when it is created on a Unix-like operating system.

A process is an executing (i.e., running) instance of a program. Each process is guaranteed a unique PID, which is always a non-negative integer.

The process init is the only process that will always have the same PID on any session and on any system, and that PID is 1. This is because init is always the first process on the system and is the ancestor of all other processes.

A very large PID does not necessarily mean that there are anywhere near that many processes on a system. This is because such numbers are often a result of the fact that PIDs are not immediately reused, in order to prevent possible errors.


PROCESS MANAGEMENT

Process management in Linux is the task of controlling and monitoring the processes that are running on a Linux system1. A process in Linux is a running instance of a program2. Any command that you execute starts a process2.

Processes in Linux can be of two types2:

Foreground Processes: Depend on the user for input, also referred to as interactive processes2.
Background Processes: Run independently of the user, referred to as non-interactive or automatic processes2.
A process in Linux can go through different states after it’s created and before it’s terminated2. These states are:

Running: The process is running or it’s ready to run2.
Sleeping: The process is waiting for a resource to be available2.
Interruptible sleep: The process will wake up to handle signals2.
Uninterruptible sleep: The process will not wake up to handle signals2.
Stopped: The process enters this state when it receives a stop signal2.
Zombie: The process is dead but the entry for the process is still present in the table2.
There are two commands available in Linux to track running processes2:

Top Command: Displays a list of processes that are running in real-time along with their memory and CPU usage2.
Ps Command: Displays the currently-running processes2.
You can manage Linux processes using commands like bg, fg, top, ps, kill PID, nice, renice, df, free, etc3. These tools help you to prioritize each process or put them in the background or foreground to manage system resources efficiently4.
