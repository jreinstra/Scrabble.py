from random import *
from drawing import *
import time

from ScrabbleBoard import *
from ScrabbleRack import *
from ScrabbleTile import *
from Button import *


TILE_SIZE = 38
TILE_BUFFER = 2
TILE_EDGE_BUFFER = 1
BOARD_SIZE = 600
WIDTH = 700
HEIGHT = 800
RACK_Y = 645



#This data structure was inspired by Ian Loftis's data structure
#should be "_":2
letterDistribution = {"_":0, "A":9, "B":2, "C":2, "D":4, "E":12, "F":2, "G":3, "H":2, "I":9, "J":1, "K":1, "L":4, "M":2, "N":6, "O":8, "P":2, "Q":1, "R":4, "S":4, "T":6, "U":4, "V":2, "W":2, "X":1, "Y":2, "Z":1}

lettersRemaining = []

#letterValues = {"_":0, "A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2, "H":4, "I":1, "J":8, "K":5, "L":1, "M":3, "N":1, "O":1, "P":3, "Q":10, "R":1, "S":1, "T":1, "U":1, "V":4, "W":4, "X":8, "Y":4, "Z":10}

#letterValues = {"_":0, "A":100, "B":300, "C":300, "D":200, "E":100, "F":400, "G":200, "H":400, "I":100, "J":800, "K":500, "L":100, "M":300, "N":100, "O":100, "P":300, "Q":1000, "R":100, "S":100, "T":100, "U":100, "V":400, "W":400, "X":800, "Y":400, "Z":1000}

letterValues = {"_":0, "A":900, "B":2700, "C":2700, "D":1800, "E":900, "F":3600, "G":1800, "H":3600, "I":900, "J":7200, "K":4500, "L":900, "M":2700, "N":900, "O":900, "P":2700, "Q":9000, "R":900, "S":900, "T":900, "U":900, "V":3600, "W":3600, "X":7200, "Y":3600, "Z":9000}


boardTiles = {}
rackTiles = {}
placedTileAddresses = {}
selectedTile = None

wordList = {}
overlapsLastTime = -1
currentOverlap = 0
currentWordsLength = 0
wordsLengthLastTime = 0

currentScore = 0
score = 0

#multipliers = {}
#entry = 0

letterMultipliers = {(7, 3): 2, (9, 1): 3, (5, 9): 3, (6, 6): 2, (3, 0): 2, (2, 8): 2, (5, 13): 3, (9, 9): 3, (6, 2): 2, (11, 14): 2, (3, 7): 2, (7, 11): 2, (0, 3): 2, (3, 14): 2, (5, 1): 3, (5, 5): 3, (12, 6): 2, (1, 5): 3, (0, 11): 2, (8, 6): 2, (2, 6): 2, (8, 2): 2, (9, 13): 3, (11, 0): 2, (1, 9): 3, (13, 9): 3, (6, 12): 2, (14, 11): 2, (11, 7): 2, (6, 8): 2, (8, 12): 2, (13, 5): 3, (8, 8): 2, (14, 3): 2, (9, 5): 3, (12, 8): 2}

wordMultipliers = {(13, 13): 2, (0, 14): 3, (12, 12): 2, (3, 11): 2, (0, 7): 3, (2, 12): 2, (11, 11): 2, (12, 2): 2, (3, 3): 2, (4, 4): 2, (2, 2): 2, (1, 1): 2, (4, 10): 2, (7, 14): 3, (0, 0): 3, (10, 4): 2, (1, 13): 2, (14, 14): 3, (13, 1): 2, (7, 0): 3, (10, 10): 2, (14, 7): 3, (11, 3): 2, (14, 0): 3}

multipliersToDelete = {}


def main() :
	global board
	global rack
	global checkButton
	global nextTurnButton
	global getHintButton
	#global switch
	global checkButtonFunction
	global nextTurnButtonFunction
	global scoreLabel
	
	checkButtonFunction = checkBoard
	nextTurnButtonFunction = doNothing
	
	loadWordList()
	board = ScrabbleBoard()
	#placeTileOnBoard(board, 1, 1, "A")
	rack = ScrabbleRack()
	checkButton = Button((WIDTH - 285), RACK_Y, 100, 50, "Check Words")
	nextTurnButton = Button((WIDTH - 170), RACK_Y, 100, 50, "Next Turn")
	getHintButton = Button(10, RACK_Y, 60, 50, "Cheat")
	scoreLabel = Button(20, 15, 100, 10, "Score: 0", "White", "White")
	#switch = Button(10, 10, 10, 10, "Switch")
	nextTurnButton.remove()
	fillRack(rack)
	bindMouseClick(clicked)
	
	''''while True:
		clicked(10 + 5, RACK_Y + 5)
		clicked(WIDTH - 285 + 5, RACK_Y + 5)
		clicked(WIDTH - 170 + 5, RACK_Y + 5)
		time.sleep(1)'''



def placeTileOnBoard(board, column, row, letter) :
	global letterValues
	coords = board.getCoords(column, row)
	newTile = Tile(coords[0], coords[1], TILE_SIZE, TILE_SIZE, letter, letterValues[letter])
	global boardTiles
	boardTiles[(column, row)] = newTile
	resetButtons()


def clicked(x, y) :
	global rackTiles
	global rack
	global board
	global selectedTile
	global placedTileAddresses
	global currentOverlap
	global overlapsLastTime
	global currentWordsLength
	global wordsLengthLastTime
	
	global nextTurnButton
	global checkButton
	global getHintButton
	
	#global switch
	#global multipliers
	#global entry
	global checkButtonFunction
	global nextTurnButtonFunction
	
	if rack.isInRack(x, y) == True :
		#if checkButtonFunction != fillRack :
			selectedTile = rack.clicked(rackTiles, x, y)
			#print selectedTile
	
	if board.isInBoard(x, y) == True:
		boardClicked(x, y)
		#makeMultipliers(x, y)
	if checkButton.isInButton(x, y) == True:
		checkButtonFunction()
		#checkBoard()
	if nextTurnButton.isInButton(x, y) == True:
		nextTurnButtonFunction()
		#overlapsLastTime = currentOverlap
		#wordsLengthLastTime = currentWordsLength
		
		#placedTileAddresses = {}
		#fillRack()
	if getHintButton.isInButton(x, y) == True:
		getHint()
	''''if switch.isInButton(x, y) == True:
		#multipliers = {}
		entry = int(raw_input("?: "))'''


def boardClicked(x, y) :
	global board
	global rack
	global selectedTile
	global rackTiles
	global boardTiles
	global placedTileAddresses

	colrow = board.getColRowFromCoords(x, y)
	try :
		boardTiles[colrow]
	except KeyError:
		boardTiles[colrow] = None
	if selectedTile != None and boardTiles[colrow] == None:
		placeTileOnBoard(board, colrow[0], colrow[1], str(selectedTile))
		placedTileAddresses[colrow] = colrow
		selectedTile.deselect()
		removeTileFromRack(rack, selectedTile)
		
		selectedTile = None
		#del boardTiles[colrow]
	elif boardTiles[colrow] != None:
		#print placedTileAddresses
		#print str(colrow)
		if colrow in placedTileAddresses :
			#print "This is also true!"
			deleteIndex = None
			for index in placedTileAddresses:
				if colrow == index:
					deleteIndex = index
			if deleteIndex != None :
				del placedTileAddresses[deleteIndex]
			lastColumn = -1
			for column in range(0, 7) :
				try :
					rackTiles[column]
				except KeyError:
					rackTiles[column] = None
				if rackTiles[column] == None:
					placeTileOnRack(rack, column, str(boardTiles[colrow]))
					removeTileFromBoard(board, boardTiles[colrow])
					break
	try :
		if boardTiles[colrow] == None :
			del boardTiles[colrow]
	except KeyError:
		nothing = "do"
		



def placeTileOnRack(rack, column, letter) :
	global letterValues
	coords = rack.getCoords(column)
	newTile = Tile(coords[0], coords[1], TILE_SIZE, TILE_SIZE, letter, letterValues[letter])
	global rackTiles
	rackTiles[column] = newTile

def removeTileFromRack(rack, tile) :
	rack.draw()
	global rackTiles
	deleteIndex = None
	for column in rackTiles :
		if rackTiles[column] != tile :
			rackTiles[column].draw()
		else :
			deleteIndex = column
	if deleteIndex != None :
		del rackTiles[deleteIndex]

def removeTileFromBoard(board, tile) :
	board.draw()
	global rackTiles
	deleteIndex = None
	for colrow in boardTiles : 
			if boardTiles[colrow] == tile :
				deleteIndex = colrow
			elif boardTiles[colrow] != None :
				boardTiles[colrow].draw()
	if deleteIndex != None :
		del boardTiles[deleteIndex]
	resetButtons()


def nextTurn() :
	global overlapsLastTime
	global wordsLengthLastTime
	global currentOverlap
	global currentWordsLength
	global placedTileAddresses
	global score
	global currentScore
	global scoreLabel
	
	fillRack()
	resetButtons()
	overlapsLastTime = currentOverlap
	wordsLengthLastTime = currentWordsLength
	placedTileAddresses = {}
	#deleteMultipliers()
	#score += currentScore
	score = currentScore
	scoreLabel.updateText("Score: " + str(score))
	print score


def deleteMultipliers() :
	global multipliersToDelete
	print multipliersToDelete
	global letterMultipliers
	global wordMultipliers
	
	do = "something"
	for i in multipliersToDelete:
		
		try:
			del wordMultipliers[i]
		except KeyError:
			do = "nothing"
		try:
			del letterMultipliers[i]
		except KeyError:
			do = "nothing"
	print do


def fillRack(inputRack = None) :
	global rackTiles
	global rack
	
	if inputRack == None:
		inputRack = rack
	for column in range(0, 7) :
		try :
			rackTiles[column]
		except KeyError :
			rackTiles[column] = None
		
		if rackTiles[column] == None :
			letter = fetchNewLetter()
			placeTileOnRack(inputRack, column, letter)


def resetButtons() :
	global checkButtonFunction
	global checkButton
	global nextTurnButtonFunction
	global nextTurnButton
	
	checkButtonFunction = checkBoard
	nextTurnButtonFunction = doNothing
	#checkButton.text = "Check Words"
	nextTurnButton.remove()
	checkButton.draw()

def setButtons() :
	global checkButtonFunction
	global checkButton
	global nextTurnButtonFunction
	global nextTurnButton
	
	checkButtonFunction = doNothing
	nextTurnButtonFunction = nextTurn
	#checkButton.text = "Next Turn"
	nextTurnButton.draw()
	checkButton.remove()
	

def fetchNewLetter() :
	global lettersRemaining
	initLettersRemaining()
	indexDouble = len(lettersRemaining) * random()
	index = int(indexDouble)
	#print index
	letter = None
	while letter == None:
		if index < 0 :
			return "You Win!"
		try:
			letter = lettersRemaining[index]
		except IndexError:
			letter = None
			index -= 1
	if letterDistribution[letter] > 0 :
		letterDistribution[letter] -= 1
	return letter


def initLettersRemaining() :
	letters = []
	for index in letterDistribution :
		for x in range(0, letterDistribution[index]) :
			letters += [index]
	global lettersRemaining
	lettersRemaining = letters
	#print lettersRemaining

def loadWordList() :
	file = open('words.txt')
	nextLine = file.readline()[:-2]
	global wordList
	i = 0
	while(nextLine != '') :
		if len(nextLine) >= 2 and len(nextLine) <= 7 :
			wordList[i] = nextLine.upper()
			i += 1
			#print nextLine
		nextLine = file.readline()[:-2]
	#print wordList


def checkBoard() :
	global placedTileAddresses
	global selectedTile
	global rack
	global currentScore
	global multipliersToDelete
	#global checkedButtonFunction
	
	if not isBoardValid():
		currentScore = 0
		multipliersToDelete = {}
		selectedTile = None
		colrows = {}
		#allows placedTileAddresses to be modified during next loop
		for i in placedTileAddresses :
			colrows[i] = placedTileAddresses[i]
		for colrow in colrows :
			coords = board.getCoords(colrow[0], colrow[1])
			boardClicked(coords[0] + 10, coords[1] + 10)
	else:
		setButtons()	



def isBoardValid() :
	#global placedTileAddresses
	global letterValues
	global wordList
	global boardTiles
	global overlapsLastTime
	global currentOverlap
	global currentWordsLength
	
	if isInOneColumnOrRow() == False :
		print "False because of colrow"
		return False
	
	words = {"orphans":{}}
	words = getHorizWords(words)
	words = getVertWords(words)
	print boardTiles
	print words
	orphans = words["orphans"]
	orphanLength = len(orphans)
	wordsLength = 0
	del words["orphans"]
	for word in words :
		print word
		print words[word]
		wordsLength += len(words[word])
		match = False
		for i in wordList :
			#print i
			#print wordList[i]
			if wordList[i] == words[word] :
				match = True
		if match == False and not "_" in words[word]:
			print "False because of invalid word"
			return False
		elif match == False:
			index = words[word].index("_")
			for i in letterValues:
				newWord = words[word][:index] + i + words[word][index + 1:]
				for j in wordList :
					if wordList[j] == newWord :
						match = True
			if match == False:
				print "False because of invalid word _"
				return False
				
	#print "True"
	#print placedTileAddresses
	#print "Number of overlap: " + str(len(placedTileAddresses) - orphanLength)
	#print orphanLength
	overlap = len(boardTiles) - orphanLength
	currentOverlap = overlap
	currentWordsLength = wordsLength
	print "Overlap: " + str(overlap)
	print "Words length: " + str(wordsLength)
	print 
	
	if (wordsLength - (2 * overlap) < orphanLength) or ((overlap <= overlapsLastTime) and wordsLength == wordsLengthLastTime) :
		print "False because of overlap problems"
		return False
	overlapsLastTime = overlap
	print "True"
	return True


def isInOneColumnOrRow() :
	global placedTileAddresses
	sameColumn = True
	sameRow = True
	
	startingColumn = None
	startingRow = None
	
	for colrow in placedTileAddresses :
		if startingColumn == None :
			startingColumn = colrow[0]
		elif colrow[0] != startingColumn :
			sameColumn = False
		else :
			startingColumn = colrow[0]
			
		if startingRow == None :
			startingRow = colrow[1]
		elif colrow[1] != startingRow :
			sameRow = False
		else :
			startingRow = colrow[1]
	print "sameRow: " + str(sameRow) + ", sameColumn: " + str(sameColumn) 
	return sameRow == True or sameColumn == True


def getHorizWords(words) :
	global boardTiles
	#words = {}
	for row in range(0, 16) :
		word = ""
		for column in range(0, 16) :
			char = ""
			try:
				char = str(boardTiles[(column, row)])
			except KeyError:
				char = " "
			if char == None or char == "None" :
				char = " "
			#rowWord += char
			#print "Vert: " + word
			if char == " " and len(word) >= 2:
				if word != None and word != "None":
					words[word + str((column - 1, row))] = word
					wordScore = getScore(((column - len(word) - 1, row), (column - 1, row)), word, True)
				word = ""
			elif char == " " and len(word) == 1:
				words["orphans"][(column - 1, row)] = word
				word = ""
			elif char != " " and char != None and char != "None":
				word += char
	return words



def getVertWords(words) :
	global boardTiles
	#words = {}
	for column in range(0, 16) :
		word = ""
		for row in range(0, 16) :
			char = ""
			try:
				char = str(boardTiles[(column, row)])
			except KeyError:
				char = " "
			if char == None or char == "None" :
				char = " "
			#rowWord += char
			#print "Vert: " + word
			if char == " " and len(word) >= 2:
				if word != None and word != "None":
					words[word + str((column, row - 1))] = word
					wordScore = getScore(((column, row - len(word) - 1), (column, row - 1)), word, True)
				word = ""
			elif char == " " and len(word) == 1:
				words["orphans"][(column, row - 1)] = word
				word = ""
			elif char != " " and char != None and char != "None":
				word += char
	return words


def getSimpleScoreForWord(word) :
	global letterValues
	score = 0
	for letter in word :
		score += letterValues[letter]
	return score


def getScore(colrows, word, real = False) :
	global currentScore
	
	if colrows == None:
		return 0
	i = 0
	score = 0
	wordMultipliers = []
	if colrows[0][0] == colrows[1][0]:
		column = colrows[0][0]
		for row in range(colrows[0][1], colrows[1][1]):
			colrow = (column, row)
			score += getScoreForSpace(colrow, word[i])
			wordMultipliers += [getWordMultiplierForSpace(colrow)]
			i += 1	
	
	elif colrows[0][1] == colrows[1][1]:
		row = colrows[0][1]
		for column in range(colrows[0][0], colrows[1][0]):
			colrow = (column, row)
			score += getScoreForSpace(colrow, word[i])
			wordMultipliers += [getWordMultiplierForSpace(colrow)]
			i += 1
	finalScore = score
	if len(wordMultipliers) > 0:
		for i in wordMultipliers:
			finalScore += (score * i)
	if real == True:
		currentScore += finalScore
	return finalScore


def getScoreForSpace(colrow, letter, real = False) :
	global letterValues
	global letterMultipliers
	global multipliersToDelete
	
	score = 0
	try:
		score = letterValues[letter] * letterMultipliers[colrow]
		if real == True:
			multipliersToDelete[colrow] = colrow
	except KeyError:
		score = letterValues[letter]
	print "Letter: " + str(letter) + ", Colrow: " + str(colrow) + ", Score: " + str(score)
	return score


def getWordMultiplierForSpace(colrow, real = False) :
	global wordMultipliers
	global multipliersToDelete
	
	try:
		result = wordMultipliers[colrow]
		if real == True:
			multipliersToDelete[colrow] = colrow
	except KeyError:
		result = 0
	return result


def getHint() :
	global rackTiles
	global letterValues
	global boardTiles
	global currentScore
	
	currentScore = 0
	
	startingWord = ""
	result = {}
	
	for i in rackTiles :
		startingWord += str(rackTiles[i])
	print startingWord
	
	if len(boardTiles) == 0:
		findWordsWithUnderscore(startingWord, result)
	else :
		for j in boardTiles :
			letter = str(boardTiles[j])
			word = startingWord + letter
			
			findWordsWithUnderscore(word, result)
	
	#scoreResult = {}
	''''for i in result :
		score = getSimpleScoreForWord(result[i])
		scoreResult[i] = (result[i], score)'''
	validWords = {}
	for i in result :
		colrows = findSpotForWord(result[i])
		score = getScore(colrows, result[i], False)
		if colrows != None:
			validWords[colrows] = (result[i], score)
	
	chosenWord = None
	for i in validWords:
		if chosenWord == None:
			chosenWord = (i, validWords[i])
		elif validWords[i][1] > chosenWord[1][1]:
			chosenWord = (i, validWords[i])
	if chosenWord != None:
		#getScore(chosenWord[0], chosenWord[1][0], True)
		makeWord(chosenWord[0], chosenWord[1][0])
	#print result
	print validWords
	#print scoreResult


def makeWord(colrows, word):
	i = 0
	if colrows[0][0] == colrows[1][0]:
		column = colrows[0][0]
		for row in range(colrows[0][1], colrows[1][1]):
			colrow = (column, row)
			makeTileAtColrow(colrow, word[i])
			i += 1
			
	elif colrows[0][1] == colrows[1][1]:
		row = colrows[0][1]
		for column in range(colrows[0][0], colrows[1][0]):
			colrow = (column, row)
			makeTileAtColrow(colrow, word[i])
			i += 1

def makeTileAtColrow(colrow, letter):
	global board
	global rackTiles
	global selectedTile
	#print "Make " + str(letter) + " at " + str(colrow)
	coords = board.getCoords(colrow[0], colrow[1])
	
	for i in rackTiles:
		if letter == str(rackTiles[i]):
			selectedTile = rackTiles[i]
			break
	boardClicked(coords[0] + 10, coords[1] + 10)


def findWordsWithUnderscore(word, result) :
	global letterValues
	
	if "_" in word :
		index = word.index("_")
		for letter in letterValues :
			newWord = word[:index] + letter + word[index + 1:]
			#newWord = word[:index] + letter + word[index + 1:]
			print newWord
			result = findWords(word, result)
	else :
		print word
		result = findWords(word, result)
		return result
	return result


#Mr. Yeh's function
def subset (s1, s2) :
	#print "s1: " + s1 + ", s2: " + s2
	for letter in s1 :
		index = s2.find(letter)
		if index == -1:
			return False
		else :
			s2 = s2[:index] + s2[index + 1:]
	return True

#Also Mr. Yeh
def findAnagrams(rack) :
	if rack == '' :
		return ['']
	result = []
	for i in wordList :
		if subset(wordList[i], rack) :
			difference = subtract(wordList[i], rack)
			#recursion!
			partials = findAnagrams(difference)
			result += map (lambda anagram : wordList[i] + ' ' + anagram, partials)
	return result


def findSpotForWord(word) :
	global boardTiles
	global rackTiles
	
	rackWord = ""
	for i in rackTiles:
		rackWord += str(rackTiles[i])
		
	result = None
	if len(boardTiles) == 0:
		colrow1 = (7 - int(len(word) / 2), 7)
		colrow2 = (colrow1[0] + len(word), 7)
		return (colrow1, colrow2)
	elif subset(word, rackWord) == False:
		for i in boardTiles:
			if str(boardTiles[i]) in word and not str(boardTiles[i]) in rackWord:
				result = findSpotFromCoords(word, i)
				if result != None:
					return result
	else :	
		for i in boardTiles:
			if str(boardTiles[i]) in word:
				result = findSpotFromCoords(word, i)
				if result != None:
					return result


def findSpotFromCoords(word, coords) :
	#print coords
	global boardTiles
	index = word.index(str(boardTiles[coords]))
	
	vertWorks = True
	horizWorks = True
	
	for row in range(coords[1] - index - 1, coords[1] - index + len(word) + 1):
		if row != coords[1]:
			if (row > 15 or row < -1): #and row != coords[1] - index + len(word) + 1:
				vertWorks = False
			if tileFullyClear(coords[0], row) == False:
				vertWorks = False
			if row != (coords[1] - index - 1) and row != (coords[1] - index + len(word) + 1):
				if tileFullyClear(coords[0] + 1, row) == False:
					vertWorks = False
				if tileFullyClear(coords[0] - 1, row) == False:
					vertWorks = False
	for column in range(coords[0] - index - 1, coords[0] - index + len(word) + 1):
		if column != coords[0]:
			if (column > 15 or column < -1):# and column != coords[0] - index + len(word) + 1:
				horizWorks = False
			if tileFullyClear(column, coords[1]) == False:
				horizWorks = False
			if column != (coords[0] - index - 1) and column != (coords[0] - index + len(word) + 1):
				if tileFullyClear(column, coords[1] + 1) == False:
					horizWorks = False
				if tileFullyClear(column, coords[1] - 1) == False:
					horizWorks = False
	if vertWorks == False and horizWorks == False:
		#print "False in find spot from coords"
		return None
	if vertWorks == True:
		return ((coords[0], coords[1] - index), (coords[0], coords[1] - index + len(word)))
	if horizWorks == True:
		return ((coords[0] - index, coords[1]), (coords[0] - index + len(word), coords[1]))
	return None


def tileFullyClear(column, row) :
	global boardTiles
	
	colrow = (column, row)
	try :
		test = boardTiles[colrow]
		return False
	except KeyError :
		return True


def findWords(word, result) :
	global wordList
	for i in wordList :
		if subset(wordList[i], word) :
			result[i] = wordList[i]
	return result


#Also Mr. Yeh
def subtract(s1, s2) :
	for letter in s1:
		index = s2.find(letter)
		s2 = s2[:index] + s2[index + 1:]
	return s2
	
''''def makeMultipliers(x, y) :
	global board
	global multipliers
	global currentType
	global entry
	
	colrow = board.getColRowFromCoords(x, y)
	multipliers[colrow] = entry
	print multipliers'''
	

def doNothing() :
	do = "nothing"


main()
draw.WINDOW.mainloop()






