1. num = int(input("Enter a number"))
   print(f"multipication table for {num}:")
   for i in range(1 , 11):
       print(f"{num} X {i} = {num * i}")

2.  n = 5
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i -1))

3.  n = 5
    for i in range(n-1,0,-1):
        print(" " * (n - i) + "*" * (2 * i -1)) 

4.  rows = int(input("Enter the number of rows'))
    for i in range(1,rows + 1):
        print(" " * (rows-1) + " ".join(num)  for rows in range(1,i + 1)))

5.  rows = int(input("Enter the number of rows :"))
    for i in range(1,rows + 1):
        print(" " * (rows-i) + " ".join(str(num)  for num in range(1,i + 1)))              

6.  n = 5
    for i in range(1, n + 1):
        print(" " * (n - i) + f"{i}" * (2 * i - 1))
