mkdir info
cd info
systeminfo  > systeminfo.txt
netstat -a  > netstat.txt
ipconfig    > ipconfig.txt
tasklist /V > tasklist_completo.txt
netstat -an |find /i "listening" > open_ports.txt
tracert www.google.com > tracert.txt