##READNE - yeeter##

This is a bash script that iterates through rpi01 - rpi18 and ping each
one to check if a host is up or down. There are two use cases:

To go through all hosts: $ rpistatus

To go through selected hosts: $rpistatus <host1> <host2> ...

The output is on screen and display the status of each host:

rpi01 is alive
rpi02 is dead
...

The script uses the ping command with -c 1 -W 1 options
