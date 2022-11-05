import socket
import time

def method1():
	while True:
		hostname = socket.gethostname()
		IPAddr = socket.gethostbyname(hostname)

		return IPAddr

def method2():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	return s.getsockname()[0]


import paho.mqtt.client as mqtt

#time.sleep(10)
broker_addr = "test.mosquitto.org"
client = mqtt.Client()
client.connect(broker_addr, 1883)

last = method2()
while True:
	try:
		curr = method2()
		client.publish("ISU/SHL/RPI1/IP", curr)

		if last != curr:
			print("changed")
		else:
			print("NOT changed")

		time.sleep(2)
	except:
		print("")