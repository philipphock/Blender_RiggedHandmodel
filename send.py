#!/usr/bin/env python3

import socket,time
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

SLEEPTIME = 0.05
rot = 180
f = 0

for i in range(72):
	toSend = "{\"finger\":[%d,%d,0,%d,%d],\"hand.rot\":[%d,0,0],\"hand.loc\":[0,0,0]}" % (f,f,f,f,rot)
	
	sock.sendto(toSend.encode(),("127.0.0.1",11911))	
	rot-=2.5
	if i > 72/2:
		f -= 2.5
	time.sleep(SLEEPTIME)



	



