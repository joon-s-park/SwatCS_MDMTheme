"""
J. Knerr
July, 2014

Lots of random squares and rectangles...

"""

#import gtk
import cairo
import math
import random
import colorsys

WIDTH = 1280
HEIGHT = 1024

WIDTH = 2560
HEIGHT = 1440
NC = 400
num_stars = 3000
radius = 100

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
# Draw something ...

# black background
#ctx.set_source_rgb(0.2, 0.2, 0.2)
ctx.set_source_rgb(0.0, 0.0, 0.0)
ctx.paint_with_alpha(1.0)

buffer = 300
cx = WIDTH/2
cy = HEIGHT/2

# circles/stars
for i in range(num_stars):
  x = random.randrange(0,WIDTH)
  #y = random.randrange(0,HEIGHT)
  #
  # set up milky-way like line from 0.75*HEIGHT on left to
  # 0.25*HEIGHT on right (use gaussian distribution)
  #
  peak = (0.75 - (0.5*(float(x)/WIDTH))) * HEIGHT
  y = random.gauss(peak,0.25*HEIGHT)
  #
  cradius = random.randrange(1,4)
  #h = float(x) / (1.0*WIDTH)
  h = random.random()
  s = random.randrange(0,4) * 0.1
  v = 1.0
  (r,g,b) = colorsys.hsv_to_rgb(h, s, v)
  ctx.arc(x, y, cradius, 0, math.pi*2) 
  a = random.randrange(5,11) * 0.1
  ctx.set_source_rgba(r,g,b,a)
  ctx.fill()
  ctx.stroke()

# login square
ctx.set_line_width(1)
ctx.set_source_rgb(0.0, 0.0, 0.0)
x = cx
y = cy
w = buffer*2
h = buffer*2*0.8
(r,g,b) = (46.0/255.0, 52.0/255.0, 54.0/255.0)
x1 = x-buffer
y1 = y-(buffer*0.9)
x2 = w
y2 = h
ctx.rectangle (x1, y1, x2, y2)
ctx.stroke_preserve()
lgrad = cairo.LinearGradient(x1,y1,x2,y2)
a = 1.0
lgrad.add_color_stop_rgba(0.0, r, g, b, a)
lgrad.add_color_stop_rgba(1.0, r, g, b, 1)
ctx.set_source_rgba(r,g,b,a)
ctx.fill()

# now the squares
num_squares = random.randrange(NC/2, NC)
for i in range(num_squares):
  ctx.set_line_width(1)
  ctx.set_source_rgb(0.0, 0.0, 0.0)
  x = random.randrange(0,WIDTH)
  y = random.randrange(0,HEIGHT)
  while x<cx+buffer and x>cx-(1.2*buffer) and y<cy+buffer and y>cy-buffer:
    # choose again to avoid middle
    x = random.randrange(0,WIDTH)
    y = random.randrange(0,HEIGHT)


  w = random.randrange(radius/2,radius)
  h = random.randrange(radius/2,radius)
  grey = random.randrange(0,8) * 0.1
  (r,g,b) = (grey, grey, grey)
  x1 = x
  y1 = y
  x2 = w
  y2 = h
  ctx.rectangle (x1, y1, x2, y2)
  ctx.stroke_preserve()
  lgrad = cairo.LinearGradient(x1,y1,x2,y2)
  a = random.randrange(5,11) * 0.1
  lgrad.add_color_stop_rgba(0.0, r, g, b, a)
  lgrad.add_color_stop_rgba(1.0, r, g, b, 1)
  ctx.set_source_rgba(r,g,b,a)
  ctx.fill()

# upper right square
ctx.set_line_width(1)
ctx.set_source_rgba(0.0, 0.0, 0.0, 0.8)
xw = 300
x = WIDTH-xw
y = 0
w = xw
h = xw*0.7
x1 = x
y1 = y
x2 = WIDTH
y2 = y+h
ctx.rectangle (x1, y1, x2, y2)
ctx.fill()

# add some images  ##########################################
images = ["xerus.png", "swatcs16.png", "uxerus.png"]
for i in images:
  image_surface = cairo.ImageSurface.create_from_png(i)
  ctx.save()
  x = random.randrange(0,WIDTH*0.9)
  y = random.randrange(0,HEIGHT*0.9)
  while x<cx+buffer and x>cx-buffer and y<cy+buffer and y>cy-buffer:
    # choose again to avoid middle
    x = random.randrange(0,WIDTH*0.9)
    y = random.randrange(0,HEIGHT*0.9)
  ctx.translate(x, y)
  ctx.set_line_width(2)
  ctx.set_source_surface(image_surface)
  ctx.paint()
  ctx.restore()

#############################################################

surface.write_to_png('squares.jpg')
