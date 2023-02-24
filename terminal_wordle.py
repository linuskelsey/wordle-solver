# Setting up now a terminal program to run and loop wordle_tool
import tool_wordle as tw
import word_entropy as we

# Fill a list up with our words with .txt file taken from source code
myfile = open("answer_list.txt","r")
content = myfile.read()
words = content.split("\n")
myfile.close()

# Functions for different letter classes
def ask_include(include):
        # Ask about letters in the word
        message = input("\n\nDo you know any of the letters in the word? (y/n) ")
        if message.lower() == 'y':
                # Begin to fill up include
                letter = input("\nTell me one of the letters you know: ")
                while letter.lower() and len(letter) == 1:
                        include.append(letter.lower())
                        letter = input("Tell me another letter you know: ")
        return include

def ask_known(known, include):
        # Set up option to fill up known
        knownBool = input("\nOf the letters you know, do you know where any of them go? (y/n) ")
        if knownBool.lower() == 'y':
                letter = input("\nTell me which letter you know the position of: ").lower()
                while letter in include:
                        position = int(input(f"And which position does {letter} go? (number) ")) - 1
                        known[position] = letter
                        letter = input("\nTell me another letter you know the position of: ").lower()
        return known

def ask_rightWrong(rightWrong, include):
        answer = input("\nOf the letters you know, are there any you know can't be in a certain place? (y/n) ")
        if answer.lower() == 'y':
                letter = input("\nTell me one this is the case for: ").lower()
                while letter in include:
                        wrongPos = int(input(f"And which position can {letter} not be in? (number) ")) - 1
                        rightWrong[wrongPos] = letter
                        letter = input("\nTell me another for which this is the case: ").lower()
        return rightWrong

def ask_exclude(exclude, include):
        # Ask about letters NOT in word
        answer = input("\nDo you know any letters we should exclude? (y/n) ")
        if answer.lower() == 'y':
                letter = input("\nTell me one of the letters not in the word: ")

                # Begin to fill up the exclude list
                while letter.lower() and len(letter) == 1:
                        if letter.lower() not in include:
                                exclude.append(letter.lower())
                                letter = input("Tell me another of the letters not in the word: ")
                        else:
                                letter = input("Tell me another of the letters not in the word: ")
        print()
        return exclude

# Welcome messages
print("\nHi! Welcome to Linus and Matilda's complete Wordle Tool!")
print("\nYou tell us which letters you can and can't use in your Wordle, and we'll tell you which words are still possible :)")
print("\nTo move onto a new question at any point, press enter without typing.")

word = input("\nWhat is your starting word? ").lower()

# Function to run through terminal program, collect start word and final score
def score(word):
        # Initialise the lists of included/excluded letters
        include = []
        exclude = []
        known = {}
        rightWrong = {}
        possible = tw.possible()

        # Begin while loop
        guess = 1
        while guess <= 6:
                # Let user know which guess they are on
                print(f"\n\n --- Guess number {str(int(guess)+1)}! --- ")

                # Ask about known letters
                include = ask_include(include)

                # Set up option to fill up known
                known = ask_known(known, include)

                # Set up option to tell where letters aren't
                rightWrong = ask_rightWrong(rightWrong, include)

                # Ask about letters NOT in word
                exclude = ask_exclude(exclude, include)

                possible = tw.possible(bank=possible, include=include, known=known, exclude=exclude, rightWrong=rightWrong)

                print(f"\n\nThe list of possible words is {possible}.")
                print(f"\nThe word with maximal entropy is '{we.max_entropy(possible)}'.")

                answer = input("\n\nDo you know which word it is yet? (y/n) ")
                if answer.lower() == 'y':
                        final = input("\nWhat was the final word? ").lower()
                        while final not in possible:
                                final = input("That's not possible! Which word was it actually? ")
                        score = input("How many guesses did it take? ")
                        print("\nCongratulations!!\n")
                        guess = 7

                guess += 1

        return (final, score)

score(word)