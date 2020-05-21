from array import *
from math import *

arr1=array('i',[])

n=int(input("Enter the length of array"))

for i in range (n):
    x=int(input("Enter your numbers"))
    arr1.append(x)
    
print(arr1)    


arr2=array(arr1.typecode,(x**3 for x in arr1))
print(arr2)

