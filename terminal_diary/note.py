#!/usr/bin/env python2.7
import sys
import os
import time
import datetime

here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)
data_path = open(here+"/../FILE_LOC").read()
os.chdir("../../../../../../../")
os.chdir(data_path)
if not os.path.exists("terminal-notes"):
    os.system("mkdir {}".format("terminal-notes"))
os.chdir("terminal-notes")

def main(args=None):
	today = str(datetime.date.today()).replace("-",'_')
	timestamp =  str(datetime.datetime.now()).split(".")[0]
	try:
		tag = sys.argv[1]
		if not os.path.exists("daily"):
		    os.makedirs("daily")

		f = open('daily/{}.md'.format(today), 'a')
		f.write(timestamp+ "     "+ tag+"        \n \n")
		f.close()
		os.system("vim "+'daily/{}.md'.format(today))
	except (IndexError):
		print ('''
			----------------------------------------------
			|| WARNING: Don't forget to tag the note !! ||
			----------------------------------------------
			''')
		print ('''
		 	``note`` : lets you jot down Markdown notes with tags by opening up your diary file today in a text editor (Vim by default).

		    >    note     <tag keyword>   
		    
		    Ex) note physics
		    >

			''')