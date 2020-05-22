side = int(input("Please Enter any Side of a Square  : "))

print("Square Number Pattern uisng FOR LOOP") 
for i in range(side):
    for i in range(side):
        print('#', end = '')
    print()
    
    
i = 0
print("Square Number Pattern using WHILE LOOP") 
while(i < side):
    j = 0    
    while(j < side):  
        print('#', end = '')
        j = j + 1
    i = i + 1
    print()
