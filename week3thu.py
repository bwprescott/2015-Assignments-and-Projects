def main():
  myPic = makePicture(pickAFile())
  explore(myPic)
  #printNow(getWidth(myPic))
  #printNow(getHeight(myPic))
  myPix = getPixel(myPic, 50, 50)
  setRed(myPix, 255)
  setBlue(myPix, 255)
  setGreen(myPix, 255)
  explore(myPic)
  #printNow(myPix)
  #printNow(getGreen(myPix))
  #printNow(getRed(myPix))
  #printNow(getBlue(myPix))
  
  
  
main()
