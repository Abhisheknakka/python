from array import *

arr=array('i',[])

n=int(input("Enter the length of the array"))

for i in range (n):
    x=int(input("Enter your numbers"))
    arr.append(x)
    
print(arr)


arr2=array(arr.typecode,[])
del_2=int(input("Enter the number you want to delete"))
for e in arr2:
    if del_2==e:
        continue
    else:
        arr2.append(e)
        
        
print("the new array is :\n",arr2)        



