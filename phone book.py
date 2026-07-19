import json
try:
    with open("phonebook.txt","r+") as myf:
        phone=json.load(myf)
except:
    phone={}
print("welcome to contacts")
print("1.Add")
print("2.View")
print("3.Search")
print("delete")
print("6.Update")
print("7.Save")
print("8.Sort Alphabetically")
print("Exit")
while True:
    I=int(input("enter your choice"))
    if I==1:
        k=input("enter the name of person to add")
        m=input("enter the number")
        if len(m)==10 and m.isdigit():
            print("no is verified and correct")
        else:
            print("number is not correct")
        phone.update({k:m})
        continue 
    if I==2:
        print(phone)
        continue
    if I==3:
        g=input("enter the item you wanna search")
        if g in phone.keys():
            w=phone.get(g)
            print(w)
            continue
        else:
            print(g,"is not present")
            continue
    if I==4:
        o=str(input("enter the contact u wanna delete "))
        if o in phone.keys():
            phone.pop(o)
            continue
        else:
            print(o,"is not in contacts")
            continue
    if I==6:
        t=input("enter the name u wanna check is duplicate")
        r=phone.keys()
        if t in r:
            u=input("enter the number you wanna update")
            if len(u)==10 and u.isdigit():
                phone.update({t:u})
                print(phone.get(t))
                continue
    if I==7:
        with open("phonebook.txt","r+") as myf:
            json.dump(phone,myf)
            continue
    if I==8:
        k=sorted(phone.items())
        print(k)
        continue
        
    if I==5:
        print("going to exit")
        break
    else:
        print("incorrect input")
        continue
with open("phonebook.txt","r+") as myf:
    json.dump(phone,myf)
    


