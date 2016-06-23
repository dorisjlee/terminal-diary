# terminal-diary
terminal-diary is an easy-to-use, note-taking and diary app that lets you take notes in the terminal with your favorite text editor. It can render pdfs of your notes scattered across multiple days using [pandoc](http://pandoc.org/) (supports Markdown, LaTeX, HTML ..etc). It is written completely in Python, so that it is highly-customizable. Feel free to fork and customize your own settings. 
 
## Installation : 

- [Install pandoc](http://pandoc.org/installing.html) for compiling Markdown to PDF (Optional if you only want to use terminal-diary in plain text mode)

- Easiest way to install terminal-diary is through ``pip``: 

``pip install terminal-diary``

You can also build from source: 

```
git clone git@github.com:dorisjlee/terminal-diary.git
cd terminal-diary
python setup.py install
```

# Tutorial

 ``note`` 
- The ``note`` command lets you jot down notes. All the notes written on the same day gets stored in the same text file, but you specify keyword tags so that it is easier to organize them later.
		> ``note     <tag keyword>  ``

 ``organize``
- The ``organize`` command compiles all your note files from multiple days into relevant categories based on your keyword tag. There's two formatting modes:``diary`` (which contains timestamps of each record) and ``notes`` (no timestamps). While a markdown file of the notes is always generated with ``organize``, you can also optionally generate the pdf.
	>    ``organize     <tag keyword>   <format>  <pdf>``
    Ex) If I want all my physics notes in diary format (include time stamps) as a pdf
    >  	 ``organize physics diary pdf``
 - Sometimes I forget which keyword tags I used for a subject keyword (Was it ML or machine_learning or machine-learning?). You can use the ``iforgot`` command to print a list of all the keywords that you've ever used, so that they'll all get sorted together.


 - The ``syncup`` command allows you to generate the most up to date notes based on your diary files. This might take a while to run, but you get nice pretty pdf notes of everything afterwards.


 # Misc. 

I have tried using a lot of different note-taking software in the past, but there was always a couple things that I didn't like each one of them, features that one had, but not in the other (See [Wikipedia's comparison of notetaking software](https://en.wikipedia.org/wiki/Comparison_of_notetaking_software) ). So about half a year ago, I decided to build my own from scratch, so that I can just build the features that I wanted. Part of making this open source is so that there's a basic framework that you can hack around to build your own plug-in scripts for customizing your own functionalities. 
  
Another cool thing about terminal-notes is that it has enabled me to collect a fairly comprehensive, digital records of my research notes for text-mining purposes. Using very crude and basic natural language processing tricks and statistics, my next goal is to make periodic visualizations that can let me keep track of how my interest shifts in time, which would be kind cool to look at. (Here's a snippet of the preliminary Wordcloud example) I'm excited to see the potential application space from mining personal text corpus data collected by terminal-diary (sentiment analysis on your diary records?). 

