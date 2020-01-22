n= int(input("enter the number"))
l=[[ 0 for i in range (n)]for j in range(n)]
print(l)
low=0
high=n-1
count=1
for i in range((n+1)//2):
    for j in range(low,high+1):
        l[low][j]=count
        count+=1
    for j in range(low+1,high+1):
        l[j][high]=count
        count+=1
    for j in range(high-1,low-1,-1):
        l[high][j]=count
        count+=1
    for j in range(high-1,low,-1):
        l[j][low]=count
        count+=1
    low+=1
    high-=1


    
for i in range(n):
    for j in range(n):
        print(l[i][j],end="\t")
    print()

