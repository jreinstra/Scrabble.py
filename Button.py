from drawing import *




class Button :
	##F68D5C#EBE39C
	def __init__(self, x, y, width, height, text, color = "#fff2cc", outline = "Black") :
		self.x1 = x
		self.y1 = y
		self.x2 = x + width
		self.y2 = y + height
		self.width = width
		self.height = height
		self.text = text
		self.color = color
		self.outline = outline
		self.draw(color, outline)
	
	def isInButton(self, x, y) :
		return x >= self.x1 and x <= self.x2 and y >= self.y1 and y <= self.y2
	
	def select(self) :
		self.draw("#FFBF00")
	
	def deselect(self) :
		self.draw()
	
	def updateText(self, text) :
		self.text = text
		self.remove()
		self.draw()
	
	def draw(self, color = None, outline = None) :
		if color == None:
			color = self.color
		if outline == None:
			outline = self.outline
		draw.rect(self.x1, self.y1, self.x2, self.y2, fill=color, outline=outline)
		draw.text(self.x2 - (self.width / 2), self.y2 - (self.height / 2), text=self.text)
	
	def remove(self) :
		draw.rect(self.x1, self.y1, self.x2, self.y2, fill="White", outline="White")