import random_wordle_bot_muted as rndbot
import letter_freq_wordle_bot_muted as freqbot
import entropy_wordle_bot_muted as entbot

# Total games played
def tot(dist):
	tot = 0
	for i in range(6):
		tot += dist[i]
	return tot

# Number of losses, stored in tuple
def losses(word):
	return word[6]

# Percentage of wins using a given start word
def win_percentage(word):
	return round(100*(tot(word)-losses(word)) / tot(word), 4)

# Probability (estimator) of each score starting from a given word
def prob(word, i):
	return round(word[i]/tot(word), 4)

# Average score from starting with a given word
def avg(word):
	Avg = 0
	for i in range(6):
		weighted_i = (i+1) * word[i]
		Avg += weighted_i
	if tot(word) == 0:
		avg = 7
	else:
		avg = round(Avg / tot(word), 4)
	return avg

# Probability distribution (estimator) for a given start word
def distn(word):
	return [prob(word, i) for i in range(6)]



# Summary of starting with a given word
def summarise(word):
	print(f" -- Starting Word: {word[7].upper()} -- ")
	print(f"Games Played: {tot(word)}")
	print(f"Win Percentage: {win_percentage(word)}%")
	print(f"Average Score: {avg(word)}")
	print(f"Score Distribution: {distn(word)}")
	print()

# Full run and compilation of data from rndbot.main() -- AVG SCORE ~ 4.74
def randomDist(word, n):
        scores = []
        summaryList = [0,0,0,0,0,0,0,word]
        for i in range(0,n):
                scores.append(rndbot.main(word)[1])
                print(f"{(100*(i+1))/n}%")
        for score in scores:
                for i in range(0,7):
                        if score == i:
                                summaryList[i] += 1
        return summaryList

# O(n) time function to run full analysis on all possible start guesses with rndbot.main() to see which gives highest average score -- extremely expensive time-wise to give a representative sample.
def avgDictRandom(n):
	myfile = open("answer_list.txt","r")
	content = myfile.read()
	words = content.split("\n")
	myfile.close()
	avgDict = {}
	for word in words:
		avgDict[word] = avg(randomDist(word,n))
		print(f"{(100*(words.index(word)+1))/2315}%")
	avgDict = list(dict(sorted(avgDict.items(), key=lambda item: item[1])).items())[:50]
	return avgDict

# Full run and compilation of data from freqbot.main() -- AVG SCORE ~ 4.63
def freqDist(word,n):
        scores = []
        summaryList = [0,0,0,0,0,0,0,word]
        for i in range(0,n):
                scores.append(freqbot.main(word)[1])
                print(f"{(100*(i+1))/n}%")
        for score in scores:
                for i in range(0,7):
                        if score == i:
                                summaryList[i] += 1
        return summaryList

# Similar to avgDictRandom, quite a bit slower than rndbot.main(), not sure of O() runtime.
def avgDictFreq(n):
	myfile = open("answer_list.txt","r")
	content = myfile.read()
	words = content.split("\n")
	myfile.close()
	avgDict = {}
	for word in words:
		avgDict[word] = avg(freqDist(word,n))
		print(f"{(100*(words.index(word)+1))/2315}%")
	avgDict = list(dict(sorted(avgDict.items(), key=lambda item: item[1])).items())[:50]
	return avgDict

# Full run and compilation of data from entbot.main() -- AVG SCORE ~ 4.53
def entDist(word,n):
        scores = []
        summaryList = [0,0,0,0,0,0,0,word]
        for i in range(0,n):
        	scores.append(entbot.main(word)[1])
        	print(f"{(100*(i+1))/n}%")
        for score in scores:
                for i in range(0,7):
                        if score == i:
                                summaryList[i] += 1
        return summaryList

# Similar to avgDictFreq, similar runtimes, ~70s for 1000 iter's
def avgDictEnt(n):
	myfile = open("answer_list.txt","r")
	content = myfile.read()
	words = content.split("\n")
	myfile.close()
	avgDict = {}
	for word in words:
		avgDict[word] = avg(entDist(word,n))
		print(f"{(100*(words.index(word)+1))/2315}%")
	avgDict = list(dict(sorted(avgDict.items(), key=lambda item: item[1])).items())[:50]
	return avgDict