# Wordle-like Solver
A simple python-based GUI application that gives possible answers given a list of floating, fixed and wrong letters.

## Description
The solver takes in a set of floating (correct letter, unknown position) and fixed (correct letter, known position) letters and creates a list of possible words that fit that criteria. The program is customizable to allow any set of words of any length by setting up a word list file.

## Requirements
A relatively recent version of Python 3. (Download it here: https://www.python.org/downloads/)

## Usage
### Regarding the Word List

### [IMPORTANT] Word List Details
The current word list stored in words.txt only contains 5 letter words and are the words Wordle uses for its answers. Thus, when changing the number of letters to use, either supply your own word list, or utilize the generic english mode (which might take longer/use more memory).
### Using the Command Line Version
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
If you want to use a different word list (for example, a word list for French or Spanish), place the word list text file in this directory and use the -w flag.
```
python solver-cli.py -fl fl -fx ****k -w [filename].txt
```
### GUI Version [WIP]
The GUI version is currently under development

## Possible Issues
The GUI version was mostly made for Windows/Linux and thus might not be usable for Mac users. If so, please issue a bug report or use the command-line version.
## Credits
