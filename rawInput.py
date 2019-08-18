def main():
  firstName = raw_input('enter your first name:   ')
  printNow(firstName)
  gpa = float(raw_input('enter gpa'))
  age = int(raw_input('enter your age:'))
  printNow("%s: your gpa is %.2f and you are %d years old" %(firstName, gpa, age))
main()