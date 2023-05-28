# Problem Set 2, hangman.py
# Name: 
# Collaborators:
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
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word = list(secret_word)
    list1 = [i for i in secret_word if i in letters_guessed]
    if all(x in list1 for x in letters_guessed):
        return True
    else:
        return False
    
# secret_word = 'apple'
# letters_guessed = ['a', 'p', 'p', 'p', 'l', 'e']
# print(is_word_guessed(secret_word, letters_guessed))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word = list(secret_word)
    x = []
    for i in secret_word:
        x.append("_ ")
    for i in secret_word:
        if i in letters_guessed:
            x[secret_word.index(i)] = i
        #elif i not in letters_guessed:
            #x[secret_word.index(i)] = "_ "
    indices = [i for i, letter in enumerate(secret_word) if letter in letters_guessed]
    for index in indices:
        x[index] = secret_word[index]
    return ''.join(x)

# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_guessed_word(secret_word, letters_guessed) )



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    letters = list(string.ascii_lowercase)
    for i in letters:
        if i in letters_guessed:
            letters.remove(i)
    return ''.join(letters)

# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_available_letters(letters_guessed))

def unique_letters(word):
    lst = []
    for i in word:
        if i not in lst:
            lst.append(i)
    return ''.join(lst)
            
            
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #secret_word = "else"
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_guessed = []
    consonant_guessed = []
    import string
    letters = string.ascii_lowercase
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long..")
    guesses = 6
    warnings = 3
    print("You have 3 warnings left!")
    
    letters_guessed = []
    while  is_word_guessed(secret_word, letters_guessed) == True  or guesses > 0:
        print("-----------")
        print("You have", guesses, "guesses left!")
        print("Available letters:", get_available_letters(letters_guessed))
        
        guessed_letter = input("Please guess a letter: ").lower()
        if warnings == 0 and (guessed_letter not in letters or guessed_letter in letters_guessed)  :
            guesses -= 1
        if guessed_letter in letters_guessed:
            warnings -= 1
            print("Oops! You have already guessed that letter. You have", warnings, "warnings left..")
        if guessed_letter not in letters_guessed:
            letters_guessed.append(guessed_letter)
        
        if guessed_letter not in letters :
            warnings -= 1
            print("Oops! That is not a valid letter! You have", warnings, "warnings left: ", get_guessed_word(secret_word, letters_guessed))
        
        if guessed_letter in secret_word  :
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            #print("Available letters: ", get_available_letters(letters_guessed))
        elif guessed_letter not in secret_word and guessed_letter in letters :
            if guessed_letter not in vowels  :
                if guessed_letter in consonant_guessed :
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            #print("Available letters: ", get_available_letters(letters_guessed))
                elif guessed_letter not in consonant_guessed:
                    consonant_guessed.append(guessed_letter)
                    guesses -= 1
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            if guessed_letter in vowels:
                if guessed_letter in vowel_guessed:
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                elif guessed_letter not in vowel_guessed:
                    vowel_guessed.append(guessed_letter)
                    guesses -= 2
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
        total_score = guesses * len(unique_letters(secret_word))
        if get_guessed_word(secret_word, letters_guessed) == secret_word :
            print("Congratulations, you won!")
            print("Your total score for this game is:", total_score)
            break
        if guesses == 0:
            print("Sorry, you ran out of guesses.. The word was", secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_stripped = my_word.replace(" ", "")
    letters = list(my_word_stripped)
    if len(other_word) == len(my_word_stripped):
        for i in range(len(my_word_stripped)):
            if my_word_stripped[i] == other_word[i]:
                continue
            elif my_word_stripped[i] == "_" and other_word[i] not in letters:
                continue
            else:
                return False
        return True
    else:
        return False

# print(match_with_gaps("te_ t", "tact"))
# print(match_with_gaps("a_ _ le", "banana"))
# print(match_with_gaps("a_ _ le", "apple"))
# print(match_with_gaps("a_ ple", "apple"))
#

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            possible_matches.append(other_word)
        else:
            continue
    if possible_matches == []:
        print("No matches found")
    else:
        return " ".join(possible_matches)
    
# print(show_possible_matches("t_ _ t"))
# print(show_possible_matches("abbbb_ "))
# print(show_possible_matches("a_ pl_ "))
            



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # secret_word = "apple"
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_guessed = []
    consonant_guessed = []
    import string
    letters = string.ascii_lowercase 
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long..")
    guesses = 6
    warnings = 3
    print("You have 3 warnings left!")
    
    letters_guessed = []
    while  is_word_guessed(secret_word, letters_guessed) == True  or guesses > 0:
        print("-----------")
        print("You have", guesses, "guesses left!")
        print("Available letters:", get_available_letters(letters_guessed))
        
        guessed_letter = input("Please guess a letter: ").lower()
        if warnings == 0 and (guessed_letter not in letters or guessed_letter in letters_guessed)  :
            guesses -= 1
        if guessed_letter in letters_guessed:
            warnings -= 1
            print("Oops! You have already guessed that letter. You have", warnings, "warnings left..")
        if guessed_letter not in letters_guessed:
            letters_guessed.append(guessed_letter)
        if guessed_letter == '*':
            print("Possible word matches are: ")
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            
        if guessed_letter not in letters and guessed_letter != "*":
            warnings -= 1
            print("Oops! That is not a valid letter! You have", warnings, "warnings left: ", get_guessed_word(secret_word, letters_guessed))
        
        if guessed_letter in secret_word  :
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            #print("Available letters: ", get_available_letters(letters_guessed))
        elif guessed_letter not in secret_word and guessed_letter in letters :
            if guessed_letter not in vowels  :
                if guessed_letter in consonant_guessed :
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            #print("Available letters: ", get_available_letters(letters_guessed))
                elif guessed_letter not in consonant_guessed:
                    consonant_guessed.append(guessed_letter)
                    guesses -= 1
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            if guessed_letter in vowels:
                if guessed_letter in vowel_guessed:
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                elif guessed_letter not in vowel_guessed:
                    vowel_guessed.append(guessed_letter)
                    guesses -= 2
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
        total_score = guesses * len(unique_letters(secret_word))
        if get_guessed_word(secret_word, letters_guessed) == secret_word :
            print("Congratulations, you won!")
            print("Your total score for this game is:", total_score)
            break
        if guesses == 0:
            print("Sorry, you ran out of guesses.. The word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
