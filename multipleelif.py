height=int(input("enter height"))
if(height>3):
    want_photos=int(input("do you want extra photos?"))
    if (want_photos==1):
        
        age=int(input("enter your age"))
        if(age<12):
            print("price is 400")
        elif(12<age>=18):
            print("500")
        else:
            print("700")
    print("50 extra")
else:
    print("not allowed")            

