# Exercise 1
string = 'wool'
string_length = len(string) -1
index = 0
letter = -1

while index <= string_length:
    print(string[letter])
    index += 1
    letter -= 1

# Exercise 3
def count(string, letter):
    number = 0
    for let in string:
        if let == letter:
            number += 1
    print(number)

count('lalala', 'l')
