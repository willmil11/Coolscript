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
from subprocess import run as subprocess
from dynamicprocessor import *
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

#Interpreter class
class Interpreter:
    class defaultfuncs:
        def consolelog(*args):
            print(*args)
    #Create __init__ function that is ran when a new instance of the
    #Interpreter class is created
    def __init__(self):
        #Init the interpreter
        self.scopes = {
            "global": {
                "variables": {
                    "console": {
                        "type": "object",
                        "value": {
                            "log": {
                                "type": "function",
                                "functype": "native",
                                "code": self.defaultfuncs.consolelog
                            }
                        }
                    }
                },
                "subscopes": {
                    "child": {
                        "variables": {
                            "hello": {
                                "type": "string",
                                "value": "Hello World!"
                            }
                        },
                        "conditional": False,
                        "parent": "global"
                    }
                },
                "conditional": False,
                "parent": None
            }
        }
    #Create the dynamic_processor function that is used to do simple math
    #and other stuff with strings
    def dynamic_processor(self, string):
        returns = None
        try:
            returns = dynamicprocessor.processor.parse(string)
        except Exception as e:
            raise Exception("Error while resolving dynamic data: " + str(e))
        return returns
    #Create fix_dynamic that is used to replace everything that is not a 
    #string or a number before handing it to the dynamic_processor
    def fix_dynamic(self, string, currentscope):
        opened = False
        for index, char in enumerate(string):
            if char == "\"":
                #If there's a char before the current char and its \ then ignore else invert opened
                if index != 0:
                    if string[index - 1] == "\\":
                        continue
                opened = not opened
            else:
                numbers = ["0","1","2","3","4","5","6","7","8","9"]
                operators = ["+","-","*","/"]
                #If not number or operator
                if char not in numbers and char not in operators:
                    if not opened:
                        trim = string[index:]
                        toreplace = {
                            "charsindex": [],
                            "toinsert": [],
                            "trimstartindex": index
                        }
                        varname = ""
                        for index, char in enumerate(trim):
                            if char in numbers or char in operators or char == "\"" or char == "\\":
                                break
                            if char == " ":
                                if varname == "":
                                    continue
                                else:
                                    break
                            varname += char
                            toreplace["charsindex"].append(index)
                        if varname == "":
                            continue
                        scan = self.scanscopevars(currentscope)
                        if varname in scan.keys():
                            toreplace["toinsert"] = scan[varname]
                        else:
                            raise Exception("Variable " + varname + " not found!")
                        string = string[:toreplace["trimstartindex"]] + str(toreplace["toinsert"]) + string[toreplace["trimstartindex"] + len(varname):]
        return string
    #Scan the variables accessible by a scope with the scanscopevars 
    #function
    def scanscopevars(self, scope):
        vars = {}

        def scanscope(s):
            # Add all variables from the current scope
            vars.update(s['variables'])

            # Check if the current scope has a parent scope
            if s.get('parent'):
                # Get the parent scope dictionary from the scopes dictionary
                parent_scope = self.scopes[s['parent']]
                # Recursively call scanscope with the parent scope
                scanscope(parent_scope)

            # Check if the current scope has any conditional child scopes
            for child_scope in s.get('subscopes', {}).values():
                if child_scope.get('conditional', False):
                    # Recursively call scanscope with the conditional child scope
                    scanscope(child_scope)

        # Call scanscope with the initial scope
        scanscope(scope)

        return vars

#Create an instance of the interpreter
coolscript = Interpreter()

print(coolscript.fix_dynamic("\"Hello world!\" + \"1\" + 2 + 1 + console", coolscript.scopes["global"]))

#If arg is --help
if args[1] == "--help":                                                                   
    messages.help()
    exit(0)
else:
    if args[1] == "--version":
        messages.version()
        exit(0)