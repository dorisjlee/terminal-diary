import os

year_lst = ['2016','2017','2018']

def initialize_WEB_FILE_LOC_directory():
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
    return WEB,web_path,data_path

def main():
    print('''
    --------------------------
    ||    Terminal Diary    ||
    --------------------------
    List of available commands: 

    ``note`` opens up a new note in your favorite Text Editor.

        > note  <tag keyword>

        Ex) Writing a new note about astronomy
    
        > note astro

    ``organize`` compiles the diary files by their tags for easy viewing and reference
	
	>    organize     <tag keyword>   <format>  <pdf>
	Ex) If I want all my physics notes in diary format (include time stamps) 
	> organize physics diary
	
	Compile a list of all keywords that you have ever used 
	> organize  word list 

    '''
    )
