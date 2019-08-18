def main():
  inputFile = open(pickAFile(), 'rt')
  fileData = inputFile.readlines()
  inputFile.close()
  print fileData
  for line in fileData:
    words = line.split(' ')
    if words[2] = "Physics"
      print line
    weeklySalary = float(words[2] * float(words[3]))
main()