#!/usr/bin/env python2.7
import sys
import os
import time
import glob
import datetime
from terminal_diary import year_lst,initialize_WEB_FILE_LOC_directory
WEB,web_path,data_path = initialize_WEB_FILE_LOC_directory()

def main(args=None):
	today = str(datetime.date.today()).replace("-","_")
	edit_note(today)
def edit_note(date):
	timestamp =  str(datetime.datetime.now()).split(".")[0]
	stnd_date = date.replace("_","-")
	try:
		tag = sys.argv[1]
		if not os.path.exists("daily"):
		    os.makedirs("daily")
		fname = 'daily/{}.md'.format(date)
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
					if phrase[0][:4] in year_lst:
						tags.append(phrase[2])
				except:
					pass
			tag=''
			tag_temp_name=''
			for i in list(set(tags)):
				tag+='- {}\n'.format(i)
				tag_temp_name+='_{}'.format(i)
			for _f in glob.glob(os.path.expanduser("~/{0}/{1}".format(web_path,'{0}-*.md'.format(stnd_date)))):
				print "Removed "+_f
				os.system("rm {}".format(_f))
			f1 = open(os.path.expanduser("{0}/{1}".format(web_path,'{0}-{1}.md'.format(stnd_date,tag_temp_name))), 'w') 
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
'''.format(stnd_date,tag))
			 
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