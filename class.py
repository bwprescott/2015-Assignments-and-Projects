class Book(object):
  def __init__(self, t, a, p, pu):
    self.title = t
    self.author = a
    self.price = p
    self.publisher = pu
  def printInformation(self):
    printNow(self.title + " " + self.author + " " + str(self.price) + " " + self.publisher)
  def getPrice(self):
    return self.price
  def setPrice(self, pct):
    self.price = self.price - (pct/100.0) * self.price
  
    
    
def main():
  b0 = Book("Harry Potter", "J. K. Rowling", 19.99, "Pearson")
  b1 = Book("It", "Stephen King", 30, "Harper Collins")
  b2 = Book("Fifty Shades of Grey", "John Doe", 10.99, "Wesly")
  library = [b0, b1, b2]
  library[1].printInformation()
  printNow(library[2].getPrice())
  printNow(b1.getPrice())
  b1.setPrice(20)
  printNow(b1.getPrice())
  library[1].setPrice(20)
  for v in library:
    printNow(b.getPrice())
    
main()
  
  
  