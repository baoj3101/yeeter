#!/bin/bash

#===========================================
# ping one host given the host name
# rpistatus $host ==> $1
#===========================================
function rpistatus {
  ping -c 1 -W 1 $1 > /dev/null # with -c 1 and ignore all output
  if [ $? -eq 0 ]; then         # exit code 0 means alive
    echo "$1 is alive<br>"
  else                          # exit code non-0 means down
    echo "$1 is dead<br>"
  fi
}

echo "Content-type: text/html"
echo ""
echo "<html><head></head><body>"

#===========================================
# if no command line arguments, go through
# rpi01-rpi18
# ./rpistatus
#===========================================
if [ $# -eq 0 ]; then          
    for i in 0{1..9} {10..18}; do
        host=rpi$i
        rpistatus $host
    done
#===========================================
# if command line arguments, go through
# user provided list of hosts
# ./rpistats rpi05 rpi16
#===========================================
else                        
    for host in ${BASH_ARGV[*]} ; do
        rpistatus $host
    done
fi

echo "</body></html>"

