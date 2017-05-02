import sys

def fixSentance(aString):
	x = 0
	while (x != 1):
		temp = aString
		temp.split('.')
		print temp.split('.')
		temp = temp.replace('_',' ').strip().lower().capitalize()
		if ((temp[-1] != '.') & (temp[-1] != '!') & (temp[-1] != '?')):
			temp = temp + '.'
		return temp

stringToFix = str(sys.argv[1])

print fixSentance(stringToFix)
# fixSentance
