import sys
from mininet.log import setLogLevel, info
from mininet.node import Controller, RemoteController
from mininet.link import TCLink
from collections import OrderedDict
from mn_wifi.net import Mininet_wifi
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from multiprocessing import Process
import json
import os
import time

station = []


def topology():


    print('-----------------------')
    host= int(sys.argv[1])
    print("Total Host: "+ str(host))
    print('-----------------------\n')
    
   
    print('-----------------------')
    algo= sys.argv[2]
    print("Adaptive algorithm: "+ str(algo))
    print('-----------------------\n')

    print('-----------------------')
    Band_trace =int(sys.argv[3])
    print("5G trace number: "+ str(Band_trace))
    print('-----------------------\n')
    
    "Create a network."
   
    net = Mininet_wifi( controller=Controller, link=TCLink )
    
    info("*** Creating nodes\n")
    
    for i in range(host):
        m='host%s' % (i+1)
        j=i+1
        station.insert(i, net.addHost(m, ip='192.168.0.%s/24'%(j)))

    s1= net.addSwitch('s1')
    s2= net.addSwitch('s2')
    server = net.addHost('server', ip='192.168.0.150/24' )
    c0 = net.addController('c0')
   
    info("*** Adding Link\n")
    for i in range(host):
        net.addLink(s1, station[i])
  
    net.addLink(s1, s2, 100, 1)
    net.addLink(server, s2, 1 ,100)

    info("*** Starting network\n")
    net.build()
    c0.start()
    s1.start([c0])
    s2.start([c0])
    #info("*** Running CLI\n")

    time.sleep(05)
    os.system('sudo chmod 777 -R /home/dash/Demo/testbed/goDash/DashApp/src/files')
    os.system('sudo rm -r /home/dash/Demo/testbed/goDash/DashApp/src/files/3*')
    subfolder = 'total_host_' + str(host) + '_algo_'+str(algo)+ '_5g_trace_'+str(Band_trace) 
    os.system('mkdir -p /home/dash/Demo/Data/Raw/' + subfolder)

    os.system('cd /home/dash/Demo/testbed/goDash/DashApp/src/config/con && sudo rm -R *')
    with open('/home/dash/Demo/testbed/goDash/DashApp/src/config/configure.json') as json_file:
        test_dict = json.load(json_file, object_pairs_hook=OrderedDict)
    test_dict['adapt']=algo
    #print(test_dict)
    #ordered_dict = OrderedDict(test_dict)
    json.dump(test_dict, open('/home/dash/Demo/testbed/goDash/DashApp/src/config/con/configure.json',"w"))


    
    client=[]
    for i in range(host):
        m1='host%s' % (i+1)
        m2=net.get(m1)
        client.insert(i, m2)
    switch=net.get('s1')
    server=net.get('server')
    
    return client, switch, server, host , algo, Band_trace

## pcap capturing by tcpdump
def cap_pcap(host , algo, Band_trace ):

    print os.system('sudo tcpdump -i s1-eth100 -U -w /home/dash/Demo/Data/Raw/total_host_' + str(host) + '_algo_'+str(algo)+ '_5g_trace_'+str(Band_trace)+'/total_host_' + str(host) + '_algo_'+str(algo)+ '_5g_trace_'+str(Band_trace)+'.pcap') 
   

## godash client streaming
def godash_client(num , host, algo, Band_trace ):
  
    print num.cmd('cd /home/dash/Demo/testbed/goDash/DashApp/src/goDASH/ && ./goDASH --config ../config/con/configure.json >/home/dash/Demo/Data/Raw/total_host_' + str(host) + '_algo_'+str(algo)+ '_5g_trace_'+str(Band_trace)+'/' + str(num) + '_algo_'+str(algo)+ '_5g_trace_'+str(Band_trace)+'.txt && echo stop streaming_' + str(num) )
   

## caddy server on
def server(sr):
    print sr.cmd('cd /var/www && ./caddy')


## emulate 5g traces

def  tc(col_no):
     os.system('sudo ./bwc.sh %d'%(col_no))


#Stop caddy and tcpdump process--short-term soln (todo)

## caddy server off
def server_stop(host):	
    t=150*host
    time.sleep(t)
    os.system('sudo pkill -9 caddy && echo caddy server off.....' )\

## stop pcap capturing
def tcpdump_stop(host):
    t=150*host
    time.sleep(t)
    os.system(' sudo chmod 777 -R /home/dash/Demo/Data/Raw && sudo pkill -9 tcpdump  && echo stop pcap capturing.....' )



if __name__ == '__main__':
    setLogLevel( 'info' )

    station, switch, ser , host , algo , Band_trace_col_no =topology()
 
    a=True; b=False; c=False; d=False; e=False; f=False; g=False; h=False; i=False;
    
    if a:   
       print("Caddy server on")
       y = Process(target=server, args=(ser,))  ## caddy server on
       y.start()
       b=True

    if b:
       print("Pcap capturing...")
       n = Process(target=cap_pcap, args=(host,algo,Band_trace_col_no))   
       n.start()       
       c=True

    if c:
       print("5g traces....(bandwidth changes 4 second intervals)")
       z= Process(target=tc, args=(Band_trace_col_no,))   
       z.start() 
       d=True
    
    if d:
       print("godash client start streaming")
       for k in range(host):
           print station[k]
           q = Process(target=godash_client, args=(station[k], host, algo, Band_trace_col_no,))  
           q.start()
           q.join
           #e= True

    if e:
       t = Process(target=server_stop, args=(host,))   
       t.start()
       f=True
    
    if f:
       x = Process(target=tcpdump_stop, args=(host,))   
       x.start()
