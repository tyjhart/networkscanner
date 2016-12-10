# Preface
The installation is orchestrated with Git and Pip, and it should require very little manual intervention on your part. Follow the steps in order, and report any problems you run into via an Issue on the Gitlab project page.

# Overview
1. [Installation](#installation)
    1. [Clone the Git Repository](#clone-the-git-repository)
    2. [Run the Installation Script](#installation-script)
2. [Add Devices](#add-devices)
3. [Run Scans](#run-scans)

# Installation
Follow the steps below in order and the installation should take no more than about 10 minutes. Copy-paste commands for easier installation.

## Clone the Git Repository
If you don't have Git installed that's OK, just do the following:

On Ubuntu Linux:
```
sudo apt-get install git
```

On Windows:
```
Download the installer from https://git-for-windows.github.io/
```

Once Git is ready to go, clone the Git repository:
```
git clone https://gitlab.com/thart/networkscanner.git
```

The download should only take a moment, then change directory to the repo's Install directory:
```
cd networkscanner/Install
```

## Installation Script
The install.sh script handles almost everything, just be sure to run it with sudo privileges:
```
sudo sh install.sh
```

# Add Devices
Modify the config.py file to include your Mikrotik device IP addresses. Examples are included in the file, and a backup copy of the file is included (config_default.py) just in case you need it. Replace the IP addresses in the file with your own.

An example of this section of the config.py file is shown below:
```
# Your targets go here in Python list type format, see the following examples
# targets = ["192.168.1.1"]
# targets = ["router01.example.com","192.168.1.1","192.168.2.1","192.168.3.1"]
targets = ["192.168.56.101","192.168.56.102"]
```

# Run Scans
Run the Python scanner.py file, as shown below:
```
python scanner.py
```
This will output JSON scan results.

For additional verbose output set the logging level:
```
python scanner.py -l info
python scanner.py --log=info
```
This will output scan activity dialog, as well as JSON scan results.

To output JSON scan results to a file:
```
python scanner.py &> scan_results.json
```

# ---
**Copyright (c) 2016, Manito Networks, LLC**
**All rights reserved.**