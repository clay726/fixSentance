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

dict = open("dictionary.txt")
dict.close()

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

print fixSentance(stringToFix) 
