import random

for i in range(5):
    print("Hello World!")

print('''
''')

for i in range(1, 10, 2):
    print(i)

print('''
''')

colors = []

for i in range(3):
    colors.append(random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'orange']))
print(colors)

for color in colors:
    print(colors)