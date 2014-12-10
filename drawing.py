from Tkinter import *
from random import *

class toolbox :
  CANVAS = WINDOW = None
  SIZE = 0
  imageMap = {}

draw = toolbox()

def newWindow (width = 600, height = 600) :
  if draw.WINDOW != None :
    draw.WINDOW.destroy()
  draw.WINDOW = Tk()
  draw.SIZE = width
  CANVAS = Canvas(draw.WINDOW , height = height , width = width )
  draw.line = CANVAS.create_line
  draw.oval = CANVAS.create_oval
  draw.rect = CANVAS.create_rectangle
  draw.polygon = CANVAS.create_polygon
  draw.text = CANVAS.create_text
  draw.CANVAS = CANVAS
  CANVAS.pack()
  #draw.WINDOW.mainloop()


def drawGIF (x,y,imgFile) :
  imgObj = PhotoImage(file = imgFile)
  draw.imageMap[imgFile] = imgObj
  draw.CANVAS.create_image(x,y,image = imgObj)

def bindMouseClick (f) :
  draw.WINDOW.bind('<Button-1>' , lambda event : f(event.x,event.y))

def bindKeyChar (f) :
  draw.WINDOW.bind('<Key>' , lambda event : f(event.char))

def HELP () :
  print """
SAMPLES
draw.line(100,100,200,300,fill='blue')
draw.oval(100,100,200,300,fill='blue')
draw.rect(400,400,200,300,fill='red',outline='blue')
draw.polygon(100,200,100,300,500,200, outline='grey')
draw.gif(300,300,'knight.gif')  <--  centered on 300,300
draw.text(200,300,text='hello!')

def keyDemo (char) :
  print char
  return char
bindKeyChar ( keyDemo )

def moveBox ( x,y ) :
  draw.rect (0,0,draw.SIZE,draw.SIZE,fill='white',outline='white')
  draw.rect (x,y,x+100,y+100,fill='red',outline='red')
bindMouseClick ( moveBox )

To use other Tk drawing commands use draw.CANVAS or draw.WINDOW :
draw.CANVAS.create_arc( ... , ... )
draw.WINDOW.bind ( '<B1-Motion>' , .... )

For image formats other than gif, download the Python Image Library:
http://effbot.org/imagingbook/pil-index.htm

To restart the window,
newWindow(800)

To quit,
quit()
"""

def welcome () :
  newWindow()
  print "type HELP() for help, quit() to quit"

def exitDraw() :
  draw.WINDOW.destroy()
  quit()

#welcome()
