# SETUP
dmg_value = 0

import random
import time

# STATS
en_hp = random.randint(125,150)
en_atk = 3
en_def = 3
en_status = "none"

p_hp = 50
p_atk = 5
p_def = 5
p_status = "none"

sw_dmg = 1
fb_dmg = 1.5
fb_charge = 3
ds_charge = 2
xs_dmg = 1.75

print("AN ENEMY APPROACHES! They have", en_hp, "hp!")
turn = "p"

# PLAYER TURN
while p_hp > 0 and en_hp > 0:
    while turn == "p":
        attack = input('''--------------------------------------------
Your turn!
What attack do you use? (Numbers)
1. Slash
2. Fireball
3. Defensive Stance
4. X-Slash
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
            if fb_charge > 0:

                dmg_value = atk_value + p_atk - en_def
                print("Rolling...")
                time.sleep(1)

                if dmg_value * fb_dmg <= 0:
                    print("You rolled", atk_value, "( 0 dmg )")
                    print("The fireball had no effect, charge not used")
                else:
                    fb_charge -= 1
                    print("You rolled", atk_value, "(",dmg_value * fb_dmg,"dmg )")
                    print(fb_charge, "fireball charges left")

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
                    
            else:
                print("Fireball is out of charges!")
        
        elif attack == "3":
            if ds_charge > 0:
                print("Rolling...")
                time.sleep(1)

                if atk_value >= 15:
                    p_def *= 2 
                    p_def = round(p_def, 0)
                    print("You rolled", atk_value, "defense raised by 2x! (", p_def, ")")
                    print(ds_charge -1, "defensive stance charges remain!")
                    ds_charge -= 1
                    turn = "e"
                elif atk_value >= 10:
                    p_def *= 1.5
                    p_def = round(p_def, 0)
                    print("You rolled", atk_value, "defense raised by 1.5x! (", p_def, ")")
                    print(ds_charge -1, "defensive stance charges remain!")
                    ds_charge -= 1
                    turn = "e"
                else:
                    p_def *= 1.25
                    p_def = round(p_def, 0)
                    print("You rolled", atk_value, "defense raised by 1.25x! (", p_def, ")")
                    print(ds_charge -1, "defensive stance charges remain!")
                    ds_charge -= 1
                    turn = "e"
            else:
                print("Defensive stance is out of charges!")

        elif attack == "4":
            dmg_value = atk_value + p_atk - en_def
            big_atk_value = dmg_value * xs_dmg
            big_atk_value = round(big_atk_value, 1)
            print("Rolling...")
            time.sleep(1)

            if dmg_value * xs_dmg <= 0:
                print("You rolled", atk_value, "( 0 dmg )")
            else:
                print("You rolled", atk_value)

                if atk_value + p_atk > en_def:
                    en_hp -= big_atk_value
                    print("The attack hit once! (", big_atk_value, "dmg )")
                    time.sleep(0.25)
                    big_atk_value2 = big_atk_value * 1.5
                    big_atk_value2 = round(big_atk_value2, 1)
                    en_hp -= big_atk_value2
                    print("The attack hit twice! (", big_atk_value2, "dmg ) You need a turn to rest.")
                    p_status = "stunned"
                else:
                    print("The enemy defended the attack!")

                if en_hp > 0:
                    print("The enemy has", en_hp, "HP remaining!")
                else:
                    print("The enemy has 0 health remaning!")
                turn = "e"

            

        else:
            print("Action not recognized")

# ENEMY TURN
    while turn == "e":
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

        if en_status == "fire3":
            en_hp -= 24
            print("The enemy took 24 damage from the fire!", en_hp, "hp remaning!")
        elif en_status == "fire2":
            en_hp -= 12
            print("The enemy took 12 damage from the fire!", en_hp, "hp remaning!")
        elif en_status == "fire":
            en_hp -= 6
            print("The enemy took 6 damage from the fire!", en_hp, "hp remaning!")

        if en_atk_value + en_atk > p_def:
            p_hp -= en_dmg_value
        else:
            print("You defended the attack!")

        if p_hp > 0:
            print("You have", p_hp, "HP remaining!")
        else:
                print("You have 0 health remaning!")

        if p_status == "stunned":
            p_status = "none"
        else:
            turn = "p"

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