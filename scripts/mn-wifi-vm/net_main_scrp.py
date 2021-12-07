#!/usr/bin/python3
import subprocess
from random import sample
from time import sleep
from sys import argv

sampleLinkPair = []

def subprocessCaller(cmd, cap_out=True):
    return subprocess.run(str(cmd).split(), capture_output=cap_out).stdout.decode("utf8")

def choiceGenerator(rng):
    return sample(range(0,rng),1)[0]

def pairer(node):
    
    pairNode = None
    
    if node >= 8 and node <= 29 and node % 6 not in (0, 1):
        choice = choiceGenerator(8)
        if choice == 0 :
            pairNode = node - 7
        elif choice == 1 :
            pairNode = node - 6
        elif choice == 2 :
            pairNode = node - 5
        elif choice == 3 :
            pairNode = node + 1
        elif choice == 4 :
            pairNode = node + 7
        elif choice == 5 :
            pairNode = node + 6
        elif choice == 6 :
            pairNode = node + 5
        else:
            pairNode = node - 1
            
    elif node >= 2 and node <= 5 :
        choice = choiceGenerator(5)
        if choice == 0 :
            pairNode = node + 1
        elif choice == 1 :
            pairNode = node + 7
        elif choice == 2 :
            pairNode = node + 6
        elif choice == 3 :
            pairNode = node + 5
        else:
            pairNode = node - 1
            
    elif node >= 12 and node <= 30 and node % 6 == 0 :
        choice = choiceGenerator(5)
        if choice == 0 :
            pairNode = node + 6
        elif choice == 1 :
            pairNode = node + 5
        elif choice == 2 :
            pairNode = node - 1
        elif choice == 3 :
            pairNode = node - 7
        else:
            pairNode = node - 6
            
    elif node >= 32 and node <= 35 :
        choice = choiceGenerator(5)
        if choice == 0 :
            pairNode = node + 1
        elif choice == 1 :
            pairNode = node - 1
        elif choice == 2 :
            pairNode = node - 7
        elif choice == 3 :
            pairNode = node - 6
        else:
            pairNode = node - 5
            
    elif node >= 7 and node <= 25 and node % 6 == 1 :
        choice = choiceGenerator(5)
        if choice == 0 :
            pairNode = node - 6
        elif choice == 1 :
            pairNode = node - 5
        elif choice == 2 :
            pairNode = node + 1
        elif choice == 3 :
            pairNode = node + 7
        else:
            pairNode = node + 6
            
    elif node == 1:
        choice = choiceGenerator(3)
        if choice == 0 :
            pairNode = node + 1
        elif choice == 1 :
            pairNode = node + 7
        else:
            pairNode = node + 6
                   
    elif node == 6:
        choice = choiceGenerator(3)
        if choice == 0 :
            pairNode = node + 6
        elif choice == 1 :
            pairNode = node + 5
        else:
            pairNode = node - 1
            
    elif node == 36:
        choice = choiceGenerator(3)
        if choice == 0 :
            pairNode = node - 1
        elif choice == 1 :
            pairNode = node - 7
        else:
            pairNode = node - 6
            
    else:
        choice = choiceGenerator(3)
        if choice == 0 :
            pairNode = node + 1
        elif choice == 1 :
            pairNode = node - 6
        else:
            pairNode = node - 5
  
    
    return tuple((node, pairNode))

def interrupter(numOfLinks):
    print(subprocessCaller("./ns_setup.6x6"))
    sampleNodes = sample(range(1,37), numOfLinks)
    global sampleLinkPair
    sampleLinkPair = [ pairer(node) for node in sampleNodes ]
    for (a, b) in sampleLinkPair:
        bashCommand = "wpan-hwsim edge del " + str(a) + " " + str(b)
        print(subprocessCaller(bashCommand))
        bashCommand = "wpan-hwsim edge del " + str(b) + " " + str(a)
        print(subprocessCaller(bashCommand))
    print("Finished interrupter()")
    print("sampleLinkPair :", sampleLinkPair)
    subprocess.Popen("./start".split())
    return

def rectifier():
    global sampleLinkPair
    for (a, b) in sampleLinkPair:
        bashCommand = "wpan-hwsim edge add " + str(a) + " " + str(b)
        print(subprocessCaller(bashCommand))
        bashCommand = "wpan-hwsim edge add " + str(b) + " " + str(a)
        print(subprocessCaller(bashCommand))
    print("Finished rectifier()")
    print(subprocessCaller("./stop"))
    return
    
if __name__ == '__main__' :
    #start_time = time()
    try:
        interval = 300 # default interval is one minute
        for iterator in (1,10):
            for numOfLinks in (7, 15, 22, 30, 37):
                interrupter(numOfLinks)
                sleep(interval)
                print("Finished sleep()")
                rectifier()
    
    except KeyboardInterrupt:
        print("--- Exiting ---")
        #print("--- Executed for %s seconds ---" % (time() - start_time))
    finally:
        rectifier()
