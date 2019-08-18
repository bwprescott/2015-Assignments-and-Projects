def main():
  n = requestInteger("please enter an integer")
  
  for i in range(0, n):
    for j in range(0, i+1):
      sys.stdout.write('*')
    sys.stdout.write('\n')
  
  for i in range(0, n):
    for j in range(0, n-i):
      sys.stdout.write('*')
    sys.stdout.write('\n')
    
  for i in range(0, n):
    for j in range(0, i+1):
      sys.stdout.write(' ')
    for x in range(0, n - j):
      sys.stdout.write('*')  
    sys.stdout.write('\n')
    
  for i in range(0, n):
    for j in range(0, n-i):
      sys.stdout.write(' ')
    for x in range(0, n - j):
      sys.stdout.write('*')
    sys.stdout.write('\n')
  
 
  
  #sys.stdout.write("c")
  #sys.stdout.write("c")
  #sys.stdout.write("\n")
  #sys.stdout.write("c")
  #sys.stdout.write("c")
  #sys.stdout.write("\t")
  #sys.stdout.write("c")
  #sys.stdout.write("c")
  #for i in range(1, 11):
  # printNow("Number is " + str(i) + ". Square is " + str(i * i) + ".")

main()