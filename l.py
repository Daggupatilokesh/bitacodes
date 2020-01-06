a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
n=input('enter the string')
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def palindrome(string):
    if string==string[::-1]:
        print(" i am palindrome")
    else:
        print("i am not palindrome")

print(add(a,b))


 
