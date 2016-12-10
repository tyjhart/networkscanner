# Copyright (c) 2016, Manito Networks, LLC
# All rights reserved.

# Your targets go here in Python list type format, see the following examples
# targets = ["192.168.1.1"]
# targets = ["192.168.1.1","192.168.2.1","192.168.3.1"]
targets = ["192.168.56.101","192.168.56.102"]

# Ports, with their respective service names, point deductions for unsecure services, and a remediation hint
ports = {
    21:     {"Service":"FTP",                   "Deduction":20,     "Remediation":"Use SSH"},
    22:     {"Service":"SSH",                   "Deduction":0,      "Remediation":"Use SSH"},
    23:     {"Service":"Telnet",                "Deduction":20,     "Remediation":"Use SSH"},
    53:     {"Service":"DNS",                   "Deduction":0,      "Remediation":"N/A"},
    80:     {"Service":"HTTP",                  "Deduction":10,     "Remediation":"Use HTTPS"},
    179:    {"Service":"BGP",                   "Deduction":0,      "Remediation":"Disable when not in use"},
    443:    {"Service":"HTTPS",                 "Deduction":0,      "Remediation":"N/A"},
    1080:   {"Service":"SOCKS Proxy",           "Deduction":0,      "Remediation":""},
    1723:   {"Service":"PPTP VPN",              "Deduction":5,      "Remediation":"Use IPSEC or SSL VPN"},
    1966:   {"Service":"MME Gateway Protocol",  "Deduction":0,      "Remediation":"N/A"},
    2000:   {"Service":"Bandwidth Test Server", "Deduction":10,     "Remediation":"Disable when not in use"},
    2828:   {"Service":"UPnP",                  "Deduction":0,      "Remediation":"N/A"},
    8291:   {"Service":"Winbox",                "Deduction":0,      "Remediation":"N/A"},
    8728:   {"Service":"API",                   "Deduction":5,      "Remediation":"Use API-SSL"},
    8729:   {"Service":"API-SSL",               "Deduction":0,      "Remediation":"N/A"},
    8080:   {"Service":"HTTP Proxy",            "Deduction":0,      "Remediation":"N/A"}
}