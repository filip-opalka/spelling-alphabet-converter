# Spelling Alphabet Converter
I had issues trying to spell words, so i created this script.
Input a word that you need to spell. You definitely need python installed: https://www.python.org/downloads/.

## How to create a easily runable file that starts the script.
This file can be doubleclicked to open, or you can put the code in the OS startup script.

### Windows:
Create a .bat file with the following content, fill in the location of the wordSpeller.py file
Example filename: wordSpeller.bat
```
@ECHO OFF
START "wordSpeller.py" "C:\Users\_username_\wordSpeller.py"
```

### Mac:
Create a .command file with the following content, fill in the location of the wordSpeller.py file
Example script filename: wordSpeller.command
```
python3 ./Desktop/Scripts/spelling-alphabet-converter.py
```

You need to change the permissions for the file, do it in the command line.
```
cd <file location>
chmod +x wordSpeller.command
```

## Examples:
Input:
Filip

Output:
Foxtrot India Lima India Papa


Input:
Github Repository

Output:
Golf India Tango Hotel Uniform Bravo <Space> Romeo Echo Papa Oscar Sierra India Tango Oscar Romeo Yankee


Input:
google.com
Output:
Golf Oscar Oscar Golf Lima Echo <Dot> Charlie Oscar Mike
