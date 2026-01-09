'''
import subprocess

command = ['hostname', '-I']
result = subprocess.run(command, capture_output=True, text=True)

my_ip = result.stdout.strip()

print(my_ip)

'''
# ----------------
'''
import subprocess


devices = ['192.168.3.1', '192.168.1.1', '4.2.2.2']

print('---Start Scanning---')

for ip in devices:
    command = ['ping', '-c', '1', ip]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print(f'{ip} is online.')

    else:
        print(f'{ip} is offline.')

print('---Scan Finished---')

'''

# ----------------------------

# The clock:
'''
from datetime import datetime

now = datetime.now()
timestamp = now.strftime('%Y-%m-%d %H-%M-%S')

print(f'The Current time is : {timestamp}')

# The Notebook: (file handling):
'''
# -----------

# Combination of all log file with time:
'''
import subprocess
from datetime import datetime

target_ip = '8.8.8.8'
now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

command = ['ping', '-c', '1', target_ip]

result = subprocess.run(command, capture_output=True, text=True)

if result.returncode == 0:
    status = 'UP'

else:
    status = 'DOWN'


with open('network_log.txt', 'a') as file:
    file.write(f'{now} Target {target_ip} is {status}\n')


print('Log updated successfully')

'''

# Function:
'''
import subprocess
from datetime import datetime

def log_ping(ip_address):
    now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    
    command = ['ping', '-c', '1', ip_address]
    
    result = subprocess.run(command, capture_output=True, text=True)

    status = 'ONLINE' if result.returncode == 0 else 'OFFLINE'
        
    with open('network_log.txt', 'a') as file:
        file.write(f'{now} {ip_address} is {status}\n')

    print(f'Checked {ip_address}')


ip_address = input('Enter ip address: ')
log_ping(ip_address)
'''

# The Raspberry Pi Update Function 1:
'''
import subprocess

def update_pi():
    print('---1. Updating Package List---')
    cmd1 = ['sudo', 'apt', 'update']
    result1= subprocess.run(cmd1, capture_output=True, text=True)

    print('---2. Upgradind Packages---')
    cmd2 = ['sudo', 'apt', 'upgrade', '-y']
    result2 = subprocess.run(cmd2, capture_output=True, text=True)

    print('---3. Cleaning System---')
    cmd3 = ['sudo', 'apt', 'autoremove']
    result3 = subprocess.run(cmd3, capture_output=True, text=True)


update_pi()
'''

# The Raspberry Pi Update Function 1:
'''
import subprocess

def update_pi():
    print('---1. Updating Package List---')
    cmd1 = ['sudo', 'apt', 'update']
    result1= subprocess.run(cmd1)

    if result1.returncode != 0:
        print('X Error: Could not update package list. Stopping.')

    print('---2. Upgradind Packages---')
    cmd2 = ['sudo', 'apt', 'upgrade', '-y']
    result2 = subprocess.run(cmd2)

    if result2.returncode != 0:
        print('X Error: Upgrade failed.')

    print('---3. Cleaning System---')
    cmd3 = ['sudo', 'apt', 'autoremove', '-y']
    result3 = subprocess.run(cmd3)

    print('V Syetem update and cleanup complete.')

update_pi()
'''
# python version:
'''
import sys

print(sys.executable)
print(sys.version)

'''

import sys
print(sys.executable)

x = 3
y = 5

if x < y:
    print('X is smaller!')






