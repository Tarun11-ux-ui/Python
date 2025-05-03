A=str(input("enter first name")).lower()
B=str(input("enter second name")).lower()
count1=0
count2=0
for i in A:
    if i in ["t","r","u","e","l","o","v","e"]:
        count1=count1+1
for i in B:
    if i in ["t","r","u","e","l","o","v","e"]:
        count2=count2+1
love_calculation=str(count1)+str(count2)
print(f"love calculation is {love_calculation}")