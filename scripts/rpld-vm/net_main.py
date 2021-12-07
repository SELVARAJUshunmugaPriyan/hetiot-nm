#!/usr/bin/python3
import subprocess

def subprocessCaller(cmd):
    subprocess.run(cmd.split(), capture_output=True).stdout.decode("utf8")
    return

def upwardRoute():
    for i in range(3, 38):
        if i % 6 == 2 and i != 2 :
            d = i - 6
        elif i <= 7 :
            d = i - 1
        else:
            d = i - 7
        cmd = "ip netns exec ns" + str(i-1) + " ip -6 r a 2005::1/128 via 2005::" + str(d)
        print(cmd)
        subprocessCaller(cmd)
    return
        
def downwardRoute():
    for i in range(36, 1, -1):
        if i % 6 == 1 :
            d = i + 6
        elif i >= 32 :
            d = i + 1
        else:
            d = i + 7
        cmd = "ip netns exec ns" + str(i-1) + " ip -6 r a 2005::37/128 via 2005::" + str(d)
        print(cmd)
        subprocessCaller(cmd)
    return
    
if __name__ == '__main__' :
    upwardRoute()
    downwardRoute()