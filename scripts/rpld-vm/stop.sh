#!/bin/bash

if [ "$EUID" -ne 0 ]
then
	echo "Please run as root"
	exit
fi

killall rpld
killall ip_mapper
killall mesh
killall adhoc
killall testScript

rmmod mac802154_hwsim
rmmod mac802154
rmmod ieee802154_6lowpan
rmmod ieee802154

for i in `seq 0 36`
do
	if [ $i == 0 ]
	then
		ip netns exec ns$i ip l s enp0s9 netns 1
	fi
	ip netns del ns$i
done
