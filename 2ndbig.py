name=input("enter the name")
ope=["{","[","("]
clo=["}","]",")"]
if len(name)%2==0:
    for i in range(0,int(len(name)/2)):
        if name[i] in ope:
            if clo[i]!=name[-1-i]:
                   print("inviled")
                   break
    else:
        print('viled')
else:
    print("inviled")
           
 
