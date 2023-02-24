# Setting up now a terminal program to run and loop wordle_tool
import random

import tool_wordle as tw

# Fill a list up with our words with .txt file taken from source code
myfile = open("answer_list.txt","r")
content = myfile.read()
words = content.split("\n")
myfile.close()

# Main function to run through game, collect start word and final score
def main(guess,answer=''):
        # Initialise the lists of included/excluded letters
        include = []
        exclude = []
        known = {}
        rightWrong = {}
        possible = tw.possible()

        # Initialise word data
        if not answer:
                answer = possible[random.randint(0,len(possible)-1)]

        # Begin while loop
        turn = 1
        while turn <= 6:
                possible = tw.possibilities(guess=guess,answer=answer,bank=possible)

                # If loop - if win, end; else, continue
                if guess == answer:
                        break
                else:
                        # NEXT GUESS IS CHOSEN AT RANDOM FROM REMAINING WORDS
                        guess = possible[random.randint(0,len(possible)-1)]
                        turn += 1

        # Output to save data
        return (guess,turn)