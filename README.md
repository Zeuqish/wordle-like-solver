# Wordle-like Solver
A simple python-based GUI application that gives possible answers given a list of floating, fixed and wrong letters.

## Description
The solver takes in a set of floating (correct letter, unknown position) and fixed (correct letter, known position) letters and creates a list of possible words that fit that criteria. The program is customizable to allow any set of words of any length by setting up a word list file.

## Requirements
A recent version of Python 3 (Download it here: https://www.python.org/downloads/). Make sure to install Tkinter during installation if you want to use the GUI version.
## Usage
### Regarding the Word List

#### [IMPORTANT] Word List Details
The current word list stored in words.txt only contains 5 letter words and are only the answers used in Wordle. If you prefer to have something harder, rename the words_all.txt file to words.txt and the program will utilize all known 5 letter english words.

#### Changing the Word List to Other Words
The program is capable enough to use wordlists with lengths not equal to 5. Merely store your wordlist to a words.txt file and save it to the directory where solver-gui.py or solver-cli.py is stored. Always remember to properly format your floating and fixed letters (e.g. if you have six letters, you should have floating letters of at most 6, and fixed letters should be of the format ******).

Note that the program does not support variable-length wordlists, and unknown compatibility for words with non-ASCII letters.

### Using the GUI Version
This version is straightforward. Input your details on the left, and the words should come out at the right. Adding banned letters *can* slow down the program, so be wary of using a lot of banned letters in a slower computer.

### Using the Command Line Version [NOT RECOMMENDED]
Please note that you will have to re-run the command-line version every time you want to use it.

The program should run with the following commands:
```
python solver-cli.py [flags] [arguments]
```
The flags and arguments are as follows:
```
solver-cli.py [-h] [-fl FLOAT] [-fx FIXED] [-o] [-n NUMBER] [-w WORDLIST]

options:
  -h, --help            show this help message and exit
  -fl FLOAT, --float FLOAT
                        Add FLOAT letters to check. Format: xxxxx, where x is a floating letter. Example: abc means a,b,c are floating.      
  -fx FIXED, --fixed FIXED
                        Add FIXED letters to check. Format: x*x*x, where asterisks are unknown letters. Example: **c** means c is fixed in   
                        the third position.
  -o, --output          Creates an output text file (called answers.txt) containing all possible answers. Prevents output from appearing in  
                        terminal.
  -n NUMBER, --number NUMBER
                        [Optional] Set the number of letters to check. Default is 5.
  -w WORDLIST, --wordlist WORDLIST
                        [Optional] Change the wordlist file.

```
An example input where the letters f and l are floating and k is fixed in the last position would be
```
python solver-cli.py -fl fl -fx ****k
```
If you want output to be stored in a text file, only know floating letters (q and u) and want to check only 4 letter words:
```
python solver-cli.py -fl qu -n 4
```
If you want to use a different word list, place the word list text file in this directory and use the -w flag.
```
python solver-cli.py -fl fl -fx ****k -w [filename].txt
```

## Possible Issues
The GUI version was mostly made for Windows/Linux and thus might not be usable for Mac users. If so, please issue a bug report or use the command-line version.

## Bugs
If there are any bugs, please file an issue so that it can easily be found.

## Credits
The words_all.txt word list was adapted from https://github.com/dwyl/english-words, and the Wordle answers were adapted from the Wordle source code. All copyrights belong to their owners.
