#Blake Prescott
#The purpose of the program is to use lists to show the grades of some students

def main():
#getting the file
  readFile = open(pickAFile(), 'rt')
  fileData = readFile.readlines()
  readFile.close()

#making each name/number it's own item in a list
  for s in fileData:
    items = s.split(' ')
#setting the grades
    grade = ((float(items[2]) + float(items[3]) + float(items[4]) + float(items[5]) + float(items[6]))*(40/500.0)) + ((float(items[7]) + float(items[8]) + float(items[9]) + float(items[10]) + float(items[11]))*(20/100.0)) + ((float(items[12]) + float(items[13]))*(40/200.0))
    if 90 <= grade <= 100:
      letter = "A"
    elif 80 <= grade < 90:
      letter = "B"
    elif 70 <= grade < 80:
      letter = "C"
    elif 60 <= grade < 70:
      letter = "D"
    elif grade < 60:
      letter = "F"
    printNow(items[0] + " " + items[1] + " " + letter)
    
main()