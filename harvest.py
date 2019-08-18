def costOfHarv():
  #cost = length*width*cost
  length = requestNumber("What is the length of your field?")
  breadth = requestNumber("What is the breadth of your field?")
  rate = requestNumber("What is the rate per square foot of your field?")
  cost = length * breadth* rate
  printNow("The total cost of harvesting this field is $" + str(cost))