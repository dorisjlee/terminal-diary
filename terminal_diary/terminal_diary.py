import os

year_lst = map(lambda x: str(x),range(2015,2050))

def initialize_WEB_FILE_LOC_directory(debug=False):
    WEB=True
    if debug:
        web_path = "~/Desktop/PersonalProj/web_diary/_posts"
        data_path = "~/Dropbox/"
        os.chdir(os.path.expanduser(data_path))
        os.chdir("terminal-notes")
    else:
        here = os.path.abspath(os.path.dirname(__file__))
        os.chdir(here)
        web_path = open("../WEB_LOC").read()
        if web_path=="none":
            WEB=False
        data_path = open("../FILE_LOC").read()
        # os.chdir("../../../../../../../")
        os.chdir(os.path.expanduser(data_path))
        if not os.path.exists("terminal-notes"):
            os.system("mkdir {}".format("terminal-notes"))
        os.chdir("terminal-notes")
    print "Current Location:", os.getcwd()
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
