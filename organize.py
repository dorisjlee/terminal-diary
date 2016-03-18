# This script helps you organize the diary files for easy viewing and reference
#To use type in : 
# >    organize     <tag keyword>   <format>
# For example if I want all my HCI notes in diary format (include time stamps) 
# > organize hci diary
# Alternatively this script can also help you compile a list of keywords that you have ever used 
# The command is : 
# > organize  word list

  
import sys
import pandas as pd
import numpy as np
import os
import glob
keyword =  sys.argv[1]
flag = sys.argv[2]
try:
    pdf = sys.argv[3]
except  (IndexError):
    pdf =""
    pass
os.chdir("/Users/dorislee/Desktop/PersonalProj/research_diary/")
year = '2016'
mega_content  = []
content = ""
FIRST=True
for filename in glob.glob("{}_*.md".format(year)):
#    print filename
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
mega_content.append([date,time,tag1,tag2,content])
df = pd.DataFrame(mega_content, columns=['date', 'time', 'tag1','tag2','content'])
#print (df)

f = open("{}.md".format(keyword),'w')
for index, row in df.iterrows():
    if flag == 'notes':
#        print "Notes mode" 
        if row['tag1']==keyword or  row['tag2']==keyword:
#            print row
            f.write(row['content'])
    elif flag == 'diary':
        #print ("Diary mode")
        if row['tag1']==keyword or  row['tag2']==keyword:
#            print row
#            f.write('\n------------------------------------------\n')
            f.write("\n __"+row['date'] +"    "+ row['time']+"__ : \n ")
            f.write(row['content'])
f.close()
if keyword == "word":
    #Organize a list of words that has be used as keywords and ignore certain keywords
    exclude = open("exclude_keywords",'r').readlines()
    #print exclude
    f = open("{}.md".format(keyword),'w')
    for i in np.unique(df['tag1']):
    #    print i 
    #    print i+"\n" not in exclude
        if (i+"\n" not in exclude):
            f.write(i+"\n")
    f.close()
if pdf=='pdf':
    print ("Rending pdf with Pandoc")
    os.system("pandoc -o {0}.pdf {0}.md".format(keyword))
    os.system("open . ") 
else:
    os.system("cat {0}.md".format(keyword))
