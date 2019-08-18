def negative():
  pic = makePicture(pickAFile())
  explore(pic)
  for p in getPixels(pic):
    newColor = makeColor(255-getRed(p), 255-getGreen(p), 255-getBlue(p))
    setColor(p, newColor)
  explore(pic)
negative()

  