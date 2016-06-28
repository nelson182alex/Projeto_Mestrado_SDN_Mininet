from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
import thread
import custom


        net = Mininet(link=TCLink)
    	c = RemoteController('c', '192.168.169.1', 6653)
    	# Change the args of GenericTree() to your desired values. You could even get them from command line.
   		net.addController(c)
    	# hosts
		h0 = net.addHost('h0')
		h1 = net.addHost('h1')
		h2 = net.addHost('h2')
		h3 = net.addHost('h3')
		h4 = net.addHost('h4')
		h5 = net.addHost('h5')
 
		# switches
		s0 = net.addSwitch('s0')
		s1 = net.addSwitch('s1')
		s2 = net.addSwitch('s2')
		s3 = net.addSwitch('s3')
		s4 = net.addSwitch('s4')
		s5 = net.addSwitch('s5')
 
		# add links
		net.addLink(h0, s0, bw=10, delay='5ms', loss=0)
 
		net.addLink(s0, s1, bw=10, delay='5ms', loss=0)
		net.addLink(s0, s2, bw=10, delay='5ms', loss=0)
		net.addLink(s0, s3, bw=10, delay='5ms', loss=0)
		net.addLink(s0, s4, bw=10, delay='5ms', loss=0)
		net.addLink(s0, s5, bw=10, delay='5ms', loss=0)
 
		net.addLink(h1, s1, bw=10, delay='5ms', loss=0)
		net.addLink(h2, s2, bw=10, delay='5ms', loss=0)
		net.addLink(h3, s3, bw=10, delay='5ms', loss=0)
		net.addLink(h4, s4, bw=10, delay='5ms', loss=0)
		net.addLink(h5, s5, bw=10, delay='5ms', loss=0)
    	net.start()

    	thread.start_new_thread(custom.disparar_normal, ("thread 1", h1))
    	thread.start_new_thread(custom.disparar_ataque, ("thread 2", h2))

    	# installStaticFlows( net )
    	CLI(net)
    	net.stop()

