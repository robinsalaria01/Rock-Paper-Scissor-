import random
n=int(input("How Many Rounds Do You Wanna Play : "))
c=0
c1=0
for j in range(1,n+1):
    i=random.randint(1,3)
    print("Round ",j)
    dic={"Stone","Paper","Scissor"}
    str=input("Stone🪨 Paper📄 Scissor✂️ : ")
    if str not in dic:  
        print("Invalid Input❌\nEnter Stone🪨 Paper📄 Scissor✂️")
        exit()
    if i == 1:
        a="Stone"
    elif i == 2:    
        a="Paper"
    elif i == 3:    
        a="Scissor"
    print("Computer : ",a)
    if a == str:    
        print("Tie 🥲")
    elif a == "Stone" and str == "Scissor" or a == "Paper" and str == "Stone" or a == "Scissor" and str == "Paper":
        print("Computer Wins🦾")
        c+=1
    elif a == "Paper" and str == "Scissor" or a == "Scissor" and str == "Stone" or a == "Stone" and str == "Paper":
        print("You Win 💪") 
        c1+=1
    else:   
        pass
print("Computer Score : ",c)
print("Your Score : ",c1)
if c<c1:
    print("Congratulations, You Win🤩")
else:
    print("Hehehe,Computer Wins😭")