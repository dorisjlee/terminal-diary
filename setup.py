import os
from setuptools import setup

try: 
    os.system("rm terminal_diary/FILE_LOC")
except:
    pass
def user_prompt():
    f = raw_input("\n Please type in the path to the directory where you want to store your notes and press 'Enter': \n (Default: Desktop/terminal-notes) ")

    if f=="":
        f = "Desktop"
    file = open('terminal_diary/FILE_LOC', 'a')
    file.write(f)
    file.close()


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
            'iforgot=terminal_diary.iforgot:main',
            'syncup=terminal_diary.syncup:main'
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
    data_files = [('', ['terminal_diary/FILE_LOC',]),]
)

