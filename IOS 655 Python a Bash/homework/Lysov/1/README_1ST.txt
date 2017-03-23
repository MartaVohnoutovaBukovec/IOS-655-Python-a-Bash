Main application file is readbins.py

It will read decode and display informataion form the file containing binary strins.
Parameter -i followed by input file name is manadatory and will be enforced.
Parameter -s is optional and will enable speach to read decoded file back.
Additional libraries needed for this fearture are 'wave', 'pyaudio' and 'requests'
It is not required to istall them. Even if the option -s is passed the application
will disable this fearture if import fails and fall back to the default behavoir.
Additioanal classes 'playwave' and 'apitts' that support this fearture are in 
the separate files that will be loaded on request only.
'playwave' encupsulates functionality of .wav files playback
'apitts' provides text to speech conversion that results in creation of .wav files

The application has been tested on Windows 10 and Ubuntu for Windows.

There is also an additional small utility writebins.py that can read text files
and save binary strings encodings of this text to .bins files (which are also text files)
writebins.py takes only one file name and creates new file with the same name
by replacing extension to .bins

The original homework binary strings are in the file 'string-input.bins'

To run in windows from the directory of .py files:

python readbins.py -i string-input.bins -s # will read homework lines
python writebins.py poem.txt # will create poem.bins
python readbins.py -i poem.bins -s # will read back a poem

for Ubuntu from the directory of .py files:

python3 ./readbins.py -i string-input.bins -s # will display homework lines
python3 ./writebins.py poem.txt # will create poem.bins
python3 ./readbins.py -i poem.bins # will display a poem

Note: the -s option is not tested on Ubuntu, but it supposed to work
The negative testing was succesful: i.e. if libraries are missing the program
displays a custom message and continues to run with the basic functionality.



