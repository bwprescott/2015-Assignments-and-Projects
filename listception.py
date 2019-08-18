def main():
  inputFile = file.open(pickAFile(),'rt')
  fileContents = inputFile.readlines()
  inputFile.close()
  print fileContents
  searchTerm = raw_input('enter name to search for: ')
  for s in fileContents:
    items = s.split(';')
    if items[0].find(searchTerm) != -1
      print items[1]
main()