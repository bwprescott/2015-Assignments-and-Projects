def mirrorVertical(pic):
  width = getWidth(pic)
  mirror = width / 2
  height = getHeight(pic)
  for y in range(0, height):
    for x in range(0, mirror)
    left = getPixel(pic, x, y)
    right = getPixel(pic, width - x - 1, y)
    c = getColor(left)
    setColor(right, c)
  show(pic)
  
mirrorVertical(makePicture(getMediaPath("vi.jpg")))