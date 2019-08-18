def main():
  names = ["Alice", "Bob", "Dave", "Frank", "Carol"]
  names.sort()
  print names
  numbers = [64, 6, 37, 92, 37, 25, 26, 17]
  print numbers
  for n in numbers:
    if n == 37:
      numbers.remove(n)
  print numbers
  numbers.insert(3, 100)
  print numbers
  print numbers.pop()
  #you can specify an index
  print numbers
  print numbers[3:]


def main2():
  names = ["Alice", "Bob", "Carol"]
  print names[0][2]
main2()

def main3():
  afcS = ["Colts", "Titans", "Texans", "Jaguars"]
  afcE = ["Patriots", "Dolphins", "Jets", "Bills"]
  afcW = ["Chargers", "Chiefs", "Raiders", "Broncos"]
  afcN = ["Bengals", "Browns", "Steelers", "Ravens"]
  afc = [afcS, afcE, afcW, afcN]
  print afc[1][3][2]
main3()





