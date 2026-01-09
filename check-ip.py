import subprocess

def check_device(ip):
    # This runs the command: ping -c 1 [IP_ADDRESS]
    status = subprocess.run(['ping', '-c', '1', ip], capture_output=True)
    
    if status.returncode == 0:
        print(f"✅ Device {ip} is UP!")
    else:
        print(f"❌ Device {ip} is DOWN!")
ip = input('Enter IP : ')
check_device(ip) # Put any ip to check if it is up.
