import random

def game():
    i=1
    n=int(input("enter no of trials"))
    c=0
    d=0
    while i<=n:
        player_choice=input("enter choice: rock/paper/scissors : ")
        options=["rock","paper","scissors"]
        computer_choice=random.choice(options)
        choices={"player":player_choice,"Computer":computer_choice}
        print(choices)
        if player_choice==computer_choice:
            c+=1
        else:
            d+=1
        i+=1
    if c<d:
        return "Player Won"
    elif c>d:
        return "Player lost"
    else:
        return "Draw"
print(game())