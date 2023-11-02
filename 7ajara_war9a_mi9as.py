#war9a>hajra
#hajra>mi9as
#mi9as>war9a
import random 
user_point=0
pc_point=0
options=["hajra","war9a","mi9as"]
# options = [0, 1, 2]

while True:
    user_pick=input("Enter war9a / hajra/ mi9as or q to quit  ").lower
    if user_pick=='q':
        break

    if user_pick in options:
        break
    
    random_number = random.randint(0, 2)
    pc_pick = options[random_number]
    print("pc :",pc_pick)
    if (user_pick=="hajra")and(pc_pick=="mi9as"):
        user_point+=1
        print("You won")
        

    elif (user_pick=="war9a")and(pc_pick=="hajra"):
        user_point+=1
        print("You won")
        

    elif (user_pick=="mi9as")and(pc_pick=="war9a"):
        user_point+=1
        print("You won")
       
    elif(user_pick=="mi9as")and (pc_pick=="mi9as") or (user_pick=="war9a")and (pc_pick=="war9a") or (user_pick=="hajra")and (pc_pick=="hajra"):
        print("Draw");
    else:
        print("You lost!")
        pc_point+=1

print("You won ,and you got",user_point, "points")
print("PC got",pc_point, "points")
print("GOODBYE")

   
    
