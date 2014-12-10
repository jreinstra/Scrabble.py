import random
import time

file = open('/usr/share/dict/words')
nextLine = file.readline()[:-1]
wordList = {}
i = 0
while(nextLine != '') :
	if len(nextLine) >= 2 and len(nextLine) <= 7 :
		wordList[i] = nextLine
		i += 1
		#print nextLine
	nextLine = file.readline()[:-1]

for i in wordList :
	print wordList[i]
	#time.sleep(1)
	blank = raw_input(": ");
	if(blank == "stop" or blank == "Stop") :
		break