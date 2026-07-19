print("Welcome to1 the game of to do")
print("1.Add task")
print("2.View Task")
print("3. Mark Task as Done")
print("4.Delete Task")
print("5.Exit")
L=[]
while True:
    I=int(input("enter the choice"))
    if I==1:
        n=int(input("enter the number of task you have decided "))
        for i in range(1,n+1):
            k=str(input("enter the task"))
            s=k.capitalize()
            u=L.append(s)
        print(L,"are the todays task")
    elif I==3:
        T=str(input("enter the task completed"))
        if T in L:
            L.remove(T)
        else:
            print("TASk not found")
            continue
        print(L,"are the remaining tasks")
    elif I==2:
        print("Tasks:",L)
        continue
    elif I==4:
        T=str(input("enter the task completed"))
        if T in L:
            L.remove(T)
        else:
            print("TASk not found")
            continue
        print(L,"are the remaining tasks")
    elif I==5:
        print("Thank you for becoming the member")
        break

    

