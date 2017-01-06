# Open up yesterday's note
import datetime 
from note import edit_note
from terminal_diary import year_lst,initialize_WEB_FILE_LOC_directory
WEB,web_path,data_path = initialize_WEB_FILE_LOC_directory()

def main(args=None):
	yesterday = str(datetime.date.today()- datetime.timedelta(1)).replace('-','_')
	edit_note(yesterday)