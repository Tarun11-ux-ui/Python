height = int(input("Enter your height in cm : "))
if (height>=150):
    age = int(input("Enter your age : "))
    if (age <= 18):
        print("The  ticket price is 250")
    else :
        print("The ticket price is 500")
else:
    print("You are eligible to ride")