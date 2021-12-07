#!/usr/bin/python
import sys
from mininet.node import Controller
from mn_wifi.node import OVSKernelAP
from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, mesh
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference


def topology():
	"Create a network."
	net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference, controller=Controller)
	info("*** Creating nodes\n")
		
	ap1 = net.addAccessPoint('ap1', ssid='new-ssid', mode='g', wlans=2,
												 channel='1', position='500,500,0')
	c1 = net.addController('c1', controller=Controller)

	info("*** Configuring Propagation Model\n")
	net.setPropagationModel(model="logDistance", exp=4)

	info("*** Configuring wifi nodes\n")
	net.configureWifiNodes()

	info("*** Creating links\n")
	net.addLink(ap1, cls=mesh, ssid='meshNet', intf='ap1-wlan2', channel=5)

	info("*** Starting network\n")
	net.build()
	net.addNAT().configDefault()
	c1.start()
	ap1.start([c1])
	
	f = sys.argv[2] if len(sys.argv) > 1 else "0"
		
	info("*** Running Test\n")

	#info("*** Running CLI\n")
	#CLI(net)	

	info("*** Stopping network\n")
	net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
