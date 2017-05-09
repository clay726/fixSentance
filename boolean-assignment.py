import sys


foo = str(sys.argv[1])
bar = str(sys.argv[2])

if (foo & bar):
	print "AND" foo " " bar " TRUE"
else:
	print "AND" foo " " bar " FALSE"
