#compute p, n, i, loanBalance
#compute a
#loop that runs from 1 to n
#  Ik = loanBalance * i
#  Pk = a -Ik
#  loanBalane -= Pk
#  print k, Pk, Ik, a, loanBalance

def main():
  #user input
  costOfHome = requestNumber("Cost of Home: ")
  downPayment = requestNumber("Down Payment: ")
  loanPeriod = requestNumber("Loan Period: ")
  percentage = requestNumber("Annual Percentage: ")
  
  P = costOfHome - downPayment
  n = loanPeriod*12
  i = percentage / 1200
  A = (P * i * pow(1 + i, n))/(pow(1 + i, n) - 1)
  
  for n in range(1,n):
    ik = i * P
    PrP = A - ik
    P -= PrP
    printNow(str(n) + "  " + str(PrP) + "  " + str(ik) + "  " + str(A) + "  " + str(P))
    
main()