import random
import time

bp = 0 # Base Power - Base power of an attack without adding coin power
cp = 0 # Coin Power - The power that's added everytime a head is flipped
sp = 0 # Sanity Points - Affects the chances of flipping heads (45 through -45)
cn = 0 # Coin Number - The amounts of coins flipped from an attcnk

# Enemy Stats
en_lvl = 0
en_hp = 0

en_statuses = []
en_speed_min = 0
en_speed_max = 0
en_off = 0
en_def = 0

en_slash = 1
en_blunt = 1
en_pierce = 1

en_pride = 1
en_gloom = 1
en_lust = 1
en_envy = 1
en_gluttony = 1
en_wrath = 1
en_sloth = 1

# coin clfip limbus Cooommmmmmmmpnayyyyyyyyyyyy
def coinflip(bp,cp,sp,cn):
    while cn > 0:
        heads = 0
        head_chance = 50 + sp
        coin_flip = random.randint(1, 100)
        if coin_flip <= head_chance:
            print('heads')
            heads += 1
        else:
            print('tails')
        cn -= 1
        time.sleep(0.25)

    result = bp + (cp * heads)
    print(result)
    return int(result)

def clash(bp1,cp1,sp1,cn1, bp2,cp2,sp2,cn2):
    for i in range(cn):
        at = coinflip(bp1,cp1,sp1,cn1)
        en = coinflip(bp2,cp2,sp2,cn2)

        if at > en:
            print('la')
        elif en > at:
            print('lala')
        else:
            print('tie')