mkdir info
cd info
systeminfo  > systeminfo.txt
netstat -a  > netstat.txt
ipconfig    > ipconfig.txt
tasklist /V > tasklist_completo.txt
netstat -an |find /i "listening" > open_ports.txt
net user    > usuarios.txt
gpresult /r > gpo_usuarios.txt
query user  > usuarios_conectados.txt
tracert www.google.com > tracert.txt