import random 
computer=random.choice([-1,0,1])

dict={-1:"snake", 0:"water", 1:"gun" }
g="Game is drawn"
w="You Win"
l="You loose"

print("S if for snake")
print("G if for Gun")
print("W if for Water")



you1=input("enter the choice ").lower()

def game():
    if(you1!="s" and you1!="w" and you1!="g"):
        return "Invalid Choice"
    else:
        medict={"s":-1, "w":0, "g":1}
        you=medict[you1]

      

        if(computer==you):
           
            print(f"The computer chose {dict[computer]}")
            return f"{g}"

        elif (computer== -1 and you==0):
            print(f"the computer chose {dict[computer]}")
            return f"{l}"

        elif(computer==-1 and you==1):
            print(f"The computer chose {dict[computer]}")
            return f"{w}"

        elif(computer==0 and you==-1):  
            print(f"The computer chose {dict[computer]}")
            return f"{w}"

        elif(computer==0 and you==1):
            print(f"The computer chose {dict[computer]}")
            return f"{l}"

        elif(computer==1 and you==0):
            print(f"The computer chose {dict[computer]}")
            return f"{w}"

        elif(computer==1 and you==-1):
            print(f"The computer chose {dict[computer]}")
            return f"{l}"


def highscore():
    result=game()
    print(result)
    if result==g:
        with open("tictactoe.txt","a") as t :
            t.write("g")
    elif result==w:
        with open("tictactoe.txt","a") as t :
            t.write("w")
    elif result==l:
        with open("tictactoe.txt","a") as t :
            t.write("l")
highscore()    
with open("tictactoe.txt","r") as r:
    data=r.read()
    print(f"The Game is Drawn {data.count("g")} times")
    print(f"The Game is Won {data.count("w")} times")
    print(f"The Game is Lost {data.count("l")} times")
