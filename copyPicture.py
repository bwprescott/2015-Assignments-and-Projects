
def copyPicture(src, dst, dstX, dstY):
  dx = dstX
  for x in range(0, getWidth(src)):
    dy = dstY
    for y in range(o, getHeight(src)):
      srcPixel = getPixel(src, x, y)
      dstPixel = getPixel(dst, dx, dy)
      srcPixelColor = getColor(srcPixel)
      setColor(dstPixel, srcPixelColor)
      dy += 1
    dx+=1



def mirrorVertical(picture):
  width = getWidth(picture)
  mirror = width / 2
  height = getHeight(picture)
  for y in range(0, height):
    for x in range(width-1, mirror, -1):
      right = getPixel(picture, x, y)
      left = getPixel(picture, width - x - 1, y)
      c = getColor(right)
      setColor(left, c)
  show(picture)

def grayScale(picture):
  for p in getPixels(picture):
    average = (getRed(p) + getGreen(p) + getBlue(p))/3
    newColor = makeColor(average, average, average)
    setColor(p, newColor)
  show(picture)

def finalThing():
  grayScale(makePicture(getMediaPath("vi.jpg")))
  mirrorVertical(makePicture(getMediaPath("vi.jpg")))

dst = makeEmptyPicture(1000, 1000)
#original = makePicture("vi.jpg")
#copyPicture(negative(original), dst, getWidth(original), 0)
#original = makePicture("vi.jpg")
#copyPicture(mirrorVertical(original), dst, 0, getHeight(original))
