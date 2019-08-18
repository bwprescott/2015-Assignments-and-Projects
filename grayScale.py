def grayScale():
  pic = makePicture(pickAFile())
  show(pic)
  for p in getPixels(pic):
    average = (getRed(p) + getGreen(p) + getBlue(p))/3
    newColor = makeColor(average, average, average)
    setColor(p, newColor)
  show(pic)
grayScale()