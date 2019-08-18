def main():
  for i in range(0,3):
    for j in range(0, 4):
      if j == 2:
        continue
      printNow('G')
      
def main2():
  x = 5
  y = 10
  if x != 10:
    printNow('hello')
  else:
    printNow('world')