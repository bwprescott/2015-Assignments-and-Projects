def main():
  for i in range(0, 5):
    printNow("hello")
    if i == 3:
      continue
    printNow("world")


def main2():
  for i in range(0,3):
    if i == 2:
      continue
    sys.stdout.write("G")
    


def main3():
  for i in range(0, 3):
    for j in range(0, 4):
      if j ==2:
        break
      sys.stdout.write("G")
      
def main4():
  x = 3
  y = 4
  printNow('%d %d' % (x, y))
  z = 3.14159293
  printNow('%.4f          %d' %(z, 6))