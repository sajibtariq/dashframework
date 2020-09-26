# A reproducible DASH Framework for 5G Networks


Framework provides real 5G emulated environment to run DASH videos. Framework installed with following packages

  - godash
  - Mininet-Wifi
  - Caddy - a WSGI web server hosting DASH video content
  - Scripts - Bash scripts to apply the 5G bandwidth values sampled from the 5G traces at run-time
  - Python scripts to process QoE & QoS logs
  
## Binder link
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sajibtariq/demo/master?filepath=Notebook%2FExecutable%20notebook.ipynb)

## Video Demonstration 
[Phase 1 - Streaming Framework](https://drive.google.com/file/d/1mGnDVoJqgwN5kXZfEPpSff7pPekEb6Y8/view?usp=sharing)

[Phase 2 - Dynamic Analysis](https://drive.google.com/file/d/1zIh8zVk3RMz1uKREnn3roOBPu9JNAmZk/view?usp=sharing)

## Features

  - Per-segment QoS to QoE mapping
  - 5G environment to run DASH videos with 10 different combinations of Bandwidth, The combinations are [here](https://github.com/sajibtariq/demo/tree/master/Testbed/5g_traces) 
  - Real 5G Traces collected from https://github.com/uccmisl/5Gdataset

## Dataset
Please note, in 5G_TC_Cases.csv there are 10 combinations for real 5G Cases across two scenarios: Mobility (driving) --- (38.26 to 10.33), (29.33 to 10.55), (0.5 to 3) and (6 to 14), and Static --- (72.42 to 9), (70 to 20), (52.06 to 0.5), (4.19 to 8), (0.5 to 6) and (8.29 to 57.15) Mbps. 

## dataset.csv description
The dataset file has 30 columns, these are 
intExpID,	type,	column,	case,	total_users,	user_no,	intSeg,	intArr,	intDel,	intSta,	intRep,	intDelRate,	intActRate,	intByteSize,	floatBuf,	algorithm_used,	seg_Dur,	width,	height,	resolutions,	play_Pos,	RTT,	Clae,	Duanmu,	Yin,	Yu,	P1203,	rtt_qos,	tp_qos,	p_qos

   - Here, intExpID is a unique experiment we performed, (type, column, case) type presents as experiment is ---Mobility or ---Static, (column and case) as the 5G case selection from 5G_TC_Cases.csv.
  - total_users, user_no as total user competing for video stream, and user_no as the logs for corresponding user.
  - intSeg as segment number, as in our case we streamed 60 segments of 2s each, intArr as Arrival Time, intDel as Delivery of the segment.
  - intSta as stall or freeze for that segment number, intRep as Representation selected for the segment, intDelRate as delivery rate of network
  - intActRate defined as actual rate in Kbps, intByteSize as byte size of this segment
  - floatBuf as buffer level in ms , algorithm_used such as (Conventional, Elastic, Arbiter +, BBA, Logistic, Exponential), seg_Dur as segment duration in ms
  - width, height as Representation width and height in pixels, resolutions as width x height such as 320x180
  - play_Pos as Current Play Back position, RTT as Packet level (ms), determined using HTTP head request
  - Clae, Dunamu, Yin, Yu and P.1203 five quality of experience models

Finally, per-segment RTT, throughput and packets for 60 segments are as rtt_qos, tp_qos and p_qos respectively

#### For more information of godash logs see below figure 

![](https://github.com/razaulmustafa852/dashframework/blob/master/images/godash_logsinfo.png)
