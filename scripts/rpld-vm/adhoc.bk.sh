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


if [ $p -eq '31' -a $p -eq '26' ]
then
	if [ $p -eq '31' ]
	then
		ip netns exec ns31 ip -6 r a 2003::1/128 via 2005::26 dev lowpan31
	fi
	ip netns exec ns25 ip -6 r a 2003::1/128 via 2005::20 dev lowpan25
	ip netns exec ns19 ip -6 r a 2003::1/128 via 2005::14 dev lowpan19
	ip netns exec ns13 ip -6 r a 2003::1/128 via 2005::8 dev lowpan13
	ip netns exec ns7 ip -6 r a 2003::1/128 via 2005::2 dev lowpan7
	ip netns exec ns1 ip -6 r a 2003::1/128 via 2005::1 dev lowpan1
	ip netns exec ns0 ip -6 r a 2003::1/128 via 2001::1 dev lowpan0
elif [ $p -eq '21' ]
then
	ip netns exec ns20 ip -6 r a 2003::1/128 via 2005::15 dev lowpan20
	ip netns exec ns14 ip -6 r a 2003::1/128 via 2005::9 dev lowpan14
	ip netns exec ns8 ip -6 r a 2003::1/128 via 2005::3 dev lowpan8
	ip netns exec ns2 ip -6 r a 2003::1/128 via 2005::2 dev lowpan2
	ip netns exec ns1 ip -6 r a 2003::1/128 via 2005::1 dev lowpan1
	ip netns exec ns0 ip -6 r a 2003::1/128 via 2001::1 dev lowpan0
elif [ $p -eq '16' ]
then
	ip netns exec ns15 ip -6 r a 2003::1/128 via 2005::10 dev lowpan15
	ip netns exec ns9 ip -6 r a 2003::1/128 via 2005::4 dev lowpan9
	ip netns exec ns3 ip -6 r a 2003::1/128 via 2005::3 dev lowpan3
	ip netns exec ns2 ip -6 r a 2003::1/128 via 2005::2 dev lowpan2
	ip netns exec ns1 ip -6 r a 2003::1/128 via 2005::1 dev lowpan1
	ip netns exec ns0 ip -6 r a 2003::1/128 via 2001::1 dev lowpan0
elif [ $p -eq '11' -a $p -eq '6' ]
then
	if [ $p -eq '11' ]
	then
		ip netns exec ns10 ip -6 r a 2003::1/128 via 2005::5 dev lowpan10
	elif [ $p -eq '6' ]
	then
		ip netns exec ns5 ip -6 r a 2003::1/128 via 2005::5 dev lowpan5
	fi
	ip netns exec ns4 ip -6 r a 2003::1/128 via 2005::4 dev lowpan4
	ip netns exec ns3 ip -6 r a 2003::1/128 via 2005::3 dev lowpan3
	ip netns exec ns2 ip -6 r a 2003::1/128 via 2005::2 dev lowpan2
	ip netns exec ns1 ip -6 r a 2003::1/128 via 2005::1 dev lowpan1
	ip netns exec ns0 ip -6 r a 2003::1/128 via 2001::1 dev lowpan0
fi


if [ $p -eq '31' -a $p -eq '26' ]
then
	if [ $p -eq '31' ]
	then
		ip netns exec ns19 ip -6 r a 2005::$p/128 via 2005::26 dev lowpan19
	fi
	ip netns exec ns13 ip -6 r a 2005::$p/128 via 2005::20 dev lowpan13
	ip netns exec ns7 ip -6 r a 2005::$p/128 via 2005::14 dev lowpan7
	ip netns exec ns1 ip -6 r a 2005::$p/128 via 2005::7 dev lowpan1
	ip netns exec ns0 ip -6 r a 2005::$p/128 via 2005::2 dev lowpan0
elif [ $p -eq '21' ]
then
	ip netns exec ns8 ip -6 r a 2005::$p/128 via 2005::15 dev lowpan8
	ip netns exec ns2 ip -6 r a 2005::$p/128 via 2005::9 dev lowpan2
	ip netns exec ns1 ip -6 r a 2005::$p/128 via 2005::3 dev lowpan1
	ip netns exec ns0 ip -6 r a 2005::$p/128 via 2005::2 dev lowpan0
elif [ $p -eq '16' ]
then
	ip netns exec ns3 ip -6 r a 2005::$p/128 via 2005::10 dev lowpan3
	ip netns exec ns2 ip -6 r a 2005::$p/128 via 2005::4 dev lowpan2
	ip netns exec ns1 ip -6 r a 2005::$p/128 via 2005::3 dev lowpan1
	ip netns exec ns0 ip -6 r a 2005::$p/128 via 2005::2 dev lowpan0
elif [ $p -eq '11' -a $p -eq '6' ]
then
	ip netns exec ns3 ip -6 r a 2005::$p/128 via 2005::5 dev lowpan3
	ip netns exec ns2 ip -6 r a 2005::$p/128 via 2005::4 dev lowpan2
	ip netns exec ns1 ip -6 r a 2005::$p/128 via 2005::3 dev lowpan1
	ip netns exec ns0 ip -6 r a 2005::$p/128 via 2005::2 dev lowpan0
fi
