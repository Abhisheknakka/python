Print("Enter the input values of x and y")
x=int(input("Enter 1st interval as a input: "))
y=int(input("Enter 2nd interval as a input:"))

for i in range(x,y+1):
    if (i**(.5) == int(i**(.5))):
        print("It is a perfect square",i)
