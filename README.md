# Mikrotik Compliance Scanner
This project is a compliance scanner for Mikrotik routers. It verifies best practices have been implemented and the attack surface of your router is minimized as much as possible.

See the [License section](#license) below for licensing details, and the [Manito Networks Router Hardening Guide](https://www.manitonetworks.com/mikrotik/2016/5/24/mikrotik-router-hardening) for Mikrotik to see an outline of what all will eventually be covered beyond what's currently supported.

1. [Project Goals](#project-goals)
2. [Features](#features)
    1. [Quick Installation](#quick-installation)
    2. [Weighted Scoring](#weighted-scoring)
    3. [Default Credential Checks](#default-credential-checks)
    4. [TCP Services Scan](#tcp-services-scan)
    5. [SNMP Public Community Check](#snmp-public-community)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Debugging](#debugging)
6. [Contributing](#contributing)
7. [License](#license)
8. [Attributions](#attributions)

# Project Goals
Our goal is to provide an easy to use Python script that supports the best practices documented in the [Manito Networks Router Hardening Guide](https://www.manitonetworks.com/mikrotik/2016/5/24/mikrotik-router-hardening) for Mikrotik routers. We think that network audits should be:
- Objective
- Repeatable
- Automatable

By using an automated script and standard JSON output we hope you'll be able to make regular device scanning part of your culture.

# Features
The scanner has the following features and functions:

1. [Quick Installation](#quick-installation)
2. [Weighted Scoring](#weighted-scoring)
3. [Default Credential Checks](#default-credential-checks)
4. [TCP Services Scan](#tcp-services-scan)
5. [SNMP Public Community Check](#snmp-public-community)

## Quick Installation
It takes about 10 minutes to clone the Gitlab repository, add your router IP addresses to the config.py file, and run your first scan. 

Check out [the installation documentation](./Install/README.md) for the few quick commands to get up and running.

## Weighted Scoring
Network audits (and indeed all audits) should be **objective** and **repeatable**, with a scoring system to help prioritize remediation steps. The scanner provides a composite weighted score, with critical vulnerabilities (eg factory-default logins) weighted heavier than less-pressing issues like running FTP instead of SSH.

The following overall grading system is used:

Check                           | Scoring       | Weight    | Criticality |
---                             | ---           | ---       | --- |
Factory-default Credentials     | Pass / Fail   | Heavy     | High |
Running TCP Services            | Numeric       | Normal    | Low to Moderate |
"Public" SNMP Communities       | Pass / Fail   | Heavy     | High |

Scores and their respective weights are combined into a composite score so you can compare devices side-by-side and prioritize remediation.

## Default Credential Checks
One of the most important things to do on a device before bringing it online is to change the factory-default credentials. Compromised devices on the internet using factory credentials are a huge contributor to botnets like Mirai and others, and it's important you don't allow your devices to be co-opted into DDoS attacks and spam networks.

## TCP Services Scan
The scanner checks for services running on the router, including:

Service                 | Score Penalty | Remediation Suggestion |
---                     | ---           | ---   | 
FTP                     | Yes           | Use SSH for secure remote file transfer |
SSH                     | --            | -- |
Telnet                  | Yes           | Use SSH for secure remote console access |
DNS                     | --            | -- |
HTTP                    | Yes           | Use HTTPS for web interface access |
BGP                     | --            | -- |
HTTPS                   | --            | -- |
SOCKS Proxy             | --            | -- |
PPTP VPN                | Yes           | Upgrade to IPSEC or SSL-based VPNs |
MME Gateway Protocol    | --            | -- |
Bandwidth Test Server   | Yes           | Disable when not in use |
UPnP                    | --            | -- |
Winbox                  | --            | -- |
API                     | Yes           | Use API-SSL |
API-SSL                 | --            | -- |
HTTP Proxy              | --            | -- |

See the [config.py](./Python/config.py) file for point deductions per service.

## SNMP Public Community Check
SNMP reachability with the default "public" community string is checked, because a device open for SNMP queries is an information goldmine during the [Scanning and Enumeration](http://www.techrepublic.com/blog/it-security/the-five-phases-of-a-successful-network-penetration/) phase of an attack.

# Requirements
A Linux or Windows computer with Python 2.7 and access to PIP for installing required modules.

# Installation
Install by cloning the latest Git repo, then run the Ubuntu installation script.

See the [installation documentation](Install/README.md) for more information.

# Debugging
If you run into any issues during or after installation check out the [Run Scans installation section](./Install/README.md#run-scans) for helpful commands and debugging options.

# Contributing
We encourage people who use the scanner to contribute to the project if they find a bug or documentation issue, or want to see a feature added. See the [Contributing page](CONTRIBUTING.md) for more information about contributing code to the project.

# License
Copyright (c) 2016, Manito Networks, LLC
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Attributions
"_Mikrotik_" is a trademark of Mikrotikls SIA.

# ---
**Copyright (c) 2016, Manito Networks, LLC**
**All rights reserved.**