import sys

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
