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

stringToFix = str(sys.argv[1])
split = splitString(stringToFix)

def spellCheck(dictionary, words):
#given a list of words in a sentance and a dictionary of correcty spelled words
#output a list of words that are in the dictionary
	return list(set(dictionary) & set(words)
	correctWords = []
	for word in words:
		for thing in dictionary:
			if (word == thing):
				print words
				correctWords += word


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

dict = open("dictionary.txt")
wl = dict.readlines()
dict.close()

print fixSentance(stringToFix) 
