import random 
print("welcome to this beautiful game")
N=int(input("enter the number of rounds you wanna play"))
Y={1:"Rock",2:"Scissor",3:"Paper",4:"None"}
computer_choice=0
users_choice=0
for i in range (1,N+1):
     K=str(input("enter your input of game"))
     G=random.randint(1,4)
     R=K.capitalize()
     if R not in Y.values():
         print("invalid input")
         continue
     cm=Y[G]
     if cm==R:
         print("its a draw round")
     elif (
         (cm=="Rock" and R=="Paper") or
         (cm=="Scissor" and R=="Rock") or
         (cm=="Rock" and R=="Scissor")):
             print("you won the round")
             users_choice+=1
     else:
         print("computer miya won the round")
         computer_choice+=1
if users_choice > computer_choice:
    print("u won the game ")
else:
    print("computerji won the game ")
#######################################################################
#yt METHOD
import random
lists=["Rock","Scissor","Paper"]
f=random.choice(lists)
y=str(input("enter your choice"))
T=y.capitalize()
if f==T:
    print("its a draw round")
elif (
    (f=="Rock" and T=="Paper") or
    (f=="Scissor" and T=="Rock") or
    (f=="Rock" and T=="Scissor")):
      print("you won the round")
      
         

       
