import time 

 def disparar_normal(threadName, src):
    time.sleep(1)
   	src.cmd('tcpreplay -i h1-eth0 -tK --loop 1 bigFlows.pcap')

def disparar_ataque(threadName, src):
    time.sleep(1)
    src.cmd('tcpreplay -i h1-eth0 -tK --loop 1 bigFlows.pcap')