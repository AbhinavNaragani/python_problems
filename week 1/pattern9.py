'''
9.  *********
     *******
      *****
       ***
        *

'''

i=1
n=int(input("enter n value:"))
while i<=n:
    j=1
    while j<=i-1:
        print(" ", end="")
        j=j+1
    j=1
    while j<=((2*n)-(2*i)+1):
        print("*", end="")
        j=j+1
    i=i+1
    print()