a=input("enter the 1st string")
b=input("enter the 2nd string")
a=list(a)
b=list(b)
a.sort()
b.sort()
print(a,b)
if a==b:
    print ("it is anagram")
else:
    print("it is not anagram")
            
        
