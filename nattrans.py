import string
import socket
import argparse

parser = argparse.ArgumentParser(description='Convert static NATS pre 8.3 into current format')
parser.add_argument('file', help='file of nats',type=file)
parser.add_argument('--dns', help='Do DNS lookup for description',action='store_true')

args=parser.parse_args()
file = args.file.readlines()
dnsc = args.dns

for line in file:
	workline=string.split(line)
	realaddr = workline[3]
	nataddr = workline[2]
	natcmd = workline[1]
        print "object network obj-"+realaddr
	if dnsc: 
                try:
                        lookup=socket.gethostbyaddr(nataddr)[0]
                except: 
                        lookup="Unknown"
                print " description "+lookup
	print " host "+realaddr
	print " nat"+natcmd+" static "+nataddr+"\n"


 	










