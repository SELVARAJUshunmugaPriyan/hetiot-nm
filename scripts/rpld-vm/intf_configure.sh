#!/bin/bash
ip link set enp0s9 netns ns0
ip netns exec ns0 ip a add 2001::2/64 dev enp0s9
ip netns exec ns0 ip link set enp0s9 up
ip netns exec ns0 ip route add 2002::/64 via 2001::1
#ip netns exec ns0 ip route add 2003::/64 via 2001::1