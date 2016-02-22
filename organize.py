# This script helps you organize the diary files for easy viewing and reference
#To use type in : 
# >    organize        <tag keyword>   <format>
# For example if I want all my HCI notes in diary format (include time stamps) 
# > organize hci diary
  
import sys
import pandas as pd
import numpy as np
keyword =  sys.argv[1]
flag = sys.argv[2]
import os
import glob
os.chdir("/Users/dorislee/Desktop/PersonalProj/research_diary/")
year = '2016'
mega_content  = []
content = ""
FIRST=True
for filename in glob.glob("{}_*.txt".format(year)):
 #   print filename
    f = open(filename)
#    content=""
    for line in f.readlines():
#         print line.split()
#        content = ""
        if (line[:4]==year):
            if (FIRST):
                line = line.split()
                date = line[0]
                time = line[1]
                tags = line[2].split(",")
                tag1 = tags[0]
                try:
                    tag2 = tags[1]
                except (IndexError):
                    tag2=""
                content =""
                FIRST=False
            else:
                mega_content.append([date,time,tag1,tag2,content])
                line = line.split()
                date = line[0]
                time = line[1]
                tags = line[2].split(",")
                tag1 = tags[0]
                try:
                    tag2 = tags[1]
                except (IndexError):
                    tag2=""
                content =""
       # content = line
        else:
            content+=line
#    print content 
#    mega_content.append([date,time,tag1,tag2,content])
df = pd.DataFrame(mega_content, columns=['date', 'time', 'tag1','tag2','content'])
#print df

f = open("{}.txt".format(keyword),'w')
for index, row in df.iterrows():
    if flag == 'notes':
#        print "Notes mode" 
        if row['tag1']==keyword or  row['tag2']==keyword:
#            print row
            f.write(row['content'])
    elif flag == 'diary':
#        print "Diary mode"
        if row['tag1']==keyword or  row['tag2']==keyword:
#            print row
            f.write('\n------------------------------------------\n')
            f.write(row['date'] +"    "+ row['time']+"\n")
            f.write(row['content'])
f.close()
