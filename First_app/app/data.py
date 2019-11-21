#!/usr/bin/python3

__author__ = 'Jan Kempeneers'

import paho.mqtt.client as mqtt
import os, socket, math
from subprocess import call, Popen, PIPE

def get_sine_datapoint(x_value):
    sine_amplitude=100
    sine_displacement=100
    sine_datapoint = int(round(math.sin(math.radians(x_value))*sine_amplitude))+sine_displacement
    return sine_datapoint

def get_ip():
    ip_address = ''
    try:
        cmd="ifconfig | grep '192.168.0'| grep -A 1 '192.168.0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1"
        stdout=Popen(cmd, shell=True, stdout=PIPE).stdout
        ip_address=stdout.read()[:-1].decode("utf-8")

        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.connect(("8.8.8.8",80))
        # ip_address = s.getsockname()[0]
        # s.close()
    except:
        ip_address = ': Sorry, no network available, so no IP address to show.'
    return ip_address

