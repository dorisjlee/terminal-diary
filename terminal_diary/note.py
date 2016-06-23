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
			``organize`` compiles the diary files by their tags for easy viewing and reference

		    >    organize     <tag keyword>   <format>  <pdf>
		    Ex) If I want all my physics notes in diary format (include time stamps)
		    > organize physics diary

		    Without Timestamps:
		    > organize physics notes

		    Compile a list of all keywords that you have ever used:
		    > organize word list

			''')