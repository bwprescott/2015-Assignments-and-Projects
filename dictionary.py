def main():
  students = [{'FirstName' : 'Alice', 'LastName' : 'Smith'}, {'FirstName' : 'Bob', 'LastName' : 'Jones'}]
  print len(students)
  print students[0]
  print students[1]
  print students[0]['LastName']
  students[0]['LastName'] = "Buis"
  students[0]['Major'] = "Physics"
  print students
  for s in students:
    for k, v in s.items():
      printNow(k + " - " + v)
  students[0].pop('Major')
  for s in students:
    for k, v in s.items():
      printNow(k + " - " + v)


def main2():
  inputFile = open(pickAFile(),'rt')
  fileData = inputFile.readlines()
  students = []
  for s in fileData:
    items = s.split(';')
    temp = {}
    temp['FirstName'] = items[0]
    temp['LastName'] = items[1]
    temp['Major'] = items[2]
    students.append(temp)
  for stu in students:
    print stu[v]
main2()