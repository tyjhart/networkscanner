# Preface
The installation is orchestrated with Git and Pip, and it should require very little manual intervention on your part. Follow the steps in order, and report any problems you run into via an Issue on the Github project page.

# Overview
1. [Installation](#installation)
    1. [Git](#git)
        - [Ubuntu / Debian Linux](#git-on-ubuntu-debian-linux)
        - [Windows](#git-on-windows)
    2. [Python Pip](#python-pip)
    3. [Clone the Git Repository](#clone-the-git-repository)
    4. [Installation on Linux](#linux)
    5. [Installation on Windows](#windows)
2. [Add Devices](#add-devices)
3. [Run Scans](#run-scans)

# Installation
Follow the steps below in order and the installation should take no more than about 10 minutes. Copy-paste commands for easier installation.

## Git
Make sure Git is installed, then clone the Git repository.

### Git on Ubuntu / Debian Linux
```
sudo apt-get install git
```

### Git on Windows
Download the installer from [the Github for Windows download page](https://git-for-windows.github.io/).

## Python Pip
If you don't have Python Pip installed by default (Windows, some Linux versions, Bash on Ubuntu on Windows) do the following:

### Ubuntu / Debian Linux Pip
```
sudo apt-get install python-pip
```

### Windows Pip
Download the get-pip.py file from [the pypa.io Pip download page](https://pip.pypa.io/en/stable/installing/), then run the following:
```
python get-pip.py
```

## Clone the Git Repository
Clone the Git repository:
```
git clone https://github.com/manitonetworks/networkscanner.git
```

The download should only take a moment, then change directory to the repo's Install directory:
```
cd networkscanner
```

## Linux
Use the following steps to install the network scanner on Linux.

The install.sh script handles almost everything, just be sure to run it with sudo privileges:
```
sudo sh ./Install/install.sh
```

## Windows
Use the following steps to install the network scanner on Windows.

Install Python dependencies with Pip:
```
python -m pip install -r ./Install/requirements.txt
```

Copy the default config_default.py file:
```
copy .\Python\config_default.py .\Python\config.py
```

# Add Devices
Modify the Python/config.py file in the Python directory to include your Mikrotik device IP addresses. Examples are included in the file, and a backup copy of the file is included (config_default.py) just in case you need it. Replace the IP addresses in the file with your own.

An example of this section of the config.py file is shown below, set to scan the devices at 192.168.56.101 and 192.168.56.102:
```
# Your targets go here in Python list type format, see the following examples
# targets = ["192.168.1.1"]
# targets = ["router01.example.com","192.168.1.1","192.168.2.1","192.168.3.1"]
targets = ["192.168.56.101","192.168.56.102"]
```

# Run Scans
Run the Python scanner.py file, as shown below:
```
cd Python
python scanner.py
```
This will output JSON scan results after the scan completes.

For additional verbose output set the logging level:
```
cd Python
python scanner.py -l info
python scanner.py --log=info
```
This will output scan activity dialog, then the JSON scan results.

To output JSON scan results to a .json file do the following:

### Linux JSON File Output
```
cd Python
python scanner.py &> scan_results.json
```

### Windows JSON File Output
```
cd Python
python scanner.py >> scan_results.json
```

# ---
**Copyright (c) 2016, Manito Networks, LLC**
**All rights reserved.**