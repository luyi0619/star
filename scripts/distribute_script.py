import sys
import os

ips = [line.strip() for line in open("ips.txt", "r")]
n = len(ips)

ins = [line.split("\t")[0] for line in ips]
outs = [line.split("\t")[1] for line in ips]

port = int(sys.argv[1]) 
script = sys.argv[2]

for i in range(n):
  os.system("python %s %d %d > run.sh" % (script, i, port))
  os.system("chmod u+x run.sh")
  os.system("scp run.sh ubuntu@%s:~/star/run.sh" % outs[i])
