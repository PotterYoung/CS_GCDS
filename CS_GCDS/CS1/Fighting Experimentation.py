dmg_value = 0

import random
import time

print("AN ENEMY APPROACHES!")
turn = "p"

# STATS
en_hp = 175
en_atk = 3
en_def = 3
en_status = "none"

p_hp = 50
p_atk = 5
p_def = 2
p_status = "none"

sw_dmg = 1.5
fb_dmg = 2.25
fb_charge = 3

# PLAYER TURN
while p_hp > 0 and en_hp > 0:
    if turn == "p":
        attack = input('''--------------------------------------------
Your turn!
What attack do you use? (Numbers)
1. Slash
2. Fireball
''')
        atk_value = random.randint(1,20)

        if attack == "1":

            dmg_value = atk_value + p_atk - en_def
            print("Rolling...")
            time.sleep(1)

            if dmg_value * sw_dmg <= 0:
                print("You rolled", atk_value, "( 0 dmg )")
            else:
                print("You rolled", atk_value, "(",dmg_value * sw_dmg,"dmg )")

                if atk_value + p_atk > en_def:
                    en_hp -= dmg_value *sw_dmg
                else:
                    print("The enemy defended the attack!")

                if en_hp > 0:
                    print("The enemy has", en_hp, "HP remaining!")
                else:
                    print("The enemy has 0 health remaning!")
                turn = "e"

        elif attack == "2":
            if fb_charge >= 1:

                dmg_value = atk_value + p_atk - en_def
                print("Rolling...")
                time.sleep(1)

                if dmg_value * fb_dmg <= 0:
                    print("You rolled", atk_value, "( 0 dmg )")
                    print("The fireball had no effect, charge not used")
                else:
                    fb_charge -= 1
                    print("You rolled", atk_value, "(",dmg_value * fb_dmg,"dmg )")
                    print(fb_charge, "firball charges left")

                    if atk_value + p_atk > en_def:
                        en_hp -= dmg_value * fb_dmg
                        if en_status == "fire2":
                            en_status = "fire3"
                            en_def -= 1
                        elif en_status == "fire":
                            en_status = "fire2"
                            en_def -= 1
                        else:
                            en_status = "fire"
                            en_def -= 1
                    else:
                        print("The enemy defended the attack!")

                    if en_hp > 0:
                        print("The enemy has been set on fire!!")
                        print("The enemy has", en_hp, "HP remaining!")
                    else:
                        print("The enemy has 0 health remaning!")

                    turn = "e"
                    
            elif fb_charge <= 0:
                print("Fireball is out of charges!")

        else:
            print("Action not recognized")

# ENEMY TURN
    elif turn == "e":
        print('''--------------------------------------------
Enemy's turn! ''')

        en_atk_value = random.randint(1,20)
        en_dmg_value = en_atk_value + en_atk - p_def
        print("Rolling...")
        time.sleep(1)

        if en_dmg_value <= 0:
            print("The enemy rolled", en_atk_value, "( 0 dmg )")
        else:
            print("The enemy rolled", en_atk_value, "(",en_dmg_value,"dmg )")

        if en_atk_value + en_atk > p_def:
            p_hp -= en_dmg_value
        else:
            print("The enemy defended the attack!")

        if en_status == "fire3":
            en_hp -= 12
            print("The enemy took 12 damage from the fire!", en_hp, "hp remaning!")
        elif en_status == "fire2":
            en_hp -= 6
            print("The enemy took 6 damage from the fire!", en_hp, "hp remaning!")
        elif en_status == "fire":
            en_hp -= 3
            print("The enemy took 3 damage from the fire!", en_hp, "hp remaning!")

        en_hp -= 3
        if p_hp > 0:
            print("You have", p_hp, "HP remaining!")
        else:
                print("You have 0 health remaning!")
        turn = "p"

# FAILSAFE
    else:
        print("Something went terribly wrong here...")
        exit()

# WINNING
if p_hp > en_hp:
    print("You win!")
    exit()
elif en_hp > p_hp:
    print("You lose")
    exit()
else:
    print("Okay something broke...")
    exit()