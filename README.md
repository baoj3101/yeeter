##READNE - rpistatus##

This is a bash script that iterates through rpi01 - rpi18 and ping each
one to check if a host is up or down. There are two use cases:

To go through all hosts: $ rpistatus

To go through selected hosts: $ rpistatus <host1> <host2> ...

The output is on screen and display the status of each host:

rpi01 is alive
rpi02 is dead
...

The script uses the ping command with -c 1 -W 1 options

-W 1: timeout after 1 second if no response

## CGI ##

To enable calling rpistatus from webpage, CGI is needed.

Steps:

 $ cp rpistatus rpi.cgi
 $ nano rpi.cgi
  
 Edit rpi.cgi to make sure output is in html format

 $ cd /usr/lib/cgi-bin
 $ sudo cp ~/scripts/rpi.cgi .
 (Check with teach if sudo copy into cgi-bin is OK)

 From inside browser

 http://rpi06/cgi-bin/rpi.cgi
 
 Pi alive status message should show up.
