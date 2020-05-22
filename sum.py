list=[]
n=int(input("Enter the number of elements"))
for i in range(0, n): 
    x=int(input("Enter the your numbers"))
    list.append(x)

print(list)    
sum=0
for e in list:
    sum=sum+e
    
print(sum)
