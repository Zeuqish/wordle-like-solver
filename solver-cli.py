
def solve(floating, fixed, dir):
    import re
    word_list = []
    with open(dir, 'r') as final_word_list:
        word_list = final_word_list.readlines()
    
    #First do the fixed letters. If fixed is empty, we do nothing and proceed to floating.
    if fixed:
        fixed = fixed.replace("*",".")
        pattern = re.compile(fixed)
        word_list = list(filter(pattern.match,word_list))
    
    #From word_list, we now have to make sure that ALL our floating characters exist for each word. Current implementation means keeping only words with a specific letter
    #in a loop.
    if floating:
        for character in floating:
            pattern = re.compile(character)
            word_list = list(filter(pattern.search,word_list))

    return word_list

if __name__ == "__main__":
    import argparse, sys

    NUM_LETTERS = 5
    WORDLIST_DIR = "words.txt"
    parser = argparse.ArgumentParser()

    parser.add_argument("-b","--ban", default="", help="Add BAN letters to remove from checking. Format: xxxxxxxxx..., where x is any letter.")

    parser.add_argument("-fl","--float", default="", help="Add FLOAT letters to check. Format: xxxxx, where x is a floating letter. Example: abc means a,b,c are floating.")
    parser.add_argument("-fx","--fixed", default="", help="Add FIXED letters to check. Format: x*x*x, where asterisks are unknown letters. Example: **c** means c is fixed in the third position.")
    parser.add_argument("-o", "--output", action='store_true' ,help="Creates an output text file (called answers.txt) containing all possible answers. Prevents output from appearing in terminal.")
    
    parser.add_argument("-n","--number", default=5, type=int, help="Set the number of letters to check. Default is 5.")
    parser.add_argument("-w","--wordlist", default=WORDLIST_DIR, help="Change the wordlist file.")
    #test_args(parser)
    arguments = parser.parse_args(sys.argv[1:])

    print(arguments)

    #Set Default Values
    NUM_LETTERS = arguments.number
    WORDLIST_DIR = arguments.wordlist

    #Check if letters are properly set up, i.e. there is at least one letter to match.
    try:
        assert(arguments.float != "" or arguments.fixed != "")
    except AssertionError:
        print("No letters to match found. Please put in at least one floating or fixed letter.")
        exit()

    #Check inputs letters for validity
    try:
        assert(len(arguments.float) <= NUM_LETTERS and len(arguments.fixed) <= NUM_LETTERS)
    except AssertionError:
        print('Invalid number of letters. You put in', len(arguments.float), 'floating letters and', len(arguments.fixed), 'fixed letters when there should be at most', NUM_LETTERS, "for either", end=".\n")
        exit()

    #Finally, check fixed letters for proper formatting.
    try:
        assert('*' in arguments.fixed or arguments.fixed == '')
    except AssertionError:
        print("There weren't any asterisks found in the fixed letters. Please see the README for proper usage.")
        exit()

    #And now, we solve.
    answers = solve(arguments.float, arguments.fixed, WORDLIST_DIR)

    #Print output depending on flags
    if not arguments.output:
        for answer in answers:
            print(answer,end='')
    else:
        with open('answers.txt', 'w') as answer_list:
            for answer in answers:
                answer_list.write(answer)
