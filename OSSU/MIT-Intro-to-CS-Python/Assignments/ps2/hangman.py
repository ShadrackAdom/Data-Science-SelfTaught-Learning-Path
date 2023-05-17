# Problem Set 2, hangman.py
# Name: Shadrack Adom
# Collaborators: N/A
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
letters_guessed = []


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    #print(random.choice(wordlist))
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
   
    win = True
    for letter in secret_word:
        if letter not in letters_guessed:
            win = False
    return win

#print(is_word_guessed('apple', ['w','a', 'q', 'p','e', 'i', 'l', 'k', 'p', 'r', 's']))
                                
                              

def get_guessed_word(secret_word, letters_guessed):
    
    guessed_word = []

    for letter in secret_word:
        if letter not in letters_guessed:
            guessed_word.append('_ ')
        else:
            guessed_word.append(letter)
    
    return ''.join(guessed_word)
          
    
#print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))




def get_available_letters(letters_guessed):

    # have a copy of ascii in lowercases 
    cp_ascii = list(string.ascii_lowercase)
    #go through loop and check 
    for letter in cp_ascii:
        #if letter in guessed remove from copied ascii array
        if letter in letters_guessed:
            cp_ascii.remove(letter)
    
    #return ascii copied array 
    return ''.join(cp_ascii)

#print(get_available_letters(['e', 'i', 'k', 'p', 'r', 's']))
    
    

def hangman(secret_word):
    
    current_guess = " "
    guesses_left = 6
    letters_guessed
    warnings = 3

    #Welcome message
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letter long")
    print(f"You have {warnings} warning(s) left")
    print("------------")

    #Interactive message
    while not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        current_guess = input("plesae guess a letter:")

    #check if user entered incorrect char
        if current_guess not in string.ascii_letters:
            if warnings > 0:
                warnings -= 1
                print("Oops! that's not a valid letter. You have {warnings} warnings left ")
                print("---------")
            else:
                guesses_left -= 1
                warnings= 0
                print(f"Oops! You have already guessed that letter. You have {warnings} lefts so you lose one guess {get_guessed_word(secret_word, letters_guessed)})")
            
        elif current_guess in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print(f"Oops! you have already guessed that letter. you have {warnings} warning left")
                print("-----------")
            else:
                guesses_left -= 1
                warnings = 0 
                print(f"Oops! You have already guessed that letter. You have {warnings} lefts so you lose one guess {get_guessed_word(secret_word, letters_guessed)})")
                print("---------")
        else:
            letters_guessed.append(current_guess)

            if current_guess in secret_word:
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
                print("------------")
            else:
                print(f"Oops that letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                guesses_left -=1
                print("-----------")

    if guesses_left == 0:
        print(f"Sorry you run of guesses, the word was {secret_word}")   
    else:
        print("Congrats you won!")      
        print(f"Your total score for this gmae is: {guesses_left * len(set(secret_word)) }")


def match_with_gaps(my_word, other_word):

    my_word_list = list(my_word)
    other_word_list = list(other_word)
    for char in my_word_list[:]:
        if char == " ":
            my_word_list.remove(char)
    
    match = True
    if len(my_word_list) != len(other_word_list):
        match = False
    else:
        for char_index in range(len(my_word_list)):
            if my_word_list[char_index] != "_":
                if my_word_list[char_index] != other_word_list[char_index]:
                    match = False
            else:
                if other_word_list[char_index] in my_word_list:
                    match = False
    return match


#print(match_with_gaps("a_ _ple", "apple"))
                
    



def show_possible_matches(my_word):
    matches = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            matches.append(other_word)
    if len(matches) == 0:
        print("No matches found.")
    return ' '.join(matches)
    
#print(show_possible_matches("a_ _le"))


def hangman_with_hints(secret_word):
    current_guess = " "
    guesses_left = 6
    letters_guessed
    warnings = 3

    #Welcome message
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letter long")
    print(f"You have {warnings} warning(s) left")
    print("------------")

    #Interactive message
    while not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        current_guess = input("plesae guess a letter:")

        if current_guess == "*":
            print("Possible word matches are:")
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            print("----------")

    #check if user entered incorrect char
        if current_guess not in string.ascii_letters and current_guess != "*":
            if warnings > 0:
                warnings -= 1
                print("Oops! that's not a valid letter. You have {warnings} warnings left ")
                print("---------")
            else:
                guesses_left -= 1
                warnings= 0
                print(f"Oops! You have already guessed that letter. You have {warnings} lefts so you lose one guess {get_guessed_word(secret_word, letters_guessed)})")
            
        elif current_guess in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print(f"Oops! you have already guessed that letter. you have {warnings} warning left")
                print("-----------")
            else:
                guesses_left -= 1
                warnings = 0 
                print(f"Oops! You have already guessed that letter. You have {warnings} lefts so you lose one guess {get_guessed_word(secret_word, letters_guessed)})")
                print("---------")
        elif current_guess != "*":
            letters_guessed.append(current_guess)

            if current_guess in secret_word:
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
                print("------------")
            else:
                print(f"Oops that letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                guesses_left -=1
                print("-----------")

    if guesses_left == 0:
        print(f"Sorry you run of guesses, the word was {secret_word}")   
    else:
        print("Congrats you won!")      
        print(f"Your total score for this gmae is: {guesses_left * len(set(secret_word)) }")




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

    pass
