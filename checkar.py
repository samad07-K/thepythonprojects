import random 
def game():
    print("your game is gonna start")
    k=random.randint(1,69)
    #fetch his hiscore
    with open("harry.txt") as f:
        hiscore=f.read()
        if hiscore!="":
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(hiscore,"is the hiscore")
    if (k>hiscore):
        with open("harry.txt","w") as f:
            f.write(str(k))
    return k 
G=game()
print(G)

