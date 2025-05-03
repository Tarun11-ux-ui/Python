pizza = int(input("Which pizza do you want to eat?\n"))
price = 0
if pizza == 1:
    price = 100
    print("Pizza price is $100")
elif pizza == 2:
    price =200
    print("Pizza price is $200")
elif pizza == 3:
    price = 300
    print("Pizza price is $300")

pepperoni = str(input("Do you want to add pepperoni?(yes/no)\n"))
if pepperoni == 'yes' or pepperoni == 'no':
  print("okay! Lets add pepperoni for you")
if pizza == 1:
    price = price + 30
    print(f"\nYour Pizza Price is now ${price}")
elif pizza == 2 or pizza == 3:
    price = price + 20
    print(f"\nYour Pizza Price is now ${price}")
elif pepperoni == 'no':
    print("ok")
    
extra = str(input("\nDo you want to add extra cheese or extra big?(yes/no)\n"))
if extra == 'yes':
    price = price + 40
    print(f"\nFinal Price of your Pizza is ${price}")
    
   
