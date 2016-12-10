# Copyright (c) 2016, Manito Networks, LLC
# All rights reserved.

import sys,socket,paramiko,json,datetime,logging, logging.handlers, getopt
from config import *
from pysnmp.hlapi import *

### Get the command line arguments ###
try:
	arguments = getopt.getopt(sys.argv[1:],"hl:",["--help","log="])
	
	for option_set in arguments:
		for opt,arg in option_set:
						
			if opt in ('-l','--log'): # Log level
				arg = arg.upper() # Uppercase for matching and logging.basicConfig() format
				if arg in ["CRITICAL","ERROR","WARNING","INFO","DEBUG"]:
					log_level = arg # Use what was passed in arguments

			elif opt in ('-h','--help'): # Help file
				with open("./help.txt") as help_file:
					print(help_file.read())
				sys.exit()

			else: # No options
				pass

except:
    sys.exit("Unsupported or badly formed options, see -h for available arguments.") 

# Set the logging level per https://docs.python.org/2/howto/logging.html
try: 
	log_level # Check if log level was passed in from command arguments
except NameError:
	log_level="INFO" # Use default logging level

logging.basicConfig(level=str(log_level)) # Set the logging level
logging.warning('Log level set to ' + str(log_level) + " - OK") # Show the logging level for debug

# Cache for tuples of (score,weight)
#
# Score: Numeric 0 - 100 /// 0 (Fail), 100 (Pass)
# Weight: Low - 1, Normal - 2, Heavy - 3
score_cache = []

# Cache for line-item result information
result_cache = {}

# SSH scanner
# Example from https://github.com/paramiko/paramiko demo
username = "admin"
password = ""

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Iterate through the target list
for target in targets:
	result_cache[target] = {} # Cache for each target

	now = datetime.datetime.utcnow() # Get the current UTC time
	result_cache[target]["Time"] = now.strftime("%Y-%m-%dT%H:%M:%S") + ".%03d" % (now.microsecond / 1000) + "Z" # Scan UTC timestamp
	
	# SSH Mikrotik default login (admin,"")
	logging.info("Trying default SSH credentials on " + str(target))
	try:
		ssh.connect(target, username=username, password=password) # Connect
		#stdin,stdout,stderr = ssh.exec_command("ip address print")
		ssh.close() # Kill SSH connection

		score_cache.append((0,3)) # Fail, Heavy weight
		result_cache[target]["Default Credentials In Use"] = "Fail"
		logging.info("Default SSH credentials still set on " + str(target) + " - FAIL")
	except paramiko.AuthenticationException:
		score_cache.append((100,3)) # Pass, Heavy weight
		result_cache[target]["Default Credentials In Use"] = "Pass"
		logging.info("Default SSH credentials failed on " + str(target) + " - PASS")
	except:
		pass

	# TCP Services
	logging.info("Beginning TCP scan of " + str(target))
	result_cache[target]["TCP Services"] = {}

	tcp_score = 100 # Start at 100%
	
	for port_num in ports:
		result_cache[target]["TCP Services"][port_num] = {}
		result_cache[target]["TCP Services"][port_num]["Service"] = ports[port_num]["Service"]
		s = socket.socket()
		
		logging.info("Scanning TCP " + str((target,port_num)))
		try:
			s.connect((target, port_num)) 
			tcp_score -= ports[port_num]["Deduction"]
			result_cache[target]["TCP Services"][port_num]["Status"] = "Not Closed"
			logging.info(str((target,port_num)) + " Not Closed")
		except: 	
			result_cache[target]["TCP Services"][port_num]["Status"] = "Closed"
			logging.info(str((target,port_num)) + " Closed")
		
		s.close()
	score_cache.append((tcp_score,2)) # TCP port score, normal weight
	logging.info("Completed TCP scan of " + str(target))


	# Calculate TCP port weighted score
	total_score = 0
	total_weigth = 0
	for item_score in score_cache:
		total_score = total_score + (item_score[0] * item_score[1]) # Sum of (scores * weights)
		total_weigth = total_weigth + item_score[1] # Sum of weights

	target_weighted_score = total_score / total_weigth # Final weighted score: sum(scores * weights) / sum(weights)
	result_cache[target]["Weighted Score"] = target_weighted_score

	# SNMP Public community probes
	#
	# Based on example from http://pysnmp.sourceforge.net/examples/hlapi/asyncore/sync/manager/cmdgen/snmp-versions.html
	snmp_poller = getCmd(SnmpEngine(),
                  CommunityData('public'),
                  UdpTransportTarget((target, 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

	errorIndication, errorStatus, errorIndex, varBinds = next(snmp_poller)
	
	if errorIndication:  # Public SNMP failed
		score_cache.append((100,2)) # Pass, normal weight
		result_cache[target]["SNMP Public Community In Use"] = "Pass"
	else:
		score_cache.append((0,2)) # Fail, normal weight
		result_cache[target]["SNMP Public Community In Use"] = "Fail"

# Output
print json.dumps(result_cache, sort_keys=True,indent=4, separators=(',', ': '))