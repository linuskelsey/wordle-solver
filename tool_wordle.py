# Fill a list up with our words with .txt file taken from source code
myfile = open("answer_list.txt","r")
content = myfile.read()
words = content.split("\n")
myfile.close()

# Functions for different letter classes
def ask_include(guess,answer):
        include = []
        for i in range(0,5):
                if guess[i] in answer:
                        include.append(guess[i])
        return include

def ask_known(guess,answer):
        known = {}
        for i in range(0,5):
                if guess[i] == answer[i]:
                        known[i] = guess[i]
        return known

def ask_rightWrong(guess,answer):
        rightWrong = {}
        for i in range(0,5):
                if guess[i] in answer and guess[i] != answer[i]:
                        rightWrong[i] = guess[i]
        return rightWrong

def ask_exclude(guess, answer):
        exclude = []
        for i in range(0,5):
                if guess[i] not in answer:
                        exclude.append(guess[i])
        return exclude

# Function to include words not containing certain letters
def excludeFunc(letter, words):
        excludeWords = []
        for word in words:
                if letter not in word:
                        excludeWords.append(word)
        return excludeWords

# Function to include words containing certain letters
def includeFunc(letter, words):
        includeWords = []
        for word in words:
                if letter in word:
                        includeWords.append(word)
        return includeWords

# Function to include words with letters in the right places
def knownFunc(key, value, words):
        knownWords = []
        for word in words:
                if word[key] == value:
                        knownWords.append(word)
        return knownWords

# Function to exclude words with right letter in wrong place
def rightWrongFunc(key, value, words):
        rightWrongWords = []
        for word in words:
                if value in word and word[key] != value:
                        rightWrongWords.append(word)
        return rightWrongWords

# Compilation of the three
def possible(bank=words, exclude=[], include=[], known={}, rightWrong={}):
        wordl = bank

        for letter in exclude:
                wordl = excludeFunc(letter, wordl)

        for letter in include:
                wordl = includeFunc(letter, wordl)

        for key, value in known.items():
                wordl = knownFunc(key, value, wordl)

        for key, value in rightWrong.items():
                wordl = rightWrongFunc(key, value, wordl)

        return wordl

def possibilities(guess,answer,bank=words):
        # Ask about known letters
        include = ask_include(guess,answer)
        # Set up option to fill up known
        known = ask_known(guess,answer)
        # Set up option to tell where letters aren't
        rightWrong = ask_rightWrong(guess,answer)
        # Ask about letters NOT in word
        exclude = ask_exclude(guess,answer)

        return possible(bank, include=include, known=known, exclude=exclude, rightWrong=rightWrong)

# Function to output the pattern given (as a ternary number in string form) shown for a guess against a given answer
def pattern(guess,answer):
        if len(guess) != len(answer):
                print("Incompatible words, please try again.")
        else:
                n = len(guess)
                pattern = [0] * n
                answer_list = []

                # Fill list with letters of answer
                for i in range(n):
                        answer_list.append(answer[i])

                # Enter a '2' (green) where letters line up
                for i in range(n):
                        if answer[i] == guess[i]:
                                pattern[i] = 2
                                answer_list.remove(guess[i])

                # Enter a '1' (yellow) where letters in wrong place w/o double count
                for i in range(n):
                        if answer[i] != guess[i] and guess[i] in answer_list:
                                pattern[i] = 1
                                answer_list.remove(guess[i])

                pattern = [str(x) for x in pattern]

                return "".join(pattern)

# Function to decimally enumerate the different patterns
def enumerate(pattern):
        n = len(pattern)
        num = 0
        for i in range(n):
                num += int(pattern[n-i-1]) * (3**i)
        return num

# Function to visually represent the different patterns
def visualise(pattern):
        rep = ""
        for x in pattern:
                if int(x) == 2:
                        rep += '🟩'
                elif int(x) == 1:
                        rep += '🟨'
                elif int(x) == 0:
                        rep += '⬛️'
        return rep