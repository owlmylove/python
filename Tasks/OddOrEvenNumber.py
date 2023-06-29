# Write a program that works out whether if a given number is an odd or even number.

user_number = input("Which number do you want to check? ")

calculation = int(user_number) % 2

if calculation == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

