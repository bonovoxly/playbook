#!/bin/bash

# delete PID if it already exists.
if [ -f /var/run/openvpn/server.pid ]; then
  echo "Cleaning up old server.pid file..."
  rm /var/run/openvpn/server.pid
fi

# build SSL certificates if they don't already exist.
if [ ! -d /etc/openvpn/keys ]
  echo "OpenVPN keys directory missing.  Creating..."
  cd /etc/openvpn
  source ./vars
  ./clean-all
  /etc/openvpn/build-ca-automated
  /etc/openvpn/build-server-automated
fi

# configure iptables
INTERFACE=eth0
iptables -t nat -C POSTROUTING -s $OVPN_SERVER -o $INTERFACE -j MASQUERADE

# launch OpenVPN
echo "Starting OpenVPN..."
/usr/sbin/openvpn --daemon --writepid /var/run/openvpn/server.pid --cd /etc/openvpn/ --config server.conf
