# Setting up now a terminal program to run and loop wordle_tool
import random

import tool_wordle as tw
import word_entropy as we

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
        possible = words

        # Initialise word data
        if not answer:
                answer = possible[random.randint(0,len(possible)-1)]

        # Begin while loop
        turn = 1
        while turn <= 6:

                print(tw.visualise(tw.pattern(guess,answer)) + " " + guess)

                # If loop - if win, end; else, continue
                if guess == answer:
                        print(f"I win! The word was '{answer}' and I guessed it in {turn} goes!")
                        break
                else:
                        # NEXT GUESS IS CHOSEN AS THE MAX ENTROPY WORD FROM REMAINING WORDS
                        possible = tw.possibilities(guess=guess,answer=answer,bank=possible)
                        guess = we.max_entropy(possible)
                        turn += 1

        # Loss statement
        if turn == 7:
                print("I lost...")

        # Output to save data
        return (guess,turn)

main('raise')