#loops
def decreaseRed():
  #do the following for all pixels
  #  grab a pixel
  #  grab its red component
  #  multiply by .5
  #  set as new red component
  picture = makePicture(pickAFile())
  explore(picture)
  for p in getPixels(picture):
    value = getRed(p)
    setRed(p, value *0.5)
  explore(picture)
decreaseRed()