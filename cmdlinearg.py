#command line argument
'''from sys import argv
print(argv)
print(type(argv))
sum1=0
for i in argv[1:]:
    sum1=sum1+int(i)
print(sum1)
'''
#argument unpacking(*arg,**kwarg)
'''
def add(*a):
    sum1=0
    for i in a:
        sum1=sum1+i
    print(sum1)
        

add(10,20,30,40,50)

'''
#zip function
'''
l=[1,2,3,4,5]
m=[6,7,8,9,10]
n=[11,12,13,14,15]

for i,j,k in zip(l,m,n):
    print(i,j,k)
'''
#map function
def printvalue(a):
    return(list(a))
b=list(map(printvalue,['bita','academy']))
print(list(b))

