def main():
  accounts = []
  pins = []
  balances = []
  fileInput = open(pickAFile(), 'rt')
  filedata = fileInput.readlines()
  fileInput.close()
  for line in filedata:
    items = line.split(';')
    accounts.append(items[0])
    pins.append(items[1])
    balances.append(items[2])
    
  while true:
    userInput = raw_input("D for Deposit, W for Withdraw, Q to Quit ")
    if userInput == "Q":
      for i in range(0, len(accounts)):
        printNow(accounts[i] + " " + str(balances[i]))
      break
      
    
    accountNumber = raw_input("Account Number: ")
    PIN = raw_input("PIN:")
    
    counter = 0
    
    while counter < len(accounts):
      if accounts[counter] != accountNumber:
        counter += 1
      else:
        break
        


    if pins[counter] == PIN:
      if userInput == "W":
        amount = requestInteger("Amount: ")
        if amount > float(balances[counter]):
          printNow("Insufficient Funds") 
          printNow(accounts[counter] + " " + balances[counter])
          pass
          
        elif amount <= balances[counter]:
          balances[counter] = float(balances[counter]) - amount
          printNow(accounts[counter] + " " + str(balances[counter]))
        
        
      elif userInput == "D":
        amount = requestInteger("Amount: ")
        balances[counter] = float(amount) + float(balances[counter])
        printNow(accounts[counter] + " " + str(balances[counter]))
    else:
      printNow("Invalid PIN")
      pass