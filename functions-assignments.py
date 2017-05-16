import sys

def fixSentance(aString):
	strings = aString.split('.')
	for temp in strings:
		if temp:
			temp = temp.replace('_',' ').strip().lower().capitalize()
			print temp.split(' ')
			#temp = temp.split(' ')
		try:
			if ((temp[-1] != '.') & (temp[-1] != '!') & (temp[-1] != '?')):
				temp = temp + '.'
			print temp
		except IndexError:
			print "Caught index error"

def spellCheck(dictionary, words):
#given a list of words in a sentance and a dictionary of correcty spelled words
#output a list of words that are in the dictionary
	#return list(set(dictionary) & set(words)
	correctWords = []
	print "Got to spell check"
	for word in words:
		#print word
		for thing in dictionary:
			#print word
			#print thing
			#print type(word)
			#print type(thing)
			if ((word == thing) & (word != " ") & (word != "")):
				print word
				#print thing
				correctWords += word
	print "Leaving spellcheck"

def splitString(str):
	str = str.split(' ')
	str = ' '.join(str)
	str = str.split('.')
	str = ' '.join(str)
	str = str.split('?')
	str = ' '.join(str)
	str = str.split(',')
	str = ' '.join(str)
	str = str.split('!')
	str = ' '.join(str)
	words = str.split(' ')
	print words 
	return words

stringToFix = str(sys.argv[1])
split = splitString(stringToFix) 

dict = open("dictionary.txt")
wl = dict.readlines()
dict.close()

wordList = []
for word in wl:
	wordList.append(word.strip())


spellCheck(wordList, split)

print fixSentance(stringToFix) 
