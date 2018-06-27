#!/usr/bin/python2

import commands as cmd

ip=cmd.getoutput("arp -a | cut -d ' ' -f2")

with open("data.txt","w") as f:
	f.write(ip)


with open('data.txt','r') as f:
	text = f.read()
	text = text.replace("(","")
	text = text.replace(")","")

with open('org_ip.txt','a') as f:
	f.write(text)







print cmd.getoutput("sudo ansible-playbook /home/subham/Desktop/cmd.xml -k -i org_ip.txt")
	
