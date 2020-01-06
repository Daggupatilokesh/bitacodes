valid=False
mail=input('enter the number')
if "@" in mail:
    if mail.count("@")==1:
       if mail[mail.index('@')+1].isalpha():
           if "." in mail[mail.index('@'):]:
               valid=True
if valid:
    print("mail is valid")
else:
    print("mail is in valid
          ")



"""
started=False

while True:
    a=input("enter the value").lower()
    if a=="start":
        if started:
            print("car already started")
        else:
            print('carstarted')
            started=True
    elif a=="stop":
        if not started:
            print("car is aleady stopped")
        else:
            print('car stopped')
            started=False
    elif a=="help":
        print('''start---- to start th car
stop---- to stop the car
help---- for help
exit---- to exit''')
    elif a=="exit":
        break
    else:
        print("i dont understand")"""
    
                    
 
