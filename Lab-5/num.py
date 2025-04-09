row=int(input("Enter the number of row : "))

for i in range (1,(row+1)):
    print(" "* (row-i) + " ".join(str(num) for num in range(1,i+1)))
    
for i in range ((row-1),0,-1):
    print(" "* (row-i) + " ".join(str(num) for num in range(1,i+1)))
