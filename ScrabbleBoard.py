from drawing import *

class ScrabbleBoard :
	def __init__(self) :
		self.tileWidth = 38
		self.tileBuffer = 2
		self.edgeBuffer = 1
		self.width = 600
		self.height = 600
		self.tiles = {}
		self.boardCenter = 320

		newWindow((2 * self.boardCenter), (2 * self.boardCenter) + 100)
		self.boardBuffer = int(self.boardCenter - (self.width / 2));

		self.draw()

	''''def placeTile(self, column, row, letter) :
		tileX = (column * (self.tileWidth + self.tileBuffer)) + self.edgeBuffer + self.boardBuffer
		tileY = (row * (self.tileWidth + self.tileBuffer)) + self.edgeBuffer + self.boardBuffer
		newTile = Tile(tileX, tileY, self.tileWidth, self.tileWidth, letter)

		self.tiles[(column, row)] = newTile'''
	
	def getCoords(self, column, row) :
		tileX = (column * (self.tileWidth + self.tileBuffer)) + self.edgeBuffer + self.boardBuffer
		tileY = (row * (self.tileWidth + self.tileBuffer)) + self.edgeBuffer + self.boardBuffer + 10
		return (tileX, tileY)
	
	def getColRowFromCoords(self, x, y) :
		column = (x - self.edgeBuffer - self.boardBuffer) / (self.tileWidth + self.tileBuffer)
		row = (y - self.edgeBuffer - self.boardBuffer - 10) / (self.tileWidth + self.tileBuffer)
		return (column, row)


	def isInBoard(self, x, y) :
		inBoard = x >= self.boardBuffer and x <= self.boardCenter + (self.width / 2) and y >= self.boardBuffer and y <= self.boardCenter + (self.height / 2)
		#print inBoard
		return inBoard
		

	''''def removeTile(self, column, row) :
		self.draw()
		delete = False
		for tile in self.tiles :
			if tile != (column, row) :
				self.tiles[tile].draw()
			else :
				delete = True
		if delete == True:
			del [self.tiles[(column, row)]]'''


	def draw(self) :
		drawGIF(self.boardCenter, self.boardCenter + 10, "board.gif")
		



