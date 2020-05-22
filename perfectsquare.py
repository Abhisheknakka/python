x=int(input("Enter 1st interval: "))
y=int(input("Enter 2nd interval:"))

for i in range(x,y+1):
    if (i**(.5) == int(i**(.5))):
        print(i)
