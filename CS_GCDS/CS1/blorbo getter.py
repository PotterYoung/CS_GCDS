import random
import time
import sys
import os

if os.name == 'nt':
    os.system('cls')

blorbo_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cyan', 'magenta', 'tuquoise', 'pink', 'white', 'black', 'gray']
blorbo_rare_colors = ['gold', 'silver', 'bronze', 'rainbow']
blorbo_personalities = ['energetic', 'depressed', 'irritable', 'adventurous']
blorbo_sizes = ['itty bitty', 'small', 'average size', 'big', 'extra large']
blorbo_tags = ['n ancient', ' demonic', 'n angelic', ' mystic', ' mysterious', ' experienced']
# common(50%) uncommon(25%) rare(12.5%) epic(7.5%) legendary(3%) mythic(1%)

def type_text(text, speed=0.075):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def get_blorbo(egg):
    georgiana = False
    type_text('Hatchin', 0.15)
    type_text('g...', 0.5)
    print('')

    if (egg == 'common' or egg == 'rare'):
        blorbo_color = random.choice(blorbo_colors)
        blorbo_personality = random.choice(blorbo_personalities)
        blorbo_size = random.choice(blorbo_sizes)
        blorbo_tag = ' normal'

    elif (egg == 'epic' or egg == 'legendary'):
        blorbo_color = random.choice(blorbo_rare_colors)
        blorbo_personality = random.choice(blorbo_personalities)
        blorbo_size = random.choice(blorbo_sizes)
        blorbo_tag = random.choice(blorbo_tags)

    elif egg == 'hell':
        hell_tags = [' hellish', ' demonic', ' devilish', ' ritualistic', ' burning', ' scorching', ' firey']
        hell_colors = ['brown', 'red', 'orange', 'yellow']
        hell_personalities = ['malicious', 'despicable', 'bloodthirsty', 'evil']

        blorbo_color = random.choice(hell_colors)
        blorbo_personality = random.choice(hell_personalities)
        blorbo_size = random.choice(blorbo_sizes)
        blorbo_tag = random.choice(hell_tags)
        
    elif egg == 'odyssey':
        ody_tags = [' godlike', ' thunder bringing', ' tele- uhh umm...', ' puppeteering', ' waiting', ' suffering', ' war torn', ' greek', 'n immortal']
        ody_personalities = ['adventuruous', 'ruthless', 'prophetic', 'dangerous', 'determined to get home', 'a warrior of the mind', 'a damsel in distress', 'here to entertain', 'reckless (sentimental at best)']

        blorbo_color = random.choice(blorbo_colors)
        blorbo_personality = random.choice(ody_personalities)
        blorbo_size = random.choice(blorbo_sizes)
        blorbo_tag = random.choice(ody_tags)

    elif egg == 'reference':
        ref_tags = [' very tragic', ' gay', ' nerdy', ' queer', ' dnd playing', ' queercoded', ' determined', 'n eepy', ' ruthless', ' dangerous', ' mentally tortured', ' brave', ' perserverant', 'n integrity', ' kind', ' patient', ' justice seeking', 'n integritous', ' consternated', ' trasgendrnr', ' harsh and sweet and bi']
        ref_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'bisexually lit', 'rainbow', '(sparkly) magenta', 'sandy', '(olive) green', '(feather) gray', 'ourple', 'blurple', '(cobalt) blue', '(blood) red', '(cerulean) blue']
        ref_personalities = ['more equal than others', 'a fixer', 'a loser', 'a theatre kid', 'obsessed with football (in the future)', 'ham cracker. cheese cracker. ham cheese. ham and cheese cracker. ham and cheese', 'a space probe', 'in a lot of debt', 'stuck in a time loop', 'greedy (it led to their downfall)', 'to my consternation I let her go', 'her name is ANYA']

        blorbo_color = random.choice(ref_colors)
        blorbo_personality = random.choice(ref_personalities)
        blorbo_size = random.choice(blorbo_sizes)
        blorbo_tag = random.choice(ref_tags)

        g_chance = random.randint(1,100)
        if g_chance >= 95:
            georgiana = True
        else:
            georgiana = False

    else:
        print('Whoops, an error occured! :(')
        exit()

    if georgiana == False:
        type_text(f'''You got a{blorbo_tag} {blorbo_color} blorbo that's {blorbo_size} and {blorbo_personality}!
''')
    elif georgiana == True:
        type_text(f'''You got a{blorbo_tag} {blorbo_color} blorbo tha- EXCUSE ME OVER HERE!!!!
''')

get_blorbo('reference')
get_blorbo('reference')
get_blorbo('reference')
get_blorbo('reference')
get_blorbo('reference')