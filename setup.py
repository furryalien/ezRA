import subprocess
import sys
import os
from pathlib import Path

def check_system_dependencies():
    """Check and install required system packages for RTL-SDR"""
    system_packages = [
        'build-essential',
        'libusb-1.0-0-dev',
        'pkg-config',
        'cmake',
        'rtl-sdr',
        'librtlsdr-dev',
        'python3-dev',
        'python3-tk',
        'python3-pip',
        'python3-matplotlib',    # Added matplotlib system package
        'python3-astropy',      # Added astropy system package
        'python3-numpy',        # Added numpy system package
        'libfreetype6-dev',     # Required for matplotlib
        'libpng-dev',           # Required for matplotlib
        'pkg-config',           # Required for matplotlib
        'python3-setuptools',   # Required for package installation
        'python3-pil',         # Required for tkinter images
        'python3-pil.imagetk', # Required for tkinter images
        'usbrelay'             # Required for USB relay control
    ]
    
    try:
        print("Updating package lists...")
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        print("Installing system dependencies...")
        subprocess.run(['sudo', 'apt-get', 'install', '-y'] + system_packages, check=True)
        print("✓ System dependencies installed successfully")

        # Install pyrtlsdr with --break-system-packages flag
        print("Installing pyrtlsdr...")
        subprocess.run(['python3', '-m', 'pip', 'install', 'pyrtlsdr', '--break-system-packages'], check=True)
        print("✓ Successfully installed pyrtlsdr")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False

def main():
    print("Checking and installing required packages...")
    
    # Check system dependencies
    if not check_system_dependencies():
        print("Failed to install system dependencies")
        sys.exit(1)
    else:
        print("\nSetup complete! You can now run ezCol.py")

if __name__ == "__main__":
    main()