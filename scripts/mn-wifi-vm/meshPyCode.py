#!/usr/bin/python

import os, sys
import time

def func(n):
	with open("meshOrg", 'r') as fp:
		with open("meshNew", 'w') as fpNew:
			for line in fp.readlines():
				if '*** Creating nodes' in line :
					fpNew.write(line)
					for j in range (0, int(n/10)):
						for i in range(1, 6):
							s = str(j) + str(i)
							t = str(450 - ( j * 50 ))
							u = str(450 - ((5 - i) * 50 ))
							fpNew.write("\tsta" + s + " = net.addStation(\'sta" + s + 
								  "\', position=\'" + u + "," + t + ",0\')\n")
				elif '*** Creating links' in line :
					fpNew.write(line)
					for j in range (0, int(n/10)):
						for i in range(1, 6):
							s = str(j) + str(i)
							fpNew.write("\tnet.addLink(sta" + s + ", cls=mesh, ssid=\'meshNet\', intf=\'sta"
								  + s + "-wlan0\', channel=5)\n")
				elif '*** Running Test' in line :
					fpNew.write(line)
					if n == 10 :
						fpNew.write("\tsta0" + str(n - 9) + ".cmd(\"ping -c600 -s1232 198.51.100.100 | tee log/M_W_6_0L_"+str(n)+str(round(time.time(),0))+".log\")\n")
					else:
						fpNew.write("\tsta" + str(n - 9) + ".cmd(\"ping -c600 -s1232 198.51.100.100 | tee log/M_W_6_0L_"+str(n)+str(round(time.time(),0))+".log\")\n")

				else :
					fpNew.write(line)

if __name__ == "__main__":
	os.chdir('/home/wifi/mn/test')
	func(int(sys.argv[1]))
