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
	sta01 = net.addStation('sta01', position='250,450,0')
	sta02 = net.addStation('sta02', position='300,450,0')
	sta03 = net.addStation('sta03', position='350,450,0')
	sta04 = net.addStation('sta04', position='400,450,0')
	sta05 = net.addStation('sta05', position='450,450,0')

	sta11 = net.addStation('sta11', position='250,400,0')
	sta12 = net.addStation('sta12', position='300,400,0')
	sta13 = net.addStation('sta13', position='350,400,0')
	sta14 = net.addStation('sta14', position='400,400,0')
	sta15 = net.addStation('sta15', position='450,400,0')

	sta21 = net.addStation('sta21', position='250,350,0')
	sta22 = net.addStation('sta22', position='300,350,0')
	sta23 = net.addStation('sta23', position='350,350,0')
	sta24 = net.addStation('sta24', position='400,350,0')
	sta25 = net.addStation('sta25', position='450,350,0')

	sta31 = net.addStation('sta31', position='250,300,0')
	sta32 = net.addStation('sta32', position='300,300,0')
	sta33 = net.addStation('sta33', position='350,300,0')
	sta34 = net.addStation('sta34', position='400,300,0')
	sta35 = net.addStation('sta35', position='450,300,0')

	sta41 = net.addStation('sta41', position='250,250,0')
	sta42 = net.addStation('sta42', position='300,250,0')
	sta43 = net.addStation('sta43', position='350,250,0')
	sta44 = net.addStation('sta44', position='400,250,0')
	sta45 = net.addStation('sta45', position='450,250,0')

	sta51 = net.addStation('sta51', position='250,200,0')
	sta52 = net.addStation('sta52', position='300,200,0')
	sta53 = net.addStation('sta53', position='350,200,0')
	sta54 = net.addStation('sta54', position='400,200,0')
	sta55 = net.addStation('sta55', position='450,200,0')

	ap1 = net.addAccessPoint('ap1', ssid='new-ssid', mode='g', wlans=2, channel='1', position='500,500,0')
	c1 = net.addController('c1', controller=Controller)

	info("*** Configuring Propagation Model\n")
	net.setPropagationModel(model="logDistance", exp=4)

	info("*** Configuring wifi nodes\n")
	net.configureWifiNodes()

	info("*** Creating links\n")
	net.addLink(sta01, cls=mesh, ssid='meshNet', intf='sta01-wlan0', channel=5)
	net.addLink(sta02, cls=mesh, ssid='meshNet', intf='sta02-wlan0', channel=5)
	net.addLink(sta03, cls=mesh, ssid='meshNet', intf='sta03-wlan0', channel=5)
	net.addLink(sta04, cls=mesh, ssid='meshNet', intf='sta04-wlan0', channel=5)
	net.addLink(sta05, cls=mesh, ssid='meshNet', intf='sta05-wlan0', channel=5)

	net.addLink(sta11, cls=mesh, ssid='meshNet', intf='sta11-wlan0', channel=5)
	net.addLink(sta12, cls=mesh, ssid='meshNet', intf='sta12-wlan0', channel=5)
	net.addLink(sta13, cls=mesh, ssid='meshNet', intf='sta13-wlan0', channel=5)
	net.addLink(sta14, cls=mesh, ssid='meshNet', intf='sta14-wlan0', channel=5)
	net.addLink(sta15, cls=mesh, ssid='meshNet', intf='sta15-wlan0', channel=5)

	net.addLink(sta21, cls=mesh, ssid='meshNet', intf='sta21-wlan0', channel=5)
	net.addLink(sta22, cls=mesh, ssid='meshNet', intf='sta22-wlan0', channel=5)
	net.addLink(sta23, cls=mesh, ssid='meshNet', intf='sta23-wlan0', channel=5)
	net.addLink(sta24, cls=mesh, ssid='meshNet', intf='sta24-wlan0', channel=5)
	net.addLink(sta25, cls=mesh, ssid='meshNet', intf='sta25-wlan0', channel=5)

	net.addLink(sta31, cls=mesh, ssid='meshNet', intf='sta31-wlan0', channel=5)
	net.addLink(sta32, cls=mesh, ssid='meshNet', intf='sta32-wlan0', channel=5)
	net.addLink(sta33, cls=mesh, ssid='meshNet', intf='sta33-wlan0', channel=5)
	net.addLink(sta34, cls=mesh, ssid='meshNet', intf='sta34-wlan0', channel=5)
	net.addLink(sta35, cls=mesh, ssid='meshNet', intf='sta35-wlan0', channel=5)

	net.addLink(sta41, cls=mesh, ssid='meshNet', intf='sta41-wlan0', channel=5)
	net.addLink(sta42, cls=mesh, ssid='meshNet', intf='sta42-wlan0', channel=5)
	net.addLink(sta43, cls=mesh, ssid='meshNet', intf='sta43-wlan0', channel=5)
	net.addLink(sta44, cls=mesh, ssid='meshNet', intf='sta44-wlan0', channel=5)
	net.addLink(sta45, cls=mesh, ssid='meshNet', intf='sta45-wlan0', channel=5)

	net.addLink(sta51, cls=mesh, ssid='meshNet', intf='sta51-wlan0', channel=5)
	net.addLink(sta52, cls=mesh, ssid='meshNet', intf='sta52-wlan0', channel=5)
	net.addLink(sta53, cls=mesh, ssid='meshNet', intf='sta53-wlan0', channel=5)
	net.addLink(sta54, cls=mesh, ssid='meshNet', intf='sta54-wlan0', channel=5)
	net.addLink(sta55, cls=mesh, ssid='meshNet', intf='sta55-wlan0', channel=5)
	net.addLink(ap1, cls=mesh, ssid='meshNet', intf='ap1-wlan2', channel=5)

	if len(sys.argv) > 1 :
		info("*** Introducing loss ", sys.argv[1], "%\n")
		sta01.cmd("tc qdisc add dev sta01-wlan0 root netem loss " + sys.argv[1] + "%")
		sta02.cmd("tc qdisc add dev sta02-wlan0 root netem loss " + sys.argv[1] + "%")
		sta03.cmd("tc qdisc add dev sta03-wlan0 root netem loss " + sys.argv[1] + "%")
		sta04.cmd("tc qdisc add dev sta04-wlan0 root netem loss " + sys.argv[1] + "%")
		sta05.cmd("tc qdisc add dev sta05-wlan0 root netem loss " + sys.argv[1] + "%")

		sta11.cmd("tc qdisc add dev sta11-wlan0 root netem loss " + sys.argv[1] + "%")
		sta12.cmd("tc qdisc add dev sta12-wlan0 root netem loss " + sys.argv[1] + "%")
		sta13.cmd("tc qdisc add dev sta13-wlan0 root netem loss " + sys.argv[1] + "%")
		sta14.cmd("tc qdisc add dev sta14-wlan0 root netem loss " + sys.argv[1] + "%")
		sta15.cmd("tc qdisc add dev sta15-wlan0 root netem loss " + sys.argv[1] + "%")

		sta21.cmd("tc qdisc add dev sta21-wlan0 root netem loss " + sys.argv[1] + "%")
		sta22.cmd("tc qdisc add dev sta22-wlan0 root netem loss " + sys.argv[1] + "%")
		sta23.cmd("tc qdisc add dev sta23-wlan0 root netem loss " + sys.argv[1] + "%")
		sta24.cmd("tc qdisc add dev sta24-wlan0 root netem loss " + sys.argv[1] + "%")
		sta25.cmd("tc qdisc add dev sta25-wlan0 root netem loss " + sys.argv[1] + "%")

		sta31.cmd("tc qdisc add dev sta31-wlan0 root netem loss " + sys.argv[1] + "%")
		sta32.cmd("tc qdisc add dev sta32-wlan0 root netem loss " + sys.argv[1] + "%")
		sta33.cmd("tc qdisc add dev sta33-wlan0 root netem loss " + sys.argv[1] + "%")
		sta34.cmd("tc qdisc add dev sta34-wlan0 root netem loss " + sys.argv[1] + "%")
		sta35.cmd("tc qdisc add dev sta35-wlan0 root netem loss " + sys.argv[1] + "%")

		sta41.cmd("tc qdisc add dev sta41-wlan0 root netem loss " + sys.argv[1] + "%")
		sta42.cmd("tc qdisc add dev sta42-wlan0 root netem loss " + sys.argv[1] + "%")
		sta43.cmd("tc qdisc add dev sta43-wlan0 root netem loss " + sys.argv[1] + "%")
		sta44.cmd("tc qdisc add dev sta44-wlan0 root netem loss " + sys.argv[1] + "%")
		sta45.cmd("tc qdisc add dev sta45-wlan0 root netem loss " + sys.argv[1] + "%")

		sta51.cmd("tc qdisc add dev sta51-wlan0 root netem loss " + sys.argv[1] + "%")
		sta52.cmd("tc qdisc add dev sta52-wlan0 root netem loss " + sys.argv[1] + "%")
		sta53.cmd("tc qdisc add dev sta53-wlan0 root netem loss " + sys.argv[1] + "%")
		sta54.cmd("tc qdisc add dev sta54-wlan0 root netem loss " + sys.argv[1] + "%")
		sta55.cmd("tc qdisc add dev sta55-wlan0 root netem loss " + sys.argv[1] + "%")
	info("*** Starting network\n")
	net.build()
	net.addNAT().configDefault()
	c1.start()
	ap1.start([c1])

	f = sys.argv[1] if len(sys.argv) > 1 else "0"

	info("*** Running Test\n")
	sta51.cmd("ping -c600 -s1232 198.51.100.100 | tee log/M_W_6_"+f+"L_60.log")

	#info("*** Running CLI\n")
	#CLI(net)

	info("*** Stopping network\n")
	net.stop()


if __name__ == '__main__':
	setLogLevel('info')
	topology()
