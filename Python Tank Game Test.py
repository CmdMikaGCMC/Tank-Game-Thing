import random

#Global Variables
#HP
LTHP = 30
MTHP = 55
HTHP = 70
#Damage
LTDMG = 8
MTDMG = 17
HTDMG = 21
#Manouverability
LTMAN = 80
MTMAN = 70
HTMAN = 45


#Input
tank1 = input("Tank 1 type (Light, Medium, Heavy): ").title()[0]
tank2 = input("Tank 2 type (Light, Medium, Heavy): ").title()[0]

while tank1 not in ["L", "M", "H"] or tank2 not in ["L", "M", "H"]:
    print("\nInvalid input, try again.")
    tank1 = input("Tank 1 type (Light, Medium, Heavy): ").title()[0]
    tank2 = input("Tank 2 type (Light, Medium, Heavy): ").title()[0]

if tank1 == "L":
    tank1HP = LTHP
    tank1DMG = LTDMG
    tank1MAN = LTMAN
elif tank1 == "M":
    tank1HP = MTHP
    tank1DMG = MTDMG
    tank1MAN = MTMAN
elif tank1 == "H":
    tank1HP = HTHP
    tank1DMG = HTDMG
    tank1MAN = HTMAN

if tank2 == "L":
    tank2HP = LTHP
    tank2DMG = LTDMG
    tank2MAN = LTMAN
elif tank2 == "M":
    tank2HP = MTHP
    tank2DMG = MTDMG
    tank2MAN = MTMAN
elif tank2 == "H":
    tank2HP = HTHP
    tank2DMG = HTDMG
    tank2MAN = HTMAN
    
print("Player 1 HP, DMG and Manouverability is:", tank1HP, tank1DMG, tank1MAN,"Player 2 HP, DMG and Manouverability is:",tank2HP,tank2DMG,tank2MAN)
print("\nConfirm - Player 1 is", tank1+"T and Player 2 is", tank2+"T. - Begin")
print("******************************************************************************************************")

#Special note
tank2MOD = tank2MAN


#Actual Game
def roll():
    global tank1HP, tank1DMG, tank1MAN, tank2MOD, tank2HP, tank2DMG, tank2MAN, tank1, tank2
    if tank1 == "L":
        tank1MAN = LTMAN
    elif tank1 == "M":
        tank1MAN = MTMAN
    elif tank1 == "H":
        tank1MAN = HTMAN
    if tank2 == "L":
        tank2MAN = LTMAN
    elif tank2 == "M":
        tank2MAN = MTMAN
    elif tank2 == "H":
        tank2MAN = HTMAN
    
    acc1 = 0
    acc2 = 0

    choice1 = input("\nPlayer 1 Choice. Manouver or Standby to fire? ").title()[0]
    if choice1 == "M":
        acc1 = random.randint(0,100)-10
        tank1MAN += 10
    elif choice1 == "S":
        acc1 = random.randint(0,100)+5
    if acc1 >= tank2MOD:
        if acc1 >= 95:
            tank2HP = tank2HP - tank1DMG*2
            print("Critical hit, Tank 2 on", tank2HP,"HP. Accuracy was", str(acc1)+"%.")
        else:
            tank2HP = tank2HP - tank1DMG
            print("Hit, Tank 2 on", tank2HP,"HP. Accuracy was", str(acc1)+"%.")
        if tank2HP <= 0:
            print("Game over, Player 1 Wins.")
    else:
        print("Miss. Accuracy was", str(acc1)+"%.")
        
    choice2 = input("\nPlayer 2 Choice. Manouver or Standby to fire? ").title()[0]
    if choice2 == "M":
        acc2 = random.randint(0,100)-10
        tank2MOD = tank2MAN + 10
    elif choice2 == "S":
        acc2 = random.randint(0,100)+5
        tank2MOD = tank2MAN
    if acc2 >= tank1MAN:
        if acc2 >= 95:
            tank1HP = tank1HP - tank2DMG*2
            print("Critical hit, Tank 1 on", tank1HP,"HP. Accuracy was", str(acc2)+"%.")
        else:
            tank1HP = tank1HP -tank2DMG
            print("Hit, Tank 1 on", tank1HP,"HP. Accuracy was", str(acc2)+"%.")
        if tank1HP <= 0:
            print("Game over, Player 2 wins.")
    else:
        print("Miss. Accuracy was", str(acc2)+"%.")



while tank1HP > 0 and tank2HP > 0:
    roll()
