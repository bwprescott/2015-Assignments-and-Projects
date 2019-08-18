def max(x, y, z):
  if x >= y and x >= z:
    return x
  elif y >= x and y >= z:
    return y
  elif z >= x and z >= y:
    return z
    

def main():
  x = requestInteger("x")
  y = requestInteger("y")
  z = requestInteger("z")
  result = max(x, y, z)
  printNow(result)
  
def temp():
  fah = requestInteger("Temp. in Fahrenheit")
  celsius = (fah-32)*5/9
  return celsius
  
def main2():
  newTemp = temp()
  printNow(newTemp)
  