import json
try:
    with open ("passwordinventory.txt","r") as myf:
        passwd=json.load(myf)
except:
    passwd=[]
while True:
    print("1.add password")
    print("2.View Password")
    print("3. Search Password")
    print("4.Exit")
    I=int(input("enter your choice"))
    if I==1:
        password=str(input("enter the password"))
        username=str(input("enter the username"))
        website=input("enter the website")
        w={"website":website,"username":username,"password":password}
        passwd.append(w)
        with open ("passwordinventory.txt","w") as myf:
            json.dump(passwd,myf)
            print("your password is added")
            continue
    if I==2:
        print(passwd,"is the password list")
        continue
    if I==3:
        J=str(input("enter the website directory u want to search"))
        found=False
        for item in passwd:
            if item["website"]==J:
                print("Website :", item["website"])
                print("Username:", item["username"])
                print("Password:", item["password"])
                found=True
        if not found:
            print("Website is not found.")
            print("if you want to add this password Press 1")
            u=int(input(" "))
            if u==1:
                website = J
                password = input("Enter password: ")
                username = input("Enter username: ")
                w = {
                "website": website,
                "username": username,
                "password": password
                }
                passwd.append(w)
                with open ("passwordinventory.txt","w") as myf:
                        json.dump(passwd,myf)
                print("your password is added")
                continue
    if I==4:
        print("exiting the program")
        break                

