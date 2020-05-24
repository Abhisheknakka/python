# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:21:53 2020

@author: Abhi
"""

list=[]
n = int(input("Enter number of elements : ")) 

for i in range(0, n): 
    ele = int(input("enter you numbers")) 
    list.append(ele)

def count(list):
    even=0
    odd=0
    for e in list:
        if e%2==0:
            even+=1
        else:
            odd+=1
            
    return odd,even

even,odd=count(list)



print(list)
print("Even count is {} and Odd count is {}".format(even,odd))

