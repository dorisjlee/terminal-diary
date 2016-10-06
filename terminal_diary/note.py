#!/usr/bin/env python2.7
import sys
import os
import time
import glob
import datetime
WEB=True
here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)
web_path = open(here+"/../WEB_LOC").read()
if web_path=="none":
	WEB=False
data_path = open(here+"/../FILE_LOC").read()
os.chdir("../../../../../../../")
os.chdir(data_path)
if not os.path.exists("terminal-notes"):
    os.system("mkdir {}".format("terminal-notes"))
os.chdir("terminal-notes")

def main(args=None):
	today = str(datetime.date.today()).replace("-","_")
	timestamp =  str(datetime.datetime.now()).split(".")[0]
	try:
		tag = sys.argv[1]
		if not os.path.exists("daily"):
		    os.makedirs("daily")
		fname = 'daily/{}.md'.format(today)
		f = open(fname, 'a')   
		f.write(timestamp+ "     "+ tag+"        \n \n")
		f.close()
		os.system("vim "+fname)
		if WEB:
			f = open(fname, 'r') 
			# get unique list of topics
			lines = f.readlines()
			tags=[]
			for l in lines:
				phrase = l.split()
				try:
					if phrase[0][:4]=='2016':
						tags.append(phrase[2])
				except:
					pass
			tag=''
			tag_temp_name=''
			for i in list(set(tags)):
				tag+='- {}\n'.format(i)
				tag_temp_name+='_{}'.format(i)
			for _f in glob.glob(os.path.expanduser("~/{0}/{1}".format(web_path,'{0}-*.md'.format(str(datetime.date.today()))))):
				print "Removed "+_f
				os.system("rm {}".format(_f))
			f1 = open(os.path.expanduser("~/{0}/{1}".format(web_path,'{0}-{1}.md'.format(str(datetime.date.today()),tag_temp_name))), 'w') 
			# Insert Jekyll Header for Blogpost
			f1.write('''---
layout: post
title:  {0} Worklog
date:  {0}
tags:
{1}
categories:
- Work
---
'''.format(str(datetime.date.today()),tag))
			 
			f1.writelines(lines)
			f.close()
			f1.close()
			# os.system("cp  {0} ~/{1}/{2}".format(fname,web_path,'{}-worklog.md'.format(today)))
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