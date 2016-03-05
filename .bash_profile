export SPARK_HOME=/Users/dorislee/Desktop/BioVis/spark-1.5.2-bin-hadoop2.4/
#.bash profile for local (Macbook) 
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced

export PATH=/usr/local/bin:$PATH
export PATH=/usr/local/mysql/bin:$PATH

PATH=$PATH:$HOME/Montage_v3.3/bin:$HOME/Desktop/StarFormation/ramses/trunk/ramses/bin:$HOME/Desktop/Princeton_USRP/athena4.2/bin:$HOME/Desktop/Princeton_USRP/athena4.2/
source  /usr/local/scisoft/bin/Setup.bash
# Enabling virtualenvwrapper at startup
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper_lazy.sh
# HackLife Scripts
hack_path="/Users/dorislee/Desktop/PersonalProj/hack-life/scripts/"
#add [%an] for printing also the name of the person who did the commit (removed because mostly work on my own repo anyways)
alias hacklife='cd /Users/dorislee/Desktop/PersonalProj/hack-life/scripts/'
alias startup='python $hack_path/startup.py &'
alias podomoro='python $hack_path/timer.py 30 &'
# Diary Scripts
diary_path='/Users/dorislee/Desktop/PersonalProj/diary.noindex/'
alias diary='python $diary_path/diary.py new '
# Research Diary Scripts
research_notes_path='/Users/dorislee/Desktop/PersonalProj/research_diary'
alias note='python $research_notes_path/research_diary.py new'
#alias organize='python $research_notes_path/organize.py'
alias organize='function _organize(){ python $research_notes_path/organize.py  $1 $2 $3 ;};_organize'
alias bsh='vim ~/.bash_profile;source ~/.bash_profile'
alias lsd='ls -F|grep /'
alias ls='ls -GFh'
alias ..='cd ..'
alias l='ls'
alias rc3='cd /Users/dorislee/Desktop/GSoC2014/workarea-rc3-project/pipeline'
#Git Alias
alias website_update='cd PersonalProj/mygithubpage/;git add . ; git commit -m "update"; git push'
alias glog="git log --pretty=format:'%h %ad | %s%d ' --graph --date=short --since='31 days ago'"
alias gs='git status '
alias ga='git add .'
alias gb='git branch '
alias gc='git commit -m'
alias gd='git diff'
alias push='git push'
alias pull='git pull'
alias go='git checkout '
#Remote Machines
#-A enable forwarding of ssh keys to remote machine if the ssh keys are copied over to .ssh/
alias hopper='ssh -A -Y hopper.nersc.gov'
alias edison='ssh -A -Y edison.nersc.gov'
alias cori='ssh -A -Y cori.nersc.gov'
alias carver='ssh -A -Y carver.nersc.gov'
alias ay='ssh dlee@ugastro.berkeley.edu'
alias boss='ssh -Y dorislee@riemann.lbl.gov'
alias cct='ssh  doris@192.168.169.13'
alias amazon='cd Desktop;ssh -i rc3.pem ec2-user@54.191.66.196'
alias bigdog='ssh doris@bigdog.astro.illinois.edu'
alias charon='ssh -X -Y dorislee@charon.astro.princeton.edu'
alias p2='workon py27dev'
alias p3='workon py34dev'
alias pb='ipython notebook'
#Mounting virtual disk remotely onto NERSC machines 
alias mount_proj="mkdir projects;sshfs dorislee@cori.nersc.gov:/project/projectdirs/astro250/doris  projects -o auto_cache,defer_permissions,noappledouble"
alias unmount_proj="diskutil unmount force projects/;rm -r projects/"
alias sf="mkdir projects;sshfs dorislee@cori.nersc.gov:/project/projectdirs/astro250/doris/ projects -o auto_cache,defer_permissions,noappledouble;cd projects/ ;p2;pb"

# added by Anaconda3 2.4.1 installer
export PATH="/Users/dorislee/anaconda/bin:$PATH"
