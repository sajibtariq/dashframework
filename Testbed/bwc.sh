#!/bin/bash
num=$1
a=1
v=1
while [ $a -lt 2 ]; do
    array=()
    i=1
    cut -d, -f 1 --output-delimiter=' ' /home/dash/Demo/testbed/5g_traces/$num.csv | while read col1  ; do
    
    array[$i]=$col1
    if [ $v -eq 1 ]; then

         sudo  tc qdisc add dev s2-eth1 handle 1:0 root htb default 1 && tc class add dev  s2-eth1 parent 1:0 classid 1:1 htb rate "${array[i]}"kbit ceil "${array[i]}"kbit && echo  "second" $SECONDS  "band" "${array[i]}"kbit 
         sleep 4
         v=0
    else
         sudo tc qdisc del dev  s2-eth1 root &&  sudo tc qdisc add dev  s2-eth1 handle 1:0 root htb default 1 && tc class add dev  s2-eth1 parent 1:0 classid 1:1 htb rate "${array[i]}"kbit ceil "${array[i]}"kbit &&  echo  "second" $SECONDS  "band" "${array[i]}"kbit

        sleep 4

    i=$((i + 1))
    fi

    #if [ $SECONDS -ge 300 ]; then
         #break
    #fi
    n=$(ps -ef| grep  goDASH| wc -l)

    if [ $n -eq 1 ]; then
            sleep 1
            sudo chmod 777 -R /home/dash/Demo/Data/Raw
            echo "caddy server of....."
            echo "stop pcap capturing....."
            sudo pkill -9 tcpdum
            sudo pkill -9 caddy
            a=$((a + 1))
            break
    fi
done
    
    if [$a -eq "2"]; then
          break
    else
          n=$(ps -ef| grep  goDASH| wc -l)

          if [ $n -eq 1 ]; then
                   sleep 1

                   sudo chmod 777 -R /home/dash/Demo/Data/Raw
                   #echo "caddy server of....."
                   #echo "stop pcap capturing....."
                   sudo pkill -9 tcpdum
                   sudo pkill -9 caddy
                   a=$((a + 1))
                   break
          fi
    fi

   
done
