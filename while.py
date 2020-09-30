i = 1

while i <= 100:
    if i%3 == 0 or i%5 ==0:
        i = i+1
    else:
        print(i)
        i=i+1

        
Using for loop



n=int(input("Enter the number"))

i=1
for i in range(n):
    if(i%3==0 or i%5==0):
        i=i+1
    else:
        print(i)
i=i+1
