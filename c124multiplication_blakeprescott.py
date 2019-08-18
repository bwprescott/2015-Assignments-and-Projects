#!/usr/bin/python3

""" Args: 2 arrays of n bits """
def binary_multiplication(a_arr, b_arr):

        
        print('a_arr={} b_arr={}'.format(a_arr, b_arr))

        a = binary2decimal(a_arr)
        print(a)
        b_arr = list(reversed(b_arr))
        
        c = [0]*len(b_arr)
        
        product = 0
        
        for j in range(0, len(b_arr)):
                
                if b_arr[j] == 1:
                        c[j] = a * (2 ** j)
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
