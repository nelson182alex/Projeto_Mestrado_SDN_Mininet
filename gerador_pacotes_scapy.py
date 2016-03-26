from scapy.all import *

cont1 = 10
cont2 = 10
cont3 = 10

while cont1 > 0:
 packet1 = IP(dst="10.0.0.2")/ICMP()/"Helloooo!"
 packet2 = IP(dst="10.0.0.2")/TCP()/"Helloooo!"
 packet3 = IP(dst="10.0.0.2")/UDP()/"Helloooo!"
 send(packet1)
 send(packet2)
 send(packet3)
 packet1.show()
 packet2.show()
 packet3.show()
 cont1 = cont1 - 1


 while cont2 > 0:
  packet1 = IP(dst="10.0.0.2")/ICMP()/"Helloooo!"
  packet2 = IP(dst="10.0.0.2")/TCP()/"Helloooo!"
  packet3 = IP(dst="10.0.0.2")/UDP()/"Helloooo!"
  send(packet1)
  send(packet2)
  send(packet3)
  packet1.show()
  packet2.show()
  packet3.show()
  cont2 = cont2 - 1
