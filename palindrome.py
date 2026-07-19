Y=input("enter the string")
rev=0
while Y>0:
    k=Y%10
    rev=rev*10+k
    Y=Y//10
print(rev)