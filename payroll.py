def main():
  #tester = 25
  #developer = 30
  #manager = 40
  position = requestNumber("What is your position? (1 for tester, 2 for developer, 3 for manager))")
  #if you want to make it stupid proof, you could have any invalid number defualt to 1, or ask the question again
  hours = requestNumber("How many hours do you work weekly?")
  if hours <= 40:
    if position == 1:
      payroll = 25 * hours
    if position == 2:
      payroll = 30 * hours
    if position == 3:
      payroll = 40 * hours
  if hours > 40:
    if position == 1:
      payroll = (25 * hours) + (25 * 1.5 *(hours - 40))
    if position == 2:
      payroll = (30 * hours) + (30 * 1.5 *(hours - 40))
    if position == 3:
      payroll = (40 * hours) + (40 * 1.5 *(hours - 40))
      
  printNow("Your weekly payment is $" + str(payroll) + ".")
      
main()
    
    
    