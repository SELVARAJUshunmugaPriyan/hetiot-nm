#!/bin/bash

if [ "$EUID" -ne 0 ]
then
	echo "Please run as root"
	exit
fi

dir="/home/wifi/rpld/test"

$dir/ns_setup $1
$dir/ip_mapper $1 &

#tmp=`echo $1'^2' | bc`
tmp=`echo $1'/2' | bc`
p=`echo $tmp'+1' | bc`

for i in `seq 0 $tmp`
do
	ip netns exec ns$i ip a a 2005::`expr $i + 1`/64 dev lowpan$i
	ip netns exec ns$i sysctl -w net.ipv6.conf.all.forwarding=1
	if [[ i -eq 0 ]]
	then
		$dir/intf_configure &
	fi   
done

if [ -z "$2" ]
then
	:
else
	for l in `seq 1 $tmp`
	do
		 ip netns exec ns$l tc qdisc add dev lowpan$l root netem loss $2%
	done 
fi

ip netns exec ns30 ip -6 r a 2003::1/128 via 2005::26 dev lowpan30
ip netns exec ns25 ip -6 r a 2003::1/128 via 2005::20 dev lowpan25
ip netns exec ns19 ip -6 r a 2003::1/128 via 2005::14 dev lowpan19
ip netns exec ns13 ip -6 r a 2003::1/128 via 2005::8 dev lowpan13
ip netns exec ns7 ip -6 r a 2003::1/128 via 2005::2 dev lowpan7
ip netns exec ns1 ip -6 r a 2003::1/128 via 2005::1 dev lowpan1
ip netns exec ns0 ip -6 r a 2003::1/128 via 2001::1 dev enp0s9

ip netns exec ns19 ip -6 r a 2005::$p/128 via 2005::26 dev lowpan19
ip netns exec ns13 ip -6 r a 2005::$p/128 via 2005::20 dev lowpan13
ip netns exec ns7 ip -6 r a 2005::$p/128 via 2005::14 dev lowpan7
ip netns exec ns1 ip -6 r a 2005::$p/128 via 2005::8 dev lowpan1
ip netns exec ns0 ip -6 r a 2005::$p/128 via 2005::2 dev lowpan0
