def main():
  readFile = open(pickAFile(), 'rt')
  fileData = readFile.readlines()
  readFile.close()
  reverse = list.reverse(fileData)
  printNow(reverse)
  
  
  

 

def main2():
  writeFile = open("output.txt", "wt")
  writeFile.write("Hello World")
  writeFile.close


def main3():
  readFile = open(pickAFile(), 'rt')
  fileData = readFile.readlines()
  readFile.close()
  frequency = [0,0,0,0,0,0,0,0,0,0]
  for f in fileData:
    frequency[int(f)] += 1
  print(frequency)
    