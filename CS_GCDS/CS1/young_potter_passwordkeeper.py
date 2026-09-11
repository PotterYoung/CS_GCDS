import time
import os
import random
import csv

def pass_entry(skip):                                                          # Password entry system
    '''
    Has the user guessing a password to get entry to the rest of the program
    Args:
        skip (boolean): checks if this function is skipped or not
    Returns:
        None
    '''
    inc_guesses = 0
    if skip == False:
        while True:
            if inc_guesses < 6:
                guess = input('Enter a password to continue: ')

                if guess.lower() == 'llama':                                  # check if the guess is llama (ignoring caps)
                    time.sleep(0.3)
                    break
                else:
                    if inc_guesses == 0:                                      # give a hint once they've guessed
                        print('Hint: its an animal')
                    if inc_guesses == 3:                                      # give another hint once they've guessed 3 times
                        print('This animal often lives on the mountains in South America')
                    inc_guesses += 1
            else:                                                             # lock them out after 6 incorrect guesses and reset everything
                print('Sorry, youre locked out for 10 minutes')
                time.sleep(600)
                inc_guesses = 0

def add_pass(apps, usernames, passwords):                                     # Adding new information sets
    '''
    Adds a set of new information to the lists
    Args:
        None
    Returns:
        None
    '''
    new_app = input('Input the name of an app: ')                             # ask for a new app username and password
    new_user = input('Whats the username? ')
    new_pass = input('Whats the password? ')
    apps.append(new_app)                                                      # add the new info to the respective lists
    usernames.append(new_user)
    passwords.append(new_pass)
    time.sleep(0.5)

def check_info(app_name, apps, usernames, passwords):                         # Checking a certain set of information
    '''
    Checks the specific information of a list
    Args:
        app_name (str): the inputted name of the app they want to check
        apps, usernames, passwords (str): syncing the list values
    Returns:
        None
    '''
    if app_name in apps:                                                     # check if the app name inputted is in the apps list
        app_index = apps.index(app_name)                                     # make a value that is the index value of the app name
        print(f'App: {apps[app_index]}')                                     # print out the information of the selected app
        print(f'Username: {usernames[app_index]}')
        print(f'Password: {passwords[app_index]}')
        input('(Press enter to continue)')
    else:
        print('App not found.')
    time.sleep(0.5)

def change_info(app_name, apps, usernames, passwords):                       # Changing a certain set of information
    '''
    Changes the specific information of a list
    Args:
        app_name (str): the inputted name of the app they want to check
        apps, usernames, passwords (str): syncing the list values
    Returns:
        None
    '''
    if app_name in apps:                                                     # check if the inputted app is in the app list
        app_index = apps.index(app_name)                                     # getting the index value of the selected app
        while True:
            pass_or_user = input('''What info would you like to change?
1. Username
2. Password
''')
            if pass_or_user == '1':                                          # if they choose username or password get the respective password and replace it with what they type
                usernames[app_index] = input('Enter a new username: ')
            elif pass_or_user == '2':
                passwords[app_index] = input('Enter a new password: ')
            else:
                print('Invalid response')
                continue
            break
    else:
        print('App not found.')
    time.sleep(0.5)

def pass_strength(app_name, apps, passwords):                               # Check the strength of a certain password
    '''
    Checks the strength of a specific password
    Args:
        app_name (str): the inputted name of the app they want to check
        apps, usernames, passwords (str): syncing the list values
    Returns:
        String: the strength of the given password
    '''
    score = 0
    total_chars = 0
    spec_chars = 0
    cap_chars = 0

    if app_name in apps:                                                   # check if the app is in the app list
        app_index = apps.index(app_name)                                   # getting the index value of the given app
        the_pass = passwords[app_index]                                    # setting a value that is the corresponding password
        total_chars = len(the_pass)                                        # checking the total characters in the password

        for char in the_pass:                                              # checking if each character is a capital or a special character
            if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '|', '"', ':', ';', "'", '<', ',', '>', '.', '/', '?']:
                spec_chars += 1
            elif char == char.upper():
                cap_chars += 1

        if total_chars >= 15:
            score += 40
        elif total_chars >= 12:
            score += 30
        elif total_chars >= 8:
            score += 20          
        elif total_chars <= 6: 
            score += 5

        if spec_chars >= 4:
            score += 30
        elif spec_chars >= 2:
            score += 20
        elif spec_chars <= 1:
            score += 10

        if cap_chars >= 4:
            score += 30
        elif cap_chars >= 2:
            score += 20
        elif cap_chars >= 1:
            score += 10
        print(f'This password got a strength score of {score}!')
        input('(Press enter to continue) ')
    else:
        print('App not found.')
    time.sleep(0.5)

def generate_pass(length):                                             # Generating a random strong password
    '''
    Generates a strong password
    Args:
        length (int): the inputted length of the desired password
    Returns:
        String: the generated password
    '''
    strong_password = []
    nb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sc = ['`', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '"', ':', ';', "'", '<', ',', '>', '.', '/', '?']

    if length % 4 == 0:                                               # Depending of the length inputted, getting a (mostly) even amount of characters (lowercase, uppercase, special, and numbers)
        lc_letters = (length//4)
        uc_letters = (length//4)
        sc_letters = (length//4)
        nb_letters = (length//4)
    elif length % 4 == 1:
        lc_letters = (length//4) + 1
        uc_letters = (length//4)
        sc_letters = (length//4)
        nb_letters = (length//4)
    elif length % 4 == 2:
        lc_letters = (length//4) + 1
        uc_letters = (length//4) + 1
        sc_letters = (length//4)
        nb_letters = (length//4)
    elif length % 4 == 3:
        lc_letters = (length//4) + 1
        uc_letters = (length//4) + 1
        sc_letters = (length//4) + 1
        nb_letters = (length//4)

    for i in range(lc_letters):                                     # continuing after the last part, adding the given amount of characters per thing
        strong_password += random.choice(lc)
    for i in range(uc_letters):
        strong_password += random.choice(uc)
    for i in range(sc_letters):
        strong_password += random.choice(sc)
    for i in range(nb_letters):
        strong_password += random.choice(nb)

    random.shuffle(strong_password)                                 # randomly shuffling the characters
    print(''.join(strong_password))                                 # joining the letters together into a string
    input('Feel free to copy and paste this! (Press enter to continue)')
    return(''.join(strong_password))

def export_info(aps, pws, uns):                                     # Exporting all the info to a spreadsheet
    '''
    Exports the three lists onto a spreadsheet
    Args:
        aps, uns, pws (str): syncing the list values
    Returns:
        None
    '''
    data = zip(aps, uns, pws)                                      # taking in the information
    with open('passkeeper.csv', 'w', newline='') as csvfile:       # opening the specific spreadsheet
        writer = csv.writer(csvfile)
        writer.writerow(['Apps', 'Usernames', 'Passwords'])        # creating rows for each set of data
        writer.writerows(data)                                     # adding the data to each rows
    print(f'Saved to "passkeeper.csv"')
    input('(Press enter to continue) ')

def main(): # The main function, allowing the calling of other functions
    '''
    Creates a selection menu for each of the previous functions
    Args:
        None
    Returns:
        None
    Raises:
        ValueError: if ps_length is not an integer
    '''
    apps = []
    usernames = []
    passwords = []

    while True:
        if os.name == 'nt':                                        # clearing the previous text
            os.system('cls')
        print('''What do you want to do? (Enter 'q' to quit)
1. Add new information
2. Check certain information
3. Edit certain information
4. Check all information
5. Check the strength of a password
6. Generate a secure password
7. Clear all lists
8. Export the info into a spreadsheet''')
        answer = input('').lower()

        if answer == "1":                                         # calling the function to add a new set of info
            add_pass(apps, usernames, passwords)

        elif answer == "2":                                       # calling the funciton to check specific info
            an = input('What apps info do you want to check? (Caps Matter): ')
            check_info(an, apps, usernames, passwords)

        elif answer == "3":                                       # calling the function to change specific info
            an = input('What app do you want to change the info of? (Caps Matter): ')
            change_info(an, apps, usernames, passwords)

        elif answer == "4":                                       # printing out all the values of the lists
            print(apps)
            print(usernames)
            print(passwords)
            input('(Press enter to continue)')

        elif answer == "5":                                       # calling the function to check the strength of a password
            an = input('What apps password do you want to check the strength of? (Caps Matter): ')
            pass_strength(an, apps, passwords)

        elif answer == "6":                                       # calling the function to create a strong password
            while True:                                           # making sure the inputted password length is an integer
                ps_length = input('How long do you want the password to be? (I suggest 8 or more) ')
                try:
                    ps_length = int(ps_length)
                    break
                except ValueError:
                    print('Please enter an integer!')
            generate_pass(ps_length)
    
        elif answer == '7':                                       # clearing the info lists
            apps = []
            usernames = []
            passwords = []
            input('All information cleared! (Press enter to continue) ')

        elif answer == '8':                                       # calling the function to export the info
            export_info(apps, passwords, usernames)

        elif answer == "q":
            quit()

        else:
            print('Not a valid response, please try again')

pass_entry(False)
main()