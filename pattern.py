n=int(input())
for i in range(1,n+1):
    for j in range(ord('a'),ord('a')+i):
        print(chr(j),end='')
        
    print()
