N=int(input("enter the number of members "))
trent=int(input("enter the rent total"))
tfood=int(input("enter the food total"))
telec=int(input("enter the units spend"))
char=int(input("enter the charge per unit"))
k=telec*char
print("₹",k,"is the electricity bill")
U=trent+tfood+k
print("₹",U,"is the total expenditure")
E=U/N
print("₹",E,"is the total cost per person")
