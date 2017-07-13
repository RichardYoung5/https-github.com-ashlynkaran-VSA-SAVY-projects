# Name:Richard Young    Blake Thompson
# Date:7-13-17



# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!


X = choose_word(wordlist)
#return random.choice(X)
list1 = []
list2 = []
underscore = "_"
counter = 0
for letter in X:
    list1.append(letter)
    list2.append(underscore)
loop_control = True

while counter <= 11:
    A = raw_input("Please guess a letter , if you do not wish to continue enter quit ")
    if A in list1:
        counter2 = 0
        print(A) "is in the word!"
        for letter in list1:
            if letter == A:
                list2[counter2]= A
            counter2 = counter2 + 1


    counter = counter + 1
    print list2
raw_input()
