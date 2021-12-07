#!/usr/bin/python

'This example shows how to create multiple interfaces in stations'

import sys
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.link import wmediumd, adhoc
from mn_wifi.wmediumdConnector import interference


def topology():
	"Create a network."
	net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)

	info("*** Creating nodes\n")
	ap1 = net.addAccessPoint('ap1', ssid='ssid_1', mode='g', channel='5', failMode="standalone", position='500,500,0')

	info("*** Configuring Propagation Model\n")
	net.setPropagationModel(model="logDistance", exp=4)

	info("*** Configuring wifi nodes\n")
	net.configureWifiNodes()

	info("*** Associating...\n")
	net.addLink(ap1, sta05)

	info("*** Starting network\n")
	net.build()
	net.addNAT().configDefault()
	ap1.start([])

	info("*** Addressing...\n")
	
	f = sys.argv[2] if len(sys.argv) > 1 else "0"

	info("*** Running Test\n")

	info("*** Stopping network\n")
	net.stop()


if __name__ == '__main__':
	setLogLevel('info')
	topology()
