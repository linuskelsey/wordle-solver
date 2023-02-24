# An effort to calculate the entropy for entering each word at any stage against the remaining words.

from math import log

import tool_wordle as tw

# Fill a list up with our words with .txt file taken from source code
myfile = open("answer_list.txt","r")
content = myfile.read()
words = content.split("\n")
myfile.close()

# Build a function returning entropy (with a given base) for a given probability-specified distribution
def H(dist,base):
	tot = 0
	for x in dist:
		if x != 0:
			A = x * log(x,base)
			tot -= A
	return tot

# Now we may define an entropy function for a given guess - first we give a function to return the probability distribution of possible patterns for such a guess with a given bank of possible words
def pattern_dist(guess,bank=words):
	dist = [0] * (3**5)
	l = len(bank)
	for word in bank:
		n = tw.enumerate(tw.pattern(guess,word))
		dist[n] += 1
	dist = [x/l for x in dist]
	return dist

# Finally we define an entropy function for words in our current answer list    (i.e. possible from tool_wordle.py)
def word_entropy(guess, bank=words):
	return H(pattern_dist(guess,bank),2)

# Now we design a function to determine the maximum entropy word from a given list
def max_entropy(bank=words):
	max_ent_word = bank[0]
	for word in bank:
		if word_entropy(word,bank) > word_entropy(max_ent_word,bank):
			max_ent_word = word
	return max_ent_word

# MAX ENTROPY WORD IS RAISE; BEST THREE WORD NON-OVERLAPPING COMBO             IS [RAISE,MULCH,DOWNY] (FOR QUORDLE).