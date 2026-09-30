'''
Name: Potter Young
Description: A menu of functions
Bugs: None known
Date: 9/29/26
Bonuses: Index function, subtotals of consonants & vowels, 
Log: Version 1.0: 9/29/26 

'''

import random

def main():
    answering_name = True                                               # Creating a variable to make the name loop work

    while answering_name == True:                                       # Setting up a cancellable forever loop
        user_name = input('Please enter a full name: ')                 # Asking the user for a name to be saved as a variable
        while True:                                                     # Forever loop
            yes_no = input(f'Is {user_name} correct? (Y/N) ')           # Confirming if user wants the name (incase of mispellings or deep regret)
            if (yes_no == 'y' or yes_no == 'Y'):                        # Checking if the user confirmed their name
                answering_name = False                                  # Cancelling the cancellable forever loop
                break                                                   # Exiting the current forever loop
            elif (yes_no == 'n' or yes_no == 'N'):                      # Checking if the user denied their name
                break                                                   # Exiting the current forever loop to ask the name question again
            else:                                                       # Checking if it's not a valid answer
                print('Please input a valid answer')                    # Politely asking the user to GET IT RIGHT

    print('''What function would you like to use?
    1) Find a letter in your name
    2) Reverse your name
    3) Check the vowels in your name
    4) Check the consonants in your name
    5) Get your first name
    6) Get your last name
    7) Get your middle name(s)
    8) Check if your name has a hyphen
    9) Turn your name into all lowercase letters
    10) Turn your name into all uppercase letters
    11) Check if your name is a palindrome
    12) Get your initals
    13) Randomly shuffle your name
    X) Quit''')

    while True:                                                                                 # Creating a loop to repeat the choosing functions part of the code
        function_choice = input('')                                                             # Getting an input to be used as the chosen function

        if function_choice == '1':                                                              # If statements for each of the available functions + x to quit
            letter = input('What letter do you want to check your name for? ')                  # Asking for an input to be used on the index function
            if string_index(user_name, letter) < 0:                                             # Checking if it returned as -1 (meaning it was not found)
                print('That letter was not found')                                              # Printing that it was not found
            else:
                print(f'That letter was found in position: {string_index(user_name, letter)}')  # Printing out that it was found in the specific position
        elif function_choice == '2':
            print(reverse(user_name))                                                           # Printing the reversed name
        elif function_choice == '3':
            vowel_check(user_name)                                                              # Calling the vowel check function
        elif function_choice == '4':
            consonant_check(user_name)                                                          # Calling the consonant check function
        elif function_choice == '5':
            print(first_name_find(user_name))                                                   # Printing out the first name
        elif function_choice == '6':
            print(last_name_find(user_name))                                                    # Printing out the last name
        elif function_choice == '7':
            print(middle_name_find(user_name))                                                  # Printing out the middle name(s)
        elif function_choice == '8':
            if hyphen_check(user_name) == True:                                                 # Checking if a hyphen was found or not
                print('A hyphen is in your name!')
            else:
                print('There is not a hyphen in your name')
        elif function_choice == '9':
            print(my_lower(user_name))                                                          # Printing the name in all lowercases
        elif function_choice == '10':
            print(my_upper(user_name))                                                          # Printing the name in all uppercases
        elif function_choice == '11':
            if is_palindrome(user_name) == True:                                                # Checking if the name was a palindrome or not
                print('Your name IS a palindrome!')
            else:
                print('Your name is not a palindrome')
        elif function_choice == '12':
            print(get_initials(user_name))                                                      # Printing the initals
        elif function_choice == '13':
            print(shuffle_name(user_name))                                                      # Printing the shuffled name
        elif my_lower(function_choice) == 'x':
            quit()                                                                              # Quitting out of the program
        else:
            print('Invalid response, try again.')

def string_index(string, wanted_letter):
    '''
    Searches a given string for a specific letter
    Args:
        string (str): the string that will be checked
        wanted_letter (str): the specific letter to check the string with
    Return:
        Integer: the position of the found letter, if none were found the value returns as -1
    '''
    wanted_letter = my_upper(wanted_letter) # Setting the desired letter to be uppercase to remove cap sensitivity
    string = my_upper(string)               # Doing the same with the string itself

    found_pos = -1                          # Creating a variable for the found letter (default being -1 as a "not found" state)
    for i in range(0, len(string)):         # Checking for each letter in the name
        if string[i] == wanted_letter:      # If the letter was the letter being searched for
            found_pos = i                   # Set the found position variable to the letter
            break                           # Breaking if the letter was found
    if found_pos == -1:                     # Checking if the found letter variable is in the "not found" state
        return found_pos + 1                # Returning the position of the desired letter (or lack there of in this case)
    else:                                   # If the letter was found
        return found_pos + 1                # Returning the position of the desired letter

def reverse(string):
    '''
        Reverses a given string
        Args:
            string (str): the string that will be reversed
        Return:
            String: the reversed string
    '''
    reversed_string = ''                                # Setting up an empty string for the reversed string
    string_list = list(string)                          # Turning the string into a list

    for letter in range(len(string_list) -1, -1, -1):   # Creating a for loop for every letter in the string and taking in reverse order
       reversed_string += string_list[letter]           # Adding the current letter to the string
    return reversed_string                              # Returning the finished product

def vowel_check(name):
    '''
    Searches a given string for all vowels, making individual and total counts
    Args:
        name (str): the string that will be checked
    Return:
        String: the final amount of vowels, individual and total
    '''
    name = my_lower(name)                                                                                                                   #  Making the name all lowercase using the lower function to lower the length of the vowel list
    total_vowels = 0                                                                                                                        # Setting a variable for the total number of vowels
    vowel_count = [0, 0, 0, 0, 0]                                                                                                           # Creating a list to store the individual count of each vowel
    vowel_list = ["a", "e", "i", "o", "u"]                                                                                                  # Creating a list of all the vowels

    for letter in name:                                                                                                                     # For loop for every letter in the name
        if letter in vowel_list:                                                                                                            # Checking if the letter is in the list of vowels
            letter_index = vowel_list.index(letter)%5                                                                                       # Creating a variable of the index of the letter with a modulo to connect (or reassign) the values of both the uppercase and lowercase letters to the same values
            vowel_count[letter_index] += 1                                                                                                  # Adding to the value of the specific vowel 
            total_vowels += 1                                                                                                               # Adding to the total amount of vowels

    print(f'Total vowels: {total_vowels}')                                                                                                  # Showing the final count of all the vowels
    print(f'Individual count A: {vowel_count[0]} | E: {vowel_count[1]} | I: {vowel_count[2]} | O: {vowel_count[3]} | U: {vowel_count[4]}')  # Showing the final count of each individual vowel

def consonant_check(name):
    '''
    Searches a given string for all consonants, making individual and total counts
    Args:
        name (str): the string that will be checked
    Return:
        String: the final amount of consonants, individual and total
    '''
    name = my_lower(name)                                                                                                       # Making the name all lowercase using the lower function to lower the length of the consonant list
    total_consonants = 0                                                                                                        # Setting a variable for the total number of consonants
    consonant_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]                                           # Creating a list to store the individual count of each consonant
    consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']  # Creating a list of all the consonants

    for letter in name:                                                                                                         # For loop for every letter in the name
        if letter in consonant_list:                                                                                            # Checking if the letter is in the list of vowels
            letter_index = consonant_list.index(letter)%21                                                                      # Creating a variable of the index of the letter with a modulo to connect (or reassign) the values of both the uppercase and lowercase letters to the same values
            consonant_count[letter_index] += 1                                                                                  # Adding to the value of the specific vowel 
            total_consonants += 1                                                                                               # Adding to the total amount of vowels
    print(f'Total consonants: {total_consonants}')                                                                              # Showing the final count of all the consonants
    print(f'Individual count B: {consonant_count[0]} | C: {consonant_count[1]} | D: {consonant_count[2]} | F: {consonant_count[3]} | G: {consonant_count[4]} | H: {consonant_count[5]} | J: {consonant_count[6]} | K: {consonant_count[7]} | L: {consonant_count[8]} | M: {consonant_count[9]} | N: {consonant_count[10]} | P: {consonant_count[11]} | Q: {consonant_count[12]} | R: {consonant_count[13]} | S: {consonant_count[14]} | T: {consonant_count[15]} | V: {consonant_count[16]} | W: {consonant_count[17]} | X: {consonant_count[18]} | Y: {consonant_count[19]} | Z: {consonant_count[20]} | ') # Showing the final count of each individual consonant

def first_name_find(name):
    '''
    Returns the first word of a given string
    Args:
        name (str): the string that will be checked
    Return:
        String: the first word
    '''
    cut_name = name.split(' ')  # Creating a list of the name split by space
    first_name = cut_name[0]    # Setting the variable that will be returned as the first word of the cut name list 
    return first_name           # Returning the first name

def last_name_find(name):
    '''
    Returns the last word of a given string
    Args:
        name (str): the string that will be checked
    Return:
        String: the last word
    '''
    cut_name = name.split(' ')  # Creating a list of the name split by space
    last_name = cut_name[-1]    # Setting the variable that will be returned as the last word of the cut name list
    return last_name            # Returning the last name

def middle_name_find(name):
    '''
    Returns the middle words of a given string
    Args:
        name (str): the string that will be checked
    Return:
        String: the words in the middle
    '''
    cut_name = name.split(' ')              # Creating a list of the name split by space
    if len(cut_name) <= 2:                  # Checking if the name has only two words 
        return 'No middle name found'       # returning out the result if so
    else:                                   # If it does not:
        end = 0                             # Setting a variable to be used as the "end" parameter when checking for what's the middle name(s)
        for i in range(0, len(name))[::-1]: # Checking backwards for each letter in the list
            if name[i] == ' ':              # If the letter is a space
                end = i -1                  # Setting "end" as the current letter (-1 to account for the space)
                break
        start = 0                           # Setting a variable to be used as the "start" parameter when checking for what's the middle name(s)
        for i in range(0, len(name)):       # Checking for each letter in the list (forward)
            if name[i] == ' ':              # If the letter is a space
                start = i +1                # Setting "end" as the current letter (+1 to account for the space)
                break

        middle_name = name[start:end]       # Setting the middle name to be the list starting from the start parameter to the end parameter
        return middle_name                  # Returning the middle name defined in the previous line

def hyphen_check(name):
    '''
    Checks a string for if it contains a hyphen
    Args:
        name (str): the string that will be checked
    Return:
        Boolean: if a hyphen was found
    '''
    has_hyphen = False          # Creating a boolean for if it contains a hyphen 
    for letter in name:         # Checking each letter of the name
        if letter == "'":       # If the name is a hyphen:
            has_hyphen = True   # Setting the boolean to true
    if has_hyphen == True:      # If a hyphen was found
        return True             # Returns that a hyphen was found
    else:                       # If no hyphen was found
        return False            # Returns that a hyphen was not found

def my_lower(string):
    '''
    Returns the given text as lowercase
    Args:
        string (str): the string that will be changed
    Return:
        String: the string in lowercase
    '''
    output = ''             # Setting a blank string for the output
    string_again = ''       # Setting a blank variable for the letters

    for letter in string:   # Checking for every letter in the string
        num = ord(letter) # Converting num into a number (the ascii hex of the letter)
        if num >= 65 and num <= 90: # If the number is imbetween 65 and 90 (uppercases of the ascii chart)
            num += 32 # Adding 32 to the number (to convert it to its lowercase variant)
            string_again = chr(num) # Converting back into a letter using the ascii hex
            output += string_again # Adding the converted letter to the output
        else: # If the number is not (lowercase or other)
            output += letter # Adding the letters without any fancy mumbo jumbo
    return output           # Printing the output

def my_upper(string):
    '''
    Returns the given text as uppercase
    Args:
        string (str): the string that will be changed
    Return:
        String: the string in uppercase
    '''
    output = ''                         # Setting a blank string for the output
    string_again = ''                   # Setting a blank variable for the letters

    for letter in string:               # Checking for every letter in the string
        num = ord(letter)               # Converting num into a number (the ascii hex of the letter)
        if num >= 97 and num <= 122:    # If the number is imbetween 97 and `11` (lowercases of the ascii chart)
            num -= 32                   # Subtracting 32 to the number (to convert it to its uppercase variant)
            string_again = chr(num)     # Converting back into a letter using the ascii hex
            output += string_again      # Adding the converted letter to the output
        else:                           # If the number is not (lowercase or other)
            output += letter            # Adding the letters without any fancy mumbo jumbo
    return output                       # Returning the output

def is_palindrome(name):
    '''
    Checks if the string is a palindrome
    Args:
        name (str): the string that will be checked
    Return:
        Boolean: if the string is a palindrome
    '''
    name = my_lower(name)       # Making sure no capitals mess up the palindrome checking by making every letter lowercase
    if name == reverse(name):   # Checking if the name is the same as itself reversed
        return True             # Returning a boolean if it is true
    else:                       # If not
        return False            # Returning a boolean if it is false

def get_initials(name):
    '''
    Gets the first letter of each word of the given string
    Args:
        name (str): the string that will be used
    Return:
        String: the first letters of each word
    '''
    initials_list = ''                              # Creating an empty string for the initials to be added to
    amount = 0                                      # Creating a variable to track the position of what name tne code's on
    split_name = name.split(' ')                    # Creating a variable of the name split by each space

    for word in split_name:                         # For loop for each name in the split names
        more_split_name = list(split_name[amount])  # Splitting the split name further (into individual letters)
        initials_list += f'{more_split_name[0]}.'   # Adding the first letter of the name to the string with a "." at the end
        amount += 1                                 # Adding to the amount variable
    return initials_list                            # Returning the completed list

def shuffle_name(name):
    '''
        Randomly shuffles the given string
        Args:
            name (str): the string that will be shuffled
        Return:
            String: the shuffled name
    '''
    split_name = list(name)                 # Making a list of each individual letter of the name
    length = len(split_name)                # Setting a variable for the length of the name
    finished_name = ''                      # Creating a variable to be used for the final name

    while length > 0:                       # A while loop for while there are still letters left
        rand = random.randint(0, length-1)  # Getting a random number from within the length of the name
        finished_name += split_name[rand]   # Adding the randomly decided letter to the finished name
        split_name.pop(rand)                # Removing the randomly decided letter from the original name
        length -= 1                         # Removing 1 from the length
    return finished_name                    # Returning the finished name

main()