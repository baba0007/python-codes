import subprocess


def run_maintenance():
    commands = [
        ["sudo", "apt", "update"],
        ["sudo", "apt", "upgrade", "-y"],
        ["sudo", "apt", "autoremove", "-y"],
        ["sudo", "apt", "autoclean"]
    ]

    for cmd in commands:
        print(f"🚀 Running: {' '.join(cmd)}")

        # We run the maintenance commands here
        process = subprocess.run(cmd, capture_output=False, text=False)

        if process.returncode == 0:
            print(f"✅ Success: {' '.join(cmd)}")
        else:
            print(f"❌ Error during {' '.join(cmd)}")
            return  # Stop the whole thing if one fails

    # This only runs AFTER all the commands above finish successfully
    print('\n--- 📊 Final Disk Space Check ---')
    subprocess.run("df -h | head -n 1; df -h | grep '/$'", shell=True)


run_maintenance()
