import re
fname = raw_input('Enter a file name: ')
try:
	fhandle = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
numlist = list()
for line in fhandle:
	line = line.rstrip()
	num = re.findall('^New .*: ([0-9]+)', line)
	if len(num) > 0:
		for number in num:
			number = float(number)
		numlist.append(number)
print sum(numlist) / len(numlist)