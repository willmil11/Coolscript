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
import os
#Patch some imports
def time():
    return rtime() * 1000
def sleep(ms):
    sleep(ms / 1000)
    return None
def perf_counter():
    return rperf_counter() * 1000
#Create console function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Messages
version = "0.0.1"

class messages:
    def help():
        print("----- Coolscript Help -----")
        print(" coolscript --help - Shows this message")
        print("            <file> - Runs the file")
        print("            --version - Shows the version")
        print("            <nothing> If there are no args it will open live interpreter.")
        print("            --live - Opens live interpreter.")
        print("---------------------------")
    def version():
        print("v" + version)

#If arg is --help
#TODO: Do that.