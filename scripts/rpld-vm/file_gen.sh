#/bin/bash
for i in `seq 1 36`
do
	touch lowpan$i.conf
	echo -e "ifaces = { {" >> lowpan$i.conf
	echo -e "\t-- the interface to run on!" >> lowpan$i.conf
	echo -e "\tifname = \"lowpan"$i"\"," >> lowpan$i.conf
	echo -e "\t-- we are not the dodag_root!" >> lowpan$i.conf
	echo -e "\tdodag_root = false," >> lowpan$i.conf
	echo -e "}, }" >> lowpan$i.conf
	echo -e "\n" >> lowpan$i.conf
	echo -e "-- vim: syntax=lua" >> lowpan$i.conf
done
