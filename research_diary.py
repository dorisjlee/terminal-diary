import sys
import os
import time
import datetime
today = str(datetime.date.today()).replace("-",'_')
timestamp =  str(datetime.datetime.now()).split(".")[0]
option =  sys.argv[1]
os.chdir("/Users/dorislee/Desktop/PersonalProj/research_diary/")
try:
	#Instead of rating the idea a score, we can tag it with different topic names, separated by comma(no spacing)
    tag = sys.argv[2]
except (IndexError):
    score="-1" 
    print ("Don't forget to tag 'em ")
if option=="new":
    print ("Scribble 'em down before you forget!! " )
    f = open('{}.txt'.format(today), 'a')
#    f.write(tag + "     "+ timestamp+"		")
    f.write(timestamp+ "     "+ tag+"        \n")
    f.close()
    # os.system("open .")
    os.system("vim "+'{}.txt'.format(today))
