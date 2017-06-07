import sys
import re

def fixSentance(aString):
#Makes many differnt gramatical error present in strings that are imputed
	strings = aString.split('.')
	for temp in strings:
		if temp:
			temp = temp.replace('_',' ').strip().lower().capitalize()
			temp = re.sub(r" +", " ", temp)
		try:
			if ((temp[-1] != '.') & (temp[-1] != '!') & (temp[-1] != '?')):
				temp = (temp + '.')
			return temp
		except IndexError:
			print "Caught index error"

def spellCheck(dictionary, words):
#Checks if the word in a sentace are in the english language and if they are leaves them alone and if not deleates them
	correctWords = []
	#print "Got to spell check"
	for word in words:
		word = word.lower()
		for thing in dictionary:
			if ((word == thing) & (word != " ") & (word != "")):
				correctWords.append(word)
	#print "Leaving spellcheck"
	return correctWords
	

def nameCheck(names, words):
#The same as spellCheck
	#print "Enter Namecheck"
	correctNames = []
	for name in names:
		for word in words:
			#print word
			#put a capitalize function in there
			if ((name == word) & (word != "  ") & (word != "")):
				correctNames.append(name)
	#print "Exit Namecheck"
	return correctNames

def fixAbbreviation(aString):
#replaces select words with the correct abbriviation
	temp = aString.replace('Dr.','Doctor').replace('Rev.','Reverend').replace('Prof.','Professor').replace('St.','Saint').replace('Gen.','General').replace('Adm.','Admiral').replace('Cpt.','Captain').replace('Gen.','General')


def splitString(str):
#Makes it so that the word list can be imputed function without breaking 
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
	return words

stringToFix = str(sys.argv[1])
split = splitString(stringToFix) 

dict = open("dictionary.txt")
wl = dict.readlines()
dict.close()

names = open("names.txt")
nl = names.readlines()
names.close()

wordList = []
for word in wl:
	wordList.append(word.strip())

nameList = []
for name in nl:
	nameList.append(name.strip())

x = nameCheck(nameList, split)
x = ' '.join(x)
y = spellCheck(wordList, split)
y = ' '.join(y)

a = fixSentance(y)

b = fixSentance(x)
print "\n"
print "Correctly spelled words"
print a
print "\n"
print "Correct Names"
print b
