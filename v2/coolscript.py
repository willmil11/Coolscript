#Coolscript 

#Imports
import json
import random
from time import time as rtime
from time import sleep as rsleep
from time import perf_counter as rperf_counter
from time import perf_counter_ns
import threading
from os import path
import os
from sys import exit
from sys import argv as args
import sys
#Patch some imports
def time():
    return rtime() * 1000
def sleep(ms):
    sleep(ms / 1000)
    return None
def perf_counter():
    return rperf_counter() * 1000

#Check args
#TODO: DO THAT