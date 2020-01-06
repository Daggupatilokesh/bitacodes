'''key=int(input("enter the keypad value"))
click=int(input("enter the click value"))
dict1={1:'1',2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
if key==7 or key==9:
    a=dict1[key][click%4-1]
    print(a)
else:
    a=dict1[key][click%3-1]
    print(a)'''
num=int(input('enter the value of num'))
if num!=1:
    while num!=1:
        rem=num/2
        num=rem
         print("SQR")
    else:
        print("not sqr of 2")
    
