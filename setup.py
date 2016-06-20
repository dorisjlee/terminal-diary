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
        'numpy>=1.10.1',
        'pandas>=0.17.1'
    ]
)
