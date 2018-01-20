#!/usr/bin//python
import urllib
import urllib2
import re, sys
import os
from termcolor import colored

def screen():

	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')

screen()


banner = ''' 
 ____   ___  _                 _  __    ____             _    
/ ___| / _ \| |    _ __  _   _| |/ /___|  _ \  ___  _ __| | __
\___ \| | | | |   | '_ \| | | | ' // _ \ | | |/ _ \| '__| |/ /
 ___) | |_| | |___| | | | |_| | . \  __/ |_| | (_) | |  |   < 
|____/ \__\_\_____|_| |_|\__,_|_|\_\___|____/ \___/|_|  |_|\_\
                                                              
                               [Auhtor : Unknown]


'''

#print colored(banner,'green')

data = str(sys.argv[1])
dork = data

#dork = raw_input("Enter the SQL Injection Dork (eg: index.php?id=1) : ")
dork_str = str(dork)
end1="No results found for <strong>"+dork_str+"</strong>"
end2='''title="Next page" href='''
print "Searching for: "+colored(dork_str,'green')
print ""
dork_encode = urllib.quote_plus(dork_str)
def main():
	try:
		
		next = 1
		while(next<=1000):

			bing = "https://www.bing.com/search?q="+dork_encode+"&go=Submit&qs=n&pq="+dork_encode+"&first="+str(next)+"&FORM=PERE"
                        next = next + 10
			data = urllib2.Request(bing)
			bf = urllib2.urlopen(data).read()
			if end1 in bf:
				break
			find = re.findall('<h2><a href="\S+', bf)
			
			for b in find:
				m = b.replace('<h2><a href="http://', "http://").replace('<h2><a href="', "")

				QL = m.replace('"', "").replace('amp;', "")

				with open('tmp.txt', 'a') as f:
					f.write(QL)
					f.write("\n")
			if end2 not in bf:
				break
		try:	
			st = open("tmp.txt" , 'r').read().splitlines()
			lines = set(st)
			count = 0
			for line in lines:
				with open('sitedata.txt', 'a') as links:
					count = count + 1
					links.write(line)
					links.write("\n")
					print line

			print ""
			print colored("Total Sites: " + str(count),'green')
			print colored("List of websites saved in Output.txt",'green')
			os.unlink("tmp.txt")
		except Exception, s:
			print colored("No websites found",'red')

	except Exception, e:
		print colored(e,'red') 
main()
