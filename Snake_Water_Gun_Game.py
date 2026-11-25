#                                    ---Snake, Water, Gun Game---

import random # computer ke liye random choice lene ka module.
'''1 for snake
-1 for water
0 for gun'''

computer = (random.choice([-1, 0, 1])) # Computer randomly -1, 0, ya 1 me se koi ek choose karega.
youstr = input("Enter your choice: ") # youstr user ka raw input (jaise "s", "w", "g").
youDict = {"s" : 1, "w" : -1, "g" : 0} # youDict mapping string → number
reverseDict = {1 : "snake", -1 : "water", 0 : "gun"} # reverseDict mapping number → text (sirf print karne ke liye).
you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}") # Dono choices print karta hai (user aur computer).

if(computer == you):
    print("Its a draw!")
else:  # (snake > water, water > gun, gun > snake)
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    else:
        print("Something went wrong!")


     
