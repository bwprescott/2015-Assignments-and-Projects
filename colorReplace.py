def change():
  x = requestInteger("Change:")
  quarters = x/25
  printNow(quarters)
  dimes = (x - (quarters * 25))/10
  printNow(dimes)
  nickels = (x - (quarters * 25) - (dimes * 10))/5
  printNow(nickels)
  pennies = (x - (quarters * 25) - (dimes * 10) - (nickels * 5))
  printNow(pennies)
  