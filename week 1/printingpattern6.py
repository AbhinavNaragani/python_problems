'''
6.       *
        **
       ***
      ****
     *****

'''
i=1
n=int(input("enter n"))
while i<=n:
    j=1
    while j<=n-i:
        print(" ", end="")
        j=j+1
    j=1
    while j<=i:
        print("*", end="")
        j=j+1
    print()
    i=i+1



