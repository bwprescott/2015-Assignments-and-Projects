def main():
  itemName = raw_input('Enter name of item purchased: ')
  year = int(raw_input('Enter year purchased: '))
  cost = float(raw_input('enter the cost: '))
  life = int(raw_input('life of item in years: '))
  method = raw_input('method of depreciation: ')
  printNow('description: ' + itemName)
  printNow('year of purchase:  ' + str(year))
  printNow('cost: $ %.2f ' %(cost))
  printNow('estimated life: ' + str(life) + ' years')
  printNow('method of depreciation:  ' + method)
  
  if method == "SL":
    value = cost
    endOfYear = 0
    for i in range(year, year + life):
      if i == year + life + 1:
        depreciation = value
      else:
        depreciation = cost * 1.0/life
      endOfYear += depreciation
      printNow('%d  %.2f   %.2f  %.2f' %(i, value, depreciation, endOfYear))
      value -= depreciation
        
  elif method == "DDB":
    value = cost
    endOfYear = 0
    for i in range(year, year + life):
      if i == year + life - 1:
        depreciation = value
      else:
        depreciation = value * 2.0/life
      endOfYear += depreciation
      printNow('%d  %.2f   %.2f  %.2f' %(i, value, depreciation, endOfYear))
      value -= depreciation
main()