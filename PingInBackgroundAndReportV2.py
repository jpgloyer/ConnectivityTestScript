#To run properly, run in command shell with
#"python PypingTest.py > PingTestResults.txt"

#Because I suck at coding, this will output the log to two separate text files
#One file will be the pinging statistics, the other will be a list of times the commands were run at
#I'll write code to consolidate the two, but in the meantime, find and replace "data:" with "data:     <<<<<-----" in the PingTestResults.txt file
#This will allow easy location of each new entry, and a good point for the new code to be able to find and insert the corresponding timestamp to

#J. Pierce Gloyer for ShoMe Technologies


import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import time
import datetime
import os


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


    #If range if 0-240 and sleep time is 15, this will ping and log response every 15 seconds for an hour 
subprocess.call('echo My Connectivity Log:',shell=True)
subprocess.call('ipconfig', shell=True)
for i in range(0,240,1):
    subprocess.call('echo --------------------------------------------------------------------------------', shell=True)
    subprocess.call('echo %date%', shell=True)
    subprocess.call('echo %time%', shell=True)
    ping("google.com")
    time.sleep(15)