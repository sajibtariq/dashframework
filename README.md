# DASH QoE Performance Evaluation Framework with 5G Datasets


Framework provides real 5G emulated environment to run DASH videos. Framework installed with following packages

  - [goDASH](https://github.com/uccmisl/godash)- a  headless DASH video player
  - [Mininet-Wifi](https://github.com/intrig-unicamp/mininet-wifi)- network emulator 
  - [Caddy](https://caddyserver.com/)- a WSGI web server hosting DASH video content
  - [Tcpdump](https://www.tcpdump.org/manpages/tcpdump.1.html)- a network packet sniffer
  - Bash scripts to apply the 5G bandwidth values sampled from the 5G traces at run-time
  - Python scripts to process QoE & QoS logs
  
## Binder link
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sajibtariq/demo/master?filepath=Notebook%2FExecutable%20notebook.ipynb)

## Video Demonstration 
[Streaming Framework and Dynamic Analysis](https://drive.google.com/file/d/1mGnDVoJqgwN5kXZfEPpSff7pPekEb6Y8/view?usp=sharing)

[Interactive notebook with the Binder service](https://drive.google.com/file/d/1zIh8zVk3RMz1uKREnn3roOBPu9JNAmZk/view?usp=sharing)

## Recorded Paper Presentation
[Presentation](https://youtu.be/2j5qp9ehUEY)

## Streaming Framework VM

* **Requirement**: [Oracle  VirtualBox 6.1.10](https://www.virtualbox.org/wiki/Downloads)
*  **Download link**: [VM](https://drive.google.com/drive/folders/1y4HZ7sYxzCi__yXTpAnZwMQlQy5na04b?usp=sharing) [25 GB Size]: Ubuntu 18.04 x64 - **pass: dash**

* **Data Acquisition**

Step  1: Open ubuntu terminal and execute the following command:

```bash
 $ conda activate myenv
 $ jupyter lab
 
```
Step  2: JupyterLab interface and open terminal:
```bash
 $ cd ~/Demo/testbed
 $ sudo python3 parameters.py
```

* **Data Preprocess and Analysis** 

Step 1: Open the **Executable.ipynb** jupyter notebook from **~/Demo/Notebook** directory.


Step 2: To export csv from raw data (godash and pcap), run the following cell in notebook:


```bash

%run /home/dash/Demo/Notebook/pre-processing.ipynb
```

Step 3: To analysis from exported csv, run the following cell in notebook:

```bash

%run /home/dash/Demo/Notebook/Interactive_Control.ipynb
```



## 5G traces dataset
Please note, in 5G traces there are 10 combinations for real 5G Cases across two scenarios: Mobility-driving (trace no-1, 2, 8, 10) --- (38.26 to 10.33), (29.33 to 10.55), (0.5 to 3) and (6 to 14), and Mobility-static (trace no-4, 5, 6, 7, 9 ,11) --- (72.42 to 9), (70 to 20), (52.06 to 0.5), (4.19 to 8), (0.5 to 6) and (8.29 to 57.15) Mbps. 

  - 5G environment to run DASH videos with 10 different combinations of Bandwidth, The combinations are [here](https://github.com/sajibtariq/demo/tree/master/Testbed/5g_traces) 
  - Real 5G Traces collected from https://github.com/uccmisl/5Gdataset

## Processesd dataset description
The dataset file has 28 columns, these are 
'Mode', 'Trace_no', 'Total_host', 'Host_no', 'Segment_no', 'Arr_time', 'Del_Time', 'Stall_Dur', 'Rep_Level', 'Del_Rate', 'Act_Rate', 'Byte_Size', 'Buff_Level', 'Algorithm', 'Seg_Dur', 'Width', 'Height', 'resolutions', 'Play_Pos', 'RTT_app', 'Clae', ' Duanmu', 'Yin', 'Yu', 'P1203', 'persegment_RTT', 'Throughput', 'Packets'

  - 'Mode' as mobility driving or static, 'Trace_no' as corresponding trace number
  - 'Total_host'  as total host competing for video stream, and 'Host_no' as the logs for corresponding host.
  - 'Segment_no' as segment number, as in our case we streamed 60 segments of 2s each,  'Arr_time' as Arrival Time,  'Del_Time' as Delivery of the segment.
  - 'Stall_Dur' as stall or freeze for that segment number, 'Rep_Level' as Representation selected for the segment, Del_Rate' as delivery rate of network
  - 'Act_Rate' defined as actual rate in Kbps,  'Byte_Size' as byte size of this segment
  - 'Buff_Level' as buffer level in ms , 'Algorithm' such as (Conventional, Elastic, Arbiter +, BBA, Logistic, Exponential),'Seg_Dur' as segment duration in ms
  - 'Width', and 'Height', as Representation width and height in pixels,'resolutions' as width x height such as 320x180
  - 'Play_Pos' as Current Play Back position, RTT as Packet level (ms), determined using HTTP head request
  - 'Clae', ' Duanmu', 'Yin', 'Yu', and 'P1203' five quality of experience models

Finally, 'persegment_RTT', 'Throughput', and 'Packets' as network level per segment uplink RTT, downlink throughput and downlink number of packets. 


#### For more information of godash logs see below figure 

![](https://github.com/sajibtariq/dashframework/blob/master/Testbed/gpdash-log-notations.png)
