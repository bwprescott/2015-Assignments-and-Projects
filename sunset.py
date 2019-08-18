def makeSunset():
  picture = makePicture(pickAFile())
  explore(picture)
  for p in getPixels(picture):
    blueValue=getBlue(p)
    setBlue(p, blueValue * .7)
    greenValue = getGreen(p)
    setGreen(p, greenValue * .7)
  explore(picture)
