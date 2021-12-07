#!/bin/bash

if [ "$EUID" -ne 0 ]
then
	echo "Please run as root"
	exit
fi

dir="/home/wifi/rpld/test"

$dir/ns_setup $1
#./testScript &
$dir/ip_mapper $1 &

#n=`echo $1'^2' | bc`
n=`echo $1'/2' | bc`

if [ -z "$2" ]
then
	:
else
	for l in `seq 1 $n`
	do
		 ip netns exec ns$l tc qdisc add dev lowpan$l root netem loss $2%
	done 
fi

for i in `seq 0 $n`
do
	sleep 1
	$dir/invoke_rpld $i &
	if [[ i -eq 0 ]]
	then
		$dir/intf_configure &
	fi
done

#ip netns exec ns36 /usr/sbin/sshd
#ip netns exec ns36 iperf -su &
#ip netns exec ns36 truncate -s 2M empty.file
