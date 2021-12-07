#!/bin/bash

rm ip_map.txt
#tmp=`echo $1'^2' | bc`
tmp=`echo $1'/2' | bc`

while [[ $(ip netns exec ns$tmp ip a show lowpan$tmp | grep "global" | awk '{ print $2 }') != *"2005::"* ]]
do
	echo 'WAIT'
	sleep 1
done
for i in `seq $tmp -1 0`
do
	string1=`ip netns exec ns$i ip a show lowpan$i | grep "global" | awk '{ print $2 }'`
	string2=`echo $string1 | rev | cut -c4- | rev`
	echo 'lowpan'$i' '$string2 >> /home/wifi/rpld/test/ip_map.txt
	if [[ i -eq $tmp ]]
	then
		ssh wifi@192.168.1.100 sudo jool_siit -i "example" eamt flush
		ssh wifi@192.168.1.100 sudo jool_siit -i "example" eamt add 2001::2/128 198.51.100.99/32
		ssh wifi@192.168.1.100 sudo jool_siit -i "example" eamt add 2002::1/128 192.0.2.16/32
		ssh wifi@192.168.1.100 sudo jool_siit -i "example" eamt add $string2/128 198.51.100.100/32
		ssh wifi@192.168.1.100 sudo jool_siit -i "example" eamt add 2003::1/128 192.168.10.`echo $1"-9" | bc`/32
		ssh wifi@192.168.1.100 sudo jool_siit -i "example" eamt display
	fi
done
