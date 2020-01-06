'''a=[4,2,9,6,3,5]
c=[]
count=0
for i in a[count::]:
    
    c.append(min(a))
    a.remove(min(a))
    count=count+1
    
print(c)'''
n=[4,2,9,6,3,5,3,4]
for i in range(len(n)):
    min_value=min(n[i:])
    min_index=n.index(min_value)
    n[i],n[min_index]=n[min_index],n[i]
    print(n)
    
    
