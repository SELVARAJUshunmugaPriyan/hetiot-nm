#!/usr/bin/python
import os, sys

def func(n):
	with open("adhocOrg", 'r') as fp:
		with open("adhocNew", 'w') as fpNew:
			for line in fp.readlines():
				if '*** Creating nodes' in line :
					fpNew.write(line)
					for j in range (0, int(n/10)):
						for i in range(1, 6):
							s = str(j) + str(i)
							t = str(450 - ( j * 50 ))
							u = str(450 - ((5 - i) * 50 ))
							if i == 5 and j == 0 :
								fpNew.write("\tsta" + s + " = net.addStation(\'sta" + s + "\', position=\'" + u + "," + t + ",0\', wlans=2)\n")
							else :
								fpNew.write("\tsta" + s + " = net.addStation(\'sta" + s + "\', position=\'" + u + "," + t + ",0\')\n")
				elif '*** Associating...' in line :
					fpNew.write(line)
					for j in range (0, int(n/10)):
						for i in range(1, 6):
							s = str(j) + str(i)
							if s == '05' :
								fpNew.write("\tnet.addLink(sta" + s + ", cls=adhoc, ssid=\'adhocNet\', intf=\'sta" + s + "-wlan1\')\n")
							else :
								fpNew.write("\tnet.addLink(sta" + s + ", cls=adhoc, ssid=\'adhocNet\', intf=\'sta" + s + "-wlan0\')\n")
				elif '*** Addressing...' in line :
					fpNew.write(line)
					for j in range (0, int(n/10)):
						for i in range(1, 6):
							s = str(j) + str(i)
							if s == '05' :
								fpNew.write("\tsta" + s + ".setIP(\'192.168.10." + s + "\', intf=\'sta" + s + "-wlan1\')\n")
							else :
								fpNew.write("\tsta" + s + ".setIP(\'192.168.10." + s + "\', intf=\'sta" + s + "-wlan0\')\n")	
					fpNew.write("\n\n")


					"""
					for i in range(5, 1, -1):
						fpNew.write("\tsta0" + str(i) + ".cmd(\"ip r a 192.168.10." + str(n - 9) +" via 192.168.10." + str(i - 1) + "\")\n")
						fpNew.write("\tsta0" + str(i) + ".cmd(\"echo 1 > /proc/sys/net/ipv4/ip_forward\")\n")
						if i != 5 :
							fpNew.write("\tsta0" + str(i) + ".cmd(\"ip r a 198.51.100.100 via 192.168.10." + str(i + 1) + "\")\n")

					fpNew.write("\tsta01.cmd(\"ip r a 198.51.100.100 via 192.168.10.2\")\n")
					fpNew.write("\tsta01.cmd(\"echo 1 > /proc/sys/net/ipv4/ip_forward\")\n")

					if n > 10 :
						fpNew.write("\tsta01.cmd(\"ip r a 192.168.10." + str(n - 9) +" via 192.168.10.11\")\n")
						fpNew.write("\n\n")
						for i in range(int(n) - 10, 20, -10):
							fpNew.write("\tsta" + str(i - 19) + ".cmd(\"ip r a 192.168.10." + str(n - 9) +" via 192.168.10." + str(i - 9) + "\")\n")
						for i in range(int(n), 10, -10):
							fpNew.write("\tsta" + str(i - 9) + ".cmd(\"ip r a 198.51.100.100 via 192.168.10." + str(i - 19) + "\")\n")
							fpNew.write("\tsta" + str(i - 9) + ".cmd(\"echo 1 > /proc/sys/net/ipv4/ip_forward\")\n")
					"""

					if n >= 50 :
						for i in range(5, n - 10, 9):
							fpNew.write("\tsta" + str(i).zfill(2) + ".cmd(\"ip r a 192.168.10." + str(n - 9) + " via 192.168." + str(n + 9) + "\")\n")
						for i in range(n - 9, 10, -9):
							i -= 1 if i < 50 else 0
							j = i - 10 if i > 50 else 0 if i < 10 else i - 9
							fpNew.write("\tsta" + str(i).zfill(2) + ".cmd(\"ip r a 198.51.100.100 via 192.168." + str(n + 9) + "\")\n")
					else :
						i = n / 10
						j = 5 - i
						for k in range(0, j):
							l = 
							fpNew.write("\tsta" + str(l).zfill(2) + ".cmd(\"ip r a 192.168.10." + str(n - 9) + " via 192.168." + str(n + 9) + "\")\n")


					fpNew.write("\n\n")
					fpNew.write("\tsta05.cmd(\"ip r a 198.51.100.100 via 10.0.0." + str(int(n/2) + 1) + "\")\n")
					fpNew.write("\tap1.cmd(\"ip r a 192.168.10." + str(n - 9) + " via 10.0.0.5\")\n")
				elif '*** Running Test' in line :
					fpNew.write(line)
					if n == 10 :
						fpNew.write("\tsta0" + str(n - 9) + ".cmd(\"ping -c600 -s1232 198.51.100.100 | tee log/A_W_6_0L_"+str(n)+".log\")\n")
					else:
						fpNew.write("\tsta" + str(n - 9) + ".cmd(\"ping -c600 -s1232 198.51.100.100 | tee log/A_W_6_0L_"+str(n)+".log\")\n")

				else :
					fpNew.write(line)

if __name__ == "__main__" :
    os.chdir('/home/wifi/mn/test')
    func(int(sys.argv[1]))
