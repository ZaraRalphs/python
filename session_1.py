# Create two variables, one that holds the width and one that holds the height of a rectangle, then, work out and store the area in a third variable. Print out the string: 'Rectangle of width <x> and height <y> has an area of <area>'
width = 5
height = 6
area = (width*height)
print('A rectangle of ' + str(width) + ' and ' + str(height) + ' has an area of ' + str(area) +'.')

# Write code that prints the length of the string, 'pyton'.

print(len('python'))

# Print out the first and third letter of the word 'python'.

word = 'python'
print(word[0])
print(word[2])

# Ask the user to enter their name, and print out "Hello, ,name".

name = input("What is your name? ")
print("Hello " + name)

# Ask the user to enter their age, tell them how old they will be in 15 years time.

age = int(input("How old are you? "))
age_plus_15_years = age + 15
print("In 15 years, you will be " + str(age_plus_15_years) + ".")

# Combine the first two input statements above and print out the message "Hello, , you are at present. In 15 years you will be . "

print("Hello " + name + " you are " + str(age) + " at present. In 15 years, you will be " + str(age_plus_15_years) + ".")

# Ask the user to enter their hometown, print it out in UPPERCASE letters.

hometown = input("Where is your hometown? ")
upper_home = hometown.upper()
print(upper_home)