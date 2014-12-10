from drawing import *
from random import *
import time

class Tile :
	def __init__(self, x, y, width, height, letter, value = 0) :
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.letter = letter
		self.value = value
		self.PID = random() * int((time.time() + 0.5) * 1000)
		self.draw()
	
	def __str__(self) :
		return self.letter
	
	def __eq__(self, other) :
		if type(self) == type(other) : 
			return other.x == self.x and other.y == self.y and other.width == self.width and other.height == self.height and other.letter == self.letter and other.PID == self.PID
		else :
			return False
	
	def __ne__(self, other) :
		return not self.__eq__(other)
	
	def isInTile(self, x, y) :
		inTile = (x >= self.x and x <= (self.x + self.width - 1) and y >= self.y and y <= (self.y + self.height - 1))
		#print str(inTile)
		return inTile
	
	
	def select(self) :
		self.draw("#FFBF00")
	
	def deselect(self) :
		self.draw()
	
	##EBE39C#F68D5C
	def draw(self, color = "#fff2cc") :
		outlineColor = "Black"
		draw.rect(self.x, self.y, self.x + self.width - 1, self.y + self.height - 1, fill = color, outline = outlineColor)
		if self.letter != "_" :
			draw.text(self.x + (self.width / 2), self.y + (self.height / 2) - 5, text=self.letter, font="ComicSansMS 20 bold")
		draw.text(self.x + 20, self.y + self.height - 9, text=self.value, font="ComicSansMS 14 bold")
	#'''self.x + self.width - 7'''
	#"Scramble 20 bold"
	clear = draw




