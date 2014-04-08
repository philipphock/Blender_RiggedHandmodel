#!/usr/bin/env python3

import socket,time
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


p0="{\"finger\":[0,0,0,0,0],\"hand.rot\":[0,0,0],\"hand.loc\":[0,0,0]}"

sock.sendto(p0.encode(),("127.0.0.1",11911))	

	



