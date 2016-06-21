# terminal-diary
terminal-diary is an easy-to-use, highly-customizable note-taking and diary Python app that lets you take notes in the terminal with your favorite note-taking app.

#Cool Functions:
- ``note`` : lets you jot down Markdown notes with tags.

## Decision Trees:
- choose best split to minimize weighted average: 
$$H_{after} = \frac{|S_l| H(S_l) + |S_r| H(S_r)}{|S_l| + |S_r|}$$
where H = entropy = $\sum_C p_C log_2 p_C$ where pc = probability in class C

Second law of thermodynamics: total entropy(S) of an isolated system always increases over time 
$S = klnW$ where W is microstates
$$dS = {\deltaQ}{T}$$

note viz
## Ch 9 : In situ processing 

- rather than writing to disk then post-process viz
    - since IO so much slower than computing these days, in-situ processing is a good way to figure out what is the interesting stuff to store 
    - two types : 
        - _coprocessing_: viz code built into simulation code 
        - _concurrent processing_: viz separate from code, external viz (like VisIT) 
    - ideally you want to leverage hybrid of the two because external viz is better (prettier plots, more functions) but coprocessing uses simultion memory directly 

- Materialized view: a replica of the master data from a single point in time
   - putting materialized view in a distributed fashion across many servers eases network load (not all read/write on master server) since everyone has a copy

HCI 

## Parametric analysis : 
- t-test :test whether two different conditions had effect on perfomrance data (i.e. whether two sets of data are significantly different from each other)  
- _one-way_: is the data better or worse for this condition? 
- _two-way_: any difference is detected (usually use this to be safe) 
- repeated measures t-test just tabulates a bunch of statistics from the data for each participant for each condition that the participant experieneces 
    - the t-value is obtained by referencing a statistics table which gives you the functional value of the t-distribution 

<demo text>
- ``organize`` comm

Markdown (LaTeX) or you could just use it in plain text mode
compiles with diary mode

## Installation : 
- ``pip install terminal-diary``
- (Install pandoc)[http://pandoc.org/installing.html] for compiling Markdown to PDF
- Numpy
- Pandas
