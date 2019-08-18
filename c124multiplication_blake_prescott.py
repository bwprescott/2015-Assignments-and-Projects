#!/usr/bin/python3

""" Args: 2 arrays of n bits """
def binary_multiplication(a_arr, b_arr):

        
        print('a_arr={} b_arr={}'.format(a_arr, b_arr))

        # transforming the input for conveniency:
        # 	- we are only interested in a's value
        #	- iteration over b's bits should be from R to L, so just reverse the array
        a = binary2decimal(a_arr)
        b_arr = list(reversed(b_arr))

        # store the partial products
	c = [0]*len(b_arr)

        #### YOUR CODE HERE ####
        ## assuming that you keep the transformations above, loop should go from 0 to n-1
        ## = range(0,n) where n is len(b_arr)

        ## TIP: you can (left-)shift an integer by j positions, as follow
        #             n = ( n << j )
        # Alternatively, you multiply by 2^j. In Python:
        #             n = n * (2 ** j)
	product = 0
        
        for j in range(0, len(b_arr)):
                if b_arr == 1:
                        c[j] = (a << j)
                else:
                        c[j] = 0
                product += c[j]
        return product


		
"""return decimal value of an array of n bits"""
def binary2decimal(a):
        s = 0
        for j in range(0,len(a)):
                s = (s*2) + a[j]
        return s


print(binary_multiplication([0,1,0,1],[1,1,1,0]))
