# Ask for the user's name, if they are called "Bob", print "Welcome Bob!".

name = input("What is your name? ")
if name == "Bob":
    print("Hello, Bob!")

# Ask you for the user's name, if they are not called "Bob", print "You are not Bob!".

if name != "Bob":
    print("You are not Bob!")

# Ask the user for a password, if they enter the password "qwerty123, print "You have successfully logged in". If they get it wrong, print "Password failure".

password = input("What is your password? ")
if password == "qwerty123":
    print("You have successfully logged in.")

if password != "qwerty123":
    print("Password failure.")

#Ask the user to enter a number, if the number is even, print "Even". Otherwise, print "Odd".

number = int(input("Input a number. "))
if (number%2) == 1:
    print("Odd.")
else:
    print("Even.")

# Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise, print "Safe".

number_one = int(input("Give me a number.\n"))
number_two = int(input("Give me another number.\n"))
if (number_one + number_two) > 21:
    print("Bust.")
else:
    print("Safe.")

# Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", print "What's up Bob!", else print "You must be Charlie".

name_two = input("What is your name, cutie?\n")

if name_two == "Alice":
    print("Hello, Alice")
elif name_two == "Bob":
    print("What's up Bob!")
else:
    print("You must be Charlie.")

# Ask the user to enter their age.
# i. If they are younger than 11, print "You are too young to go to school."
# ii. If they are between 11 and 16, print "You can come to this school."
# iii. If they are over 16, print "You're too old for school."
# iv. If they are 0, print "You're not born yet!"

agetwo = int(input("How old are you, sweetie?\n"))

if agetwo < 11 and agetwo >= 1:
    print("You are too young to go to school")
elif agetwo > 11 and agetwo < 16:
    print("You can come to this school.")
elif agetwo > 16:
    print("You're too old for school.")
else:
    print("You're not born yet.")

# Ask the user to enter the name of a month. If the user enters March, April or May, print "Your month is in spring.", Otherwise print "I don't know."
# i. Expand the rest of the year, give that Summer is June, July and August. Autumn is September, October and November. Winter is December, January and February.
# ii. Ensure that when an unknown month is given it prints "That isn't a month, you moron!".

month = input("What is the name of the month at present?\n")

if month == "March" or month == "April" or month == "May":
    print("Your month is in Spring.")
elif month == "June" or month == "July" or month == "August":
    print("Your month is in Summer.")
elif month == "September" or month == "October" or month == "November":
    print("Your month is in Autumn.")
elif month == "December" or month == "January" or month == "February":
    print("Your month is in Winter.")
else:
    print("That isn't a month, you moron!")

# Ask the use for two different numbers, if both numbers are even, print "Even.", if both numbers are odd, print "Odd", else print the product of the two numbers.

number_three = int(input("Give me a number.\n"))
number_four = int(input("OK, now give me another number.\n"))

if (number_three%2) == 0 and (number_four%2) == 0:
    print("Even.")
elif (number_three%2) == 1 and (number_four%2) == 1:
    print("Odd.")
else:
    print(number_three * number_four)

# Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango.

fruits = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
print(fruits)

# Add "Grapes" to the list.

fruits.append("Grapes")
print(fruits)

# Change "Pears" to "Strawberries".

fruits[3] = "Strawberries"

# Remove "Apples" from the list.

del(fruits[1])

# Print out the current length of the list.

print(len(fruits))

# Print out the list.

print(fruits)

# Order the list alphabetically.

fruits.sort()

# Print out the list again.

print(fruits)

# Loop through the list and print them out.

for fruit in fruits:
    print (fruit)

# Print the numbers 1 to 100 (including 100)

for my_number in range(101):
    print(my_number)

# Print all odd numbers from 1 to 100

for my_number in range(1, 100, 2):
    print(my_number)

# The modern olympics started in 1896, print the years in which they have been held.

for my_number in range(1896, 2020, 4):
    print(my_number)
