#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Total bill
total_bill = input("What is the total bill? ")
total_bill_float = float(total_bill)
print(f"{total_bill_float:.2f}")

# Select tips percentage
tips_percentage = input("How many % of tips you want to leave? 10, 12, 15? ")
tips_percentage_int = int(tips_percentage)
print(tips_percentage_int)

# Amount of people to divide the bill
amount_of_people = input("How many people to divide the bill? ")
amount_of_people_int = int(amount_of_people)
print(amount_of_people_int)

# Get the amount of money from tips - 18
count_percentage_from_bill = (total_bill_float * (tips_percentage_int/int(100)))

# Total amount with tips - 150=18
total_amount = (total_bill_float + count_percentage_from_bill)

# Amount each person should pay
each_person_pay = (total_amount/amount_of_people_int)
each_person_pay_float = float(each_person_pay)
print(f"Each person should pay {each_person_pay_float:.2f}")