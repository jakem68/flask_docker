#!/usr/bin/python3

__author__ = 'Jan Kempeneers'

# import paho.mqtt.client as mqtt
import os, socket, math, json, time
from subprocess import call, Popen, PIPE
from yaml_load_dump import yaml_load, yaml_dump

def get_sine(x_value):
    sine_amplitude=50
    sine_displacement=50
    sine_value = int(round(math.sin(math.radians(x_value))*sine_amplitude))+sine_displacement
    return sine_value

def update_sine_dataset(sine_value, sine_dataset):
    sine_dataset["timestamps"].append(int(time.time()))
    sine_dataset["timestamps"].pop(0)
    sine_dataset["sine_values"].append(sine_value)
    sine_dataset["sine_values"].pop(0)
    return sine_dataset

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
