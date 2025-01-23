import subprocess
import sys

def get_connected_devices():
    """
    Get the list of connected devices using `adb devices`.
    Returns:
        List of device serial numbers.
    """
    result = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.strip().split("\n")
    devices = [line.split()[0] for line in lines[1:] if "device" in line]
    return devices

def execute_adb_command(devices, command):
    """
    Execute an adb command on all connected devices.
    Args:
        devices: List of connected devices.
        command: List of adb command arguments.
    """
    if not devices:
        print("No devices connected.")
        return
    
    for device in devices:
        cmds = ["adb", "-s", device] + command
        print(f"Executing on device: {device}, cmd: {cmds}")
        result = subprocess.run(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Output from {device}:\n{result.stdout}")
        if result.stderr:
            print(f"Error from {device}:\n{result.stderr}")

def print_help():
    """
    Print help message for using the script.
    """
    print("""
Usage:
  python adbs.py devices
      List all connected devices.

  python adbs.py install <path_to_apk>
      Install an APK on all connected devices.

  python adbs.py uninstall <package_name>
      Uninstall an app by package name from all connected devices.

  python adbs.py <adb_command>
      Execute an adb command on all connected devices.
      
  python adbs.py --help
      Show this help message.
    """)

def main():
    if len(sys.argv) < 2:
        print("Error: No command provided.")
        print_help()
        sys.exit(1)
    
    command = sys.argv[1]
    
    # Handle special commands
    if command == "--help":
        print_help()
        return
    
    if command == "devices":
        devices = get_connected_devices()
        print("Connected devices:")
        for device in devices:
            print(f"  {device}")
        return
    
    # Get all connected devices
    devices = get_connected_devices()
    if not devices:
        print("No devices connected.")
        return
    
    # Handle specific operations (install, uninstall) or forward all other commands
    if command == "install":
        #apk_path = sys.argv[2]
        #execute_adb_command(devices, ["install", apk_path])
        execute_adb_command(devices, sys.argv[1:])
    elif command == "uninstall" and len(sys.argv) >= 3:
        package_name = sys.argv[2]
        execute_adb_command(devices, ["uninstall", package_name])
    else:
        # Forward other commands to all devices
        execute_adb_command(devices, sys.argv[1:])

if __name__ == "__main__":
    main()
