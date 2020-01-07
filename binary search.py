a=[12,8,6,9,3,2,5,13,19]
n=int(input('enter the search number'))
a.sort()
for i in a:
    
    if a[len(a)//2]==n:
        print("present")
        break
    
    elif a[len(a)//2]>n:
        b=a[0:len(a)//2:]
        a=b
    elif a[len(a)//2]<n:
        c=a[len(a)//2:len(a):]
        a=c
        
else:
    print('not present')
    count=+1
            



