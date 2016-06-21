import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
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
    long_description=read('README.md'),
    # scripts=['bin/organize','bin/note'],

    entry_points = {
        'console_scripts': [
            'terminal-diary=terminal_diary.terminal_diary:main',
            'organize = terminal_diary.organize:main',
            'note = terminal_diary.note:main'
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
    ]
)


def user_prompt():
    f = raw_input("\n Please type in the path to the directory where you want to store your notes and press 'Enter': \n (Default: Desktop/terminal-notes) ")
    print f
    if f=="":
        f = "$HOME/Desktop/terminal-notes/"
    if not os.path.exists(f):
        os.system("mkdir {}".format(f))
    file = open('FILE_LOC', 'w')
    file.write(f)
    file.close()