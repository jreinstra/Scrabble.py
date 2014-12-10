from drawing import *

class ScrabbleRack :
	def __init__(self) :
		self	.height = 50
		self.width = 318
		self.tileWidth = 38
		#self.x = int(320 - (self.width / 2))
		self.x = 85
		self.y = 645

		self.tileYMin = int(self.y + (self.height / 2) - (self.tileWidth / 2))
		self.tileYMax = int(self.y + (self.height / 2) + (self.tileWidth / 2))

		self.tiles = {}

		self.draw()


	''''def placeTile(self, column, letter) :
		tileX = 	15 + (41 * column) + self.x
		newTile = Tile(tileX, self.tileYMin, self.tileWidth, self.tileWidth, letter)
		self.tiles[column] = newTile'''
	
	def getCoords(self, column) :
		tileY = self.tileYMin
		tileX = 	15 + (41 * column) + self.x
		return (tileX, tileY)

	''''def removeTile(self, column) :
			self.draw()
			delete = False
			for tile in self.tiles :
				if tile != column:
					self.tiles[tile].draw()
				else : delete = True
			if delete == True :
				del [self.tiles[column]]
			rackLetters[column] = ""'''



	''''def fillRack(self) :
		for column in rackLetters :
			if rackLetters[column] == "" :
				letter = fetchNewLetter()
				self.placeTile(column, letter)'''
	def isInRack(self, x, y) :
		inRack = x >= self.x and x <= (self.x + self.width) and y >= self.y and y <= (self.y + self.height)
		#print inRack
		return inRack

	def clicked(self, rackTiles, x, y) :
		selected = None
		for i in rackTiles :
			if rackTiles[i].isInTile(x, y) == True :
				selected = rackTiles[i]
			else :
				rackTiles[i].deselect()
		if selected != None :
			selected.select()
		return selected




	def draw(self) :
		draw.rect(self.x, self.y, self.x + self.width, self.y + self.height, fill="#CC9900", outline="#CC9900")

	clear = draw

