def main():
  names = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank"]
  print names[0:3]
  print names[:5]
  print len(names)
  for n in names:
    print n
  numbers = [23, 40 ,45, 54, 31, 12, 10]
  print numbers[2]
  numbers[2] = 95
  print numbers[2]
  for n in numbers:
    print n * 10
main()
