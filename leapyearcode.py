year=int(input("enter year you want to check?"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(" not leap year")
        else:
            print("LEaP yeaR")
else:
    print("Not a leap year")            