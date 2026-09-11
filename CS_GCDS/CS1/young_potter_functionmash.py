import random
import time
import os

def chorus():
    '''
    Prints the chorus of a song
    Args:
        None
    Return:
        Print (str): the chorus of a song
    '''
    print('''
I see a song of past romance, I see the sacrifice of man
I see portrayals of betrayal and a brother's final stand
I see you on the brink of death, I see you draw your final breath
I see a man who gets to make it home alive, but it's no longer you''')

def sing_song():
    '''
    Prints out a song with the help of the chorus() function
    Args:
        None
    Return:
        Print (str): a song
    '''
    print('''
I am the prophet with the answers you seek
Time, I've unlocked it, I see past and future running free
There is a world where I help you get home
But that's not a world I know
What?''')
    chorus()
    print('''
This can't be
We've suffered and sailed through the toughest of hells
Now you tell us our effort's for nothing?
I see your palace covered in red
Faces of men who had long believed you're dead
I see your wife with a man who is haunting
A man with a trail of bodies
WHO???''')
    chorus()
    
def add(num1, num2):
    '''
    Takes two numbers and adds them together
    Args:
        num1 (str): the first inputted number
        num2 (str): the second inputted number
    Return:
        Print (str): the sum of the two numbers
    '''
    print(num1 + num2)

def print_list(array):
    '''
    Prints out all elements in a given list
    Args:
        array (str): the list it will print
    Return:
        Print (str): each element of the list
    '''
    for i in array:
        print(i)

def in_list(array, element):
    '''
    Checks if a given element is in a given array
    Args:
        array (str): the list that it will check
        element (str): the specific element it is searching for within the list
    Return:
        Boolean: true if the element is in the list false if not
    '''
    return element in array

def is_integer(any_parameter):
    '''
    Checks if a given parameter is an integer
    Args:
        any_parameter (str): the parameter that will be checked
    Return:
        Boolean: True if it is an integer false if otherwise
    Raises:
        ValueError: if any_parameter is not an integer
    '''
    try:
        int(any_parameter)
        return True
    except ValueError:
        return False

def get_integer(context=' number'):
    '''
    Gets an integer using the is_integer() function
    Args:
        context (str): text that can be changed depending on the context, defaulted to ' number'
    Return:
        Int: the inputted number
    '''
    while True:
        number = input(f'Please enter a{context}: ')
        
        if is_integer(number):
            return int(number)
    
def get_random():
    '''
    Gets a random number inbetween two numbers it gets from the get_integer() function
    Args:
        None
    Return:
        Print (str): the random number that's selected
    '''
    rand1 = get_integer(' number')
    rand2 = get_integer('nother number')

    if rand1 > rand2:
        print(random.randrange(rand2, rand1))
    else:
        print(random.randrange(rand1, rand2))

def count_vowels(a_string):
    '''
    Counts the number of vowels in a given string
    Args:
        a_string (str): the string that gets analyzed for its vowels
    Return:
        Print (str): The amount of vowels along with the total letters
        Print (str): The subtotal of vowels and consonants
    '''
    vowels = 0
    
    for char in str(a_string).lower():
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
            print(vowels)
            time.sleep(0.1)

    print(f'There are {vowels} vowels in this string out of {len(a_string)} letters!')
    print(f'({vowels} vowels, {len(a_string) - vowels} consonants)')

def reverse_string(a_string):
    '''
    Reverses a given string
    Args:
        a_string (str): the string that will be reversed
    Return:
        String: the reversed message
    '''
    reversed_message = ''
    a_list = list(a_string)

    for index in range(len(a_list)-1, -1, -1):
       reversed_message += a_list[index]
    return reversed_message

    #or you could use "a_string[::-1]"

def is_palindrome(a_string):
    '''
    Checks if the given string is a palindrome
    Args:
        a_string (str): the string that will be checked
    Return:
        Print (str): stating if the string is or is not a palindrome
        Boolean: returning true or false based on if the string is a palindrome
    '''
    if a_string.lower() == reverse_string(a_string.lower()):
        print(f'{a_string} IS a palindrome!')
        return True
    else:
        print(f'{a_string} is NOT a palindrome')
        return False

def get_initials(name):
    '''
    Returns all the initials of a given name(string)
    Args:
        name (str): the string that the initials will be taken from
    Return:
        String: the initials
    '''
    initials = ''
    names = name.split(' ')

    for n in names:
        initials += n[0]
    return initials

def replace_characters(a_string, old_char, new_char):
    '''
    Replaces certain characters in a string with new characters
    Args:
        a_string (str): the string that will have its characters replaced
        old_char (str): the character that will be replaced
        new_char (str): the character that will replace the old character
    Return:
        String: the finished message after replacing the characters
    '''
    new_string = ''

    for char in a_string:
        if char == old_char:
            new_string += new_char
        else:
            new_string += char
    return new_string

def corrupt_text(text, corruption):
    '''
    Replaces random letters in a string with a certain character
    Args:
        text (str): the string that will have its letters replaced
        corruption (str): the character that will replace the letters
    Return:
        Print (str): the text post-replacement
    '''
    corrupted_text = ''
    
    for char in text:
        crpt_chance = random.randint(1,5)
        if crpt_chance >= 4:
            corrupted_text += corruption
        else:
            corrupted_text += char
    print(corrupted_text)

def pump_water(capacity, rise):
    '''
    A little game where you have to press enter to fill water
    Args:
        capacity (str): the max capacity of water that needs to be pumped
        rise (str): the amount of water each pump fills
    Return:
        Print (str): saying when the water has been fully pumped
    '''
    print('Press enter repeatedly to pump water!')
    water_level = 0
    
    while water_level < capacity:
        pump = input('')
        
        if pump == '':
            water_level += rise
            if water_level > capacity:
                print(f'{capacity}/{capacity}')
            else:
                print(f'{water_level}/{capacity}')
    print('Filled to max capacity!')

def random_reverse(text):
    '''
    Reverses random words in a string
    Args:
        text (str): the string that will have its words reversed
    Return:
        Print (str): the text after the reversal
    '''
    message = text.split()
    changed_text = ''

    for word in message:
        reverse_chance = random.randint(1,5)

        if reverse_chance >= 4:
            changed_text += reverse_string(word) + " "
        else:
            changed_text += word + " "

    print(changed_text)

def main():
    '''
    A menu that allows the user to select all the previous functions
    Args:
        None
    Return:
        none
    '''
    if os.name == 'nt':
            os.system('cls')
    while True:
        print('''Please select a function from this list to run (Respond with a number)
1. sing_song
2. add
3. print_list
4. in_list 
5. is_integer
6. get_random
7. count_vowels
8. reverse_string
9. is_palindrome
10. get_initials
11. replace_characters
12. corrupt_text
13. pump_water
14. random_reverse
(Q to quit)''')
        function_select = input('')

        if function_select == '1':
            sing_song()
            input('(Enter to continue)')

        elif function_select == '2':            
            n1 = get_integer()
            n2 = get_integer('another number')
            add(n1, n2)
        
        elif function_select == '3':
            while True:
                list_choice = input('''What list would you like to print? (ingredients, musicals, or alphabet)
''').lower()
                if (list_choice == 'ingredients' or list_choice == 'musicals' or list_choice == 'alphabet'):
                    if list_choice == 'ingredients':
                        list_choice = ['flour', 'sugar', 'eggs', 'chocolate chips', 'hydrochloric acid']
                    elif list_choice == 'musicals':
                        list_choice = ['epic', 'hades town', 'anastasia', 'hamilton', 'into the woods']
                    elif list_choice == 'alphabet':
                        list_choice = ['a', 'b', 'c', 'd', 'e', 'f']
                    break
                else:
                    print('Invalid list')
            print_list(list_choice)

        elif function_select == '4':
            while True:
                list_choice = input('''What list would you like to print? (ingredients, musicals, or alphabet)
''').lower()
                if (list_choice == 'ingredients' or list_choice == 'musicals' or list_choice == 'alphabet'):
                    element_choice = input('''Choose an element within the list
''').lower()
                    if list_choice == 'ingredients':
                        output = in_list(['flour', 'sugar', 'eggs', 'chocolate chips', 'hydrochloric acid'], element_choice)
                    elif list_choice == 'musicals':
                        output = in_list(['epic', 'hades town', 'anastasia', 'hamilton', 'into the woods'], element_choice)
                    elif list_choice == 'alphabet':
                        output = in_list(['a', 'b', 'c', 'd', 'e', 'f'], element_choice)
                    break
                else:
                    print('Invalid list')
            if output:
                print(f'{element_choice} IS in {list_choice}')
            else:
                print(f'{element_choice} is NOT in {list_choice}')

        elif function_select == '5':
            num_choice = input('Type something to check if its an integer! ')
            output = is_integer(num_choice)
            if output:
                print(f'{num_choice} IS an integer!')
            else: print(f'{num_choice} is NOT an integer!')

        elif function_select == '6':
            get_random()

        elif function_select == '7':
            the_string = input('''Type in a message!
''')
            count_vowels(the_string)

        elif function_select == '8':
            the_string = input('''Type in something to reverse!
''')
            output = reverse_string(the_string)
            print(output)

        elif function_select == '9':
            the_string = input('''Type in a message to see if its a palindrome!
''')
            is_palindrome(the_string)

        elif function_select == '10':
            the_name = input('''Type in a name to get the initials of!
''')
            output = get_initials(the_name)
            print(output)

        elif function_select == '11':
            the_string = input('''Type the message that will have its characters replaced (Caps matter!)
''')
            the_old_char = input('''Type the character you want to replace
''')
            the_new_char = input('''Type what you want to replace the old character with
''')
            print(replace_characters(the_string, the_old_char, the_new_char))

        elif function_select == '12':
            the_text = input('''Type the message you want corrupted
''')
            the_corruption = input('''Type what you want the corruption to be
''')
            corrupt_text(the_text, the_corruption)

        elif function_select == '13':
            while True:
                the_capacity = int(input('''What do you want the capacity to be? (Integer)
'''))
                output1 = is_integer(the_capacity)
                if output1:
                    break
                else:
                    print('Invalid response, please type an integer')
            while True:
                the_rise = int(input('''How much should it rise by each pump? (Integer)
'''))
                output2 = is_integer(the_rise)
                if output2:
                    break
                else:
                    print('Invalid response, please type an integer')

            pump_water(the_capacity, the_rise)

        elif function_select == '14':
            the_text = input('''Type the text you want affected
''')
            random_reverse(the_text)

        else:
            print('Not a valid input, try again')
            time.sleep(0.5)
            if os.name == 'nt':
                os.system('cls')
            continue

        time.sleep(3)
        if os.name == 'nt':
            os.system('cls')

main()