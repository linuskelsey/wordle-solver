# Fill a list up with our words with .txt file taken from source code
myfile = open("answer_list.txt","r")
content = myfile.read()
words = content.split("\n")
myfile.close()

# Ordered list of letters in English language according to frequency
letterFreqSort = ['e','t','a','o','i','n','s','r','h','l','d','c','u','m','f','p','g','w','y','b','v','k','x','j','q','z']

# Function to assign a score to each word based on frequency of letters in word
def freqScore(word):
	score = 0
	for letter in word:
		for i in range(0,26):
			if letterFreqSort[i] == letter:
				score += 26-i
	return score

# Function to find the maximum freqScore() from a list of words
def maxFreq(words):
	scores = []
	for word in words:
		if freqScore(word) not in scores:
			scores.append(freqScore(word))
	return max(scores)

# Function to produce a sub-list of maximum freqScore()
def maxFreqList(words):
	maxList = []
	n = maxFreq(words)
	for word in words:
		if freqScore(word) == n:
			maxList.append(word)
	return maxList