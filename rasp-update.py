import paramiko
import getpass
import time
import subprocess


def connect_pi():
    # --- 1. SETUP DETAILS ---
    pi_ip = '192.168.3.11'
    user = 'pi'
    pwd = getpass.getpass(f'Enter password for {user}@{pi_ip}: ')

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # --- 2. CONNECTING ---
        print(f'\n--- 📞 Calling the Pi at {pi_ip} ---')
        client.connect(hostname=pi_ip, username=user, password=pwd)
        print("✅ Success! The Pi answered the call.")

        # --- 3. THE CHECKLIST OF STAGES ---
        # We put each command in a list so we can run them one-by-one
        stages = [
            {"name": "UPDATE PACKAGE LIST", "cmd": f"echo {pwd} | sudo -S apt update"},
            {"name": "UPGRADE SOFTWARE",    "cmd": f"echo {pwd} | sudo -S apt upgrade -y"},
            {"name": "REMOVE OLD FILES",    "cmd": f"echo {pwd} | sudo -S apt autoremove -y"},
            {"name": "CLEAN CACHE",         "cmd": f"echo {pwd} | sudo -S apt autoclean -y"},
            {"name": "PI-HOLE UPDATE",      "cmd": f"echo {pwd} | sudo -S pihole -up"}
        ]

        # --- 4. RUNNING THE STAGES ---
        for stage in stages:
            start_time = time.time()  # Start the clock for this stage
            print(f"\n🚀 STARTING STAGE: {stage['name']}...")

            # Send the command to the Pi
            stdin, stdout, stderr = client.exec_command(stage['cmd'])

            # Show the output live
            for line in stdout:
                print(f"  {line.strip()}")

            end_time = time.time()  # Stop the clock
            duration = round(end_time - start_time, 2)
            print(f"✅ FINISHED: {stage['name']} (Took {duration} seconds)")

        # --- 5. DISK SPACE CHECK ---
        print('\n--- 📊 Final Disk Space Check ---')
        stdin, stdout, stderr = client.exec_command(
            "df -h | head -n 1; df -h | grep '/$'")
        print(stdout.read().decode())

        # --- 6. THE REBOOT ---
        print('\n--- 🌙 Maintenance Done. Rebooting the Pi... ---')
        client.exec_command(f"echo {pwd} | sudo -S reboot")
        print("👋 The Pi is restarting. See you in 2 minutes!")

        # --- 7. THE WATCHER (PING) ---
        time.sleep(30)  # Wait 30 seconds before we start checking
        print("\n🔍 Waiting for Pi to wake up...")

        while True:
            # -c 1 means send 1 ping
            check = subprocess.run(
                ['ping', '-c', '1', pi_ip], capture_output=True)

            if check.returncode == 0:
                print("🌟 SUCCESS: The Pi is back ONLINE!")
                break
            else:
                print("...still sleeping...")
                time.sleep(5)  # Wait 5 seconds and try again

    except paramiko.AuthenticationException:
        print("❌ Error: Wrong password! The Pi didn't recognize you.")
    except Exception as e:
        print(f"❌ Error: Something went wrong: {e}")
    finally:
        client.close()
        print('\n--- 🔌 Connection Closed ---')
        print('--- 🏁 All Tasks Finished ---')


# --- 8. START THE PROGRAM ---
if __name__ == "__main__":
    connect_pi()
