import os
import sys
import subprocess

#host=[2,3] # total number of host
host = [2]

#algorithm =['arbiter','exponential','bba','logistic','conventional','elastic'] ## adaptive algorithm
algorithm =['conventional']

#trace=[1,2,4,5,6,7,8,9,10,11] #5f_traces[dynamic: trace number-1,2,8,10 and static: trace number- 4,5,6,7,9,11]

trace =[10]

count = 1

for curr in range(count):
    for h in host:
        for a in algorithm:
            for c in trace:
                clear = 'sudo mn -c'
                run_top_script = 'sudo python topo.py '+ str(h)+ ' ' + str(a)+ ' ' + str(c)       
                subprocess.run(clear.split(' '))
                print(run_top_script)
                subprocess.run(run_top_script.split(' '))
