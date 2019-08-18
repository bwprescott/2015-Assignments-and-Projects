#!/usr/bin/python3

print("Addition")


def add(a, b):

 print(a, b)
 c = 0
 s = [0] * (len(a) + 1) 
 #whatever you were trying to do with .format was causing this to not work, so I took it out. It's probably because this isn't quite python
 for j in reversed(range(0, len(a))):
		d = (a[j] + b[j] + c) // 2
		s[j] = (a[j] + b[j] + d) - 2*d
		print("j: " + str(j) + " a: " + str(a[j]) + " b: " + str(b[j]) + " c: " + str(c) + " d: "+ str(d) + " s: " + str(s[j]))
		c = d
	#also didn't like the way you presented your end data, so I changed that too.
 return(s)
	

add([1,0,1], [1,1,0])
