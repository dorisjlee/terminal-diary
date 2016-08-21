import sys
import os
import time
import datetime
today = str(datetime.date.today()).replace("-",'_')
timestamp =  str(datetime.datetime.now()).split(".")[0]
here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)
data_path = open(here+"/../DIARY_LOC").read()
os.chdir("../../../../../../../")
os.chdir(data_path)
if not os.path.exists("diary.noindex"):
    # .noindex dirrectory are not indexed in Mac's Spotlight
    # This way the diary directory stays privated and would not show up in search 
    os.system("mkdir {}".format("diary.noindex"))
    os.chdir("diary.noindex")
def main(args=None):
    try:
        score = sys.argv[1]
        print ("Starting new diary file for {}".format(today) )
        f = open('{}.txt'.format(today), 'a')
        f.write(timestamp)
        f.write("    "+score+"\n")
        f.close()
        os.system("open .")
        os.system("vim "+'{}.txt'.format(today))
    except (IndexError):
        print ('''
        --------------------------------------------------
        || WARNING: Don't forget enter a daily score !! ||
        --------------------------------------------------
        ''')
        print ('''
        ``diary`` : record a daily diary with a daily mood score 

        >    diary     <daily-score>  

        Ex) diary 8

        ''')