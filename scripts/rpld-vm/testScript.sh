#!/bin/bash

#while [[ $(cat ./address) != *"2006::"* ]]
#do
#	echo 'testScript: WAIT'
#	sleep 1
#done

#while [[ $(ip netns exec ns36 ping -c 1 2005::1) != *""* ]]
#do
#	echo 'testScript: WAIT'
#	sleep 1
#done
sleep 1
ip netns exec ns36 ping -c 100 -s 1232 2006::37 > log/A_6_6_0L_6x6_Initial.log
ip netns exec ns36 ping -c 100 -s 1232 2006::37 > log/A_6_6_0L_6x6_Stable.log
#rm ./address
