n=int(input("enter the num"))
for i in range(0,n):
    for j in range(n-i,0,-1):
        print(" ", end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print("*",end=" ")
        
    print()
    
