#!/usr/bin/env python2.7
import os
import sys
import pandas as pd
import numpy as np
import glob
from terminal_diary import year_lst,initialize_WEB_FILE_LOC_directory
WEB,web_path,data_path = initialize_WEB_FILE_LOC_directory()
# WEB,web_path,data_path = initialize_WEB_FILE_LOC_directory(debug=True)
def main(args=None):
    try: 
        keyword =  sys.argv[1]
        flag = sys.argv[2]
    except(IndexError):
        print ('''
            ------------------------------------------------------
            || WARNING: Missing Keyword or Output Type Flags !! ||
            ------------------------------------------------------
            ''')
        print('''
            ``organize`` compiles the diary files by their tags for easy viewing and reference

            >    organize     <tag keyword>   <format>  <pdf>
            Ex) If I want all my physics notes in diary format (include time stamps) as a pdf
            > organize physics diary pdf

            Without Timestamps, plain text mode:
            > organize physics notes

            Compile a list of all keywords that you have ever used:

            > organize word list
            ''')
    try:
        pdf = sys.argv[3]
    except  (IndexError):
        pdf =""
        pass

    date = ""
    time=""
    tag1=""
    tag2=""
    content=""

    mega_content  = []
    content = ""
    FIRST=True

    for filename in glob.glob("daily/*.md"):
        f = open(filename)
        for line in f.readlines():
            if (line[:4] in year_lst):
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
                    #print mega_content
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
            else:
                content+=line
    mega_content.append([date,time,tag1,tag2,content])
    df = pd.DataFrame(mega_content, columns=['date', 'time', 'tag1','tag2','content'])
    if not os.path.exists("org_md"):
        os.makedirs("org_md")
    f = open("org_md/{}.md".format(keyword),'w')
    for index, row in df.iterrows():
        if flag == 'notes':
            if row['tag1']==keyword or  row['tag2']==keyword:
                f.write(row['content'])
        elif flag == 'diary':
            if row['tag1']==keyword or  row['tag2']==keyword:
                f.write("\n __"+row['date'] +"    "+ row['time']+"__ : \n ")
                f.write(row['content'])
    f.close()
    if keyword == "word":
        #Organize a list of words that has be used as keywords and ignore certain keywords
        exclude = open("exclude_keywords",'r').readlines()
        f = open("{}.md".format(keyword),'w')
        for i in np.unique(df['tag1']):
            if (i+"\n" not in exclude):
                f.write(i+"\n")
        f.close()
    if pdf=='pdf' or pdf=='pdf!':
        print ("Rending pdf with Pandoc")
        if not os.path.exists(flag):
            os.makedirs(flag)
        os.system("pandoc -V geometry:margin=0.5in -o {0}/{1}.pdf org_md/{1}.md --latex-engine=xelatex --wrap=preserve".format(flag,keyword))
        if pdf=="pdf":
            os.system("open {0}/{1}.pdf".format(flag,keyword)) 
    else:
        os.system("cat org_md/{}.md".format(keyword))