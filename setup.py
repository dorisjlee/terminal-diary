import os
from setuptools import setup

try: 
    os.system("rm terminal_diary/FILE_LOC")
except:
    pass
try:
    os.system("rm terminal_diary/DIARY_LOC")
except:
    pass
try:
    os.system("rm terminal_diary/WEB_LOC")
except:
    pass
def user_prompt():
    f0 = raw_input("\n Please type in the path to the directory where you host your Jekyll blogpost, or type 'none' if you chose not to use the web interface.: \n (Default: ~/Desktop/PersonalProj/web_diary/_posts) ")
    if f0 =='':
        f0 = '~/Desktop/PersonalProj/web_diary/_posts'
    file = open('terminal_diary/WEB_LOC', 'a')
    file.write(f0)
    file.close()

    f = raw_input("\n Please type in the path to the directory where you want to store your notes and press 'Enter': \n (Default: ~/Dropbox/terminal-notes) ")
    if f =='':
        f = '~/Dropbox/'
    file = open('terminal_diary/FILE_LOC', 'a')
    file.write(f)
    file.close()

    f2 = raw_input("\n Please type in the path to the directory where you want to store your diaries and press 'Enter': \n (Default: ~/Desktop/PersonalProj/diary.noindex) ")
    if f2=="":
        f2 = '~/Desktop/PersonalProj'
    file2 = open('terminal_diary/DIARY_LOC', 'a')
    file2.write(f2)
    file2.close()


user_prompt()
setup(
    name = "terminal-diary",
    version = "0.9.0",
    author = "Doris Jung-Lin Lee",
    author_email = "dorisjunglinlee@gmail.com",
    description = ("Note-taking app for writing your diary in the terminal"),
    license = "BSD",
    keywords = "note, diary, text-edit",
    url = "https://github.com/dorisjlee/terminal-diary",
    packages=['terminal_diary'],
    entry_points = {
        'console_scripts': [
            'terminal-diary=terminal_diary.terminal_diary:main',
            'organize = terminal_diary.organize:main',
            'note = terminal_diary.note:main',
            'diary = terminal_diary.diary:main',
            'iforgot=terminal_diary.iforgot:main',
            'syncup=terminal_diary.syncup:main',
            'yesterday=terminal_diary.yesterday:main'
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        'numpy>=1.9.0',
        'pandas>=0.16.0'
    ],
    data_files = [('', ['terminal_diary/FILE_LOC',]),
                  ('', ['terminal_diary/DIARY_LOC',]),
                  ('', ['terminal_diary/WEB_LOC',])]
)

